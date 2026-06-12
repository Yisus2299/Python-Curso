#!/usr/bin/env python3
"""
Organize Downloads folder by type and date.
Usage:
  python organize_downloads.py            # run once on detected Downloads
  python organize_downloads.py --path "C:\\Users\\You\\Downloads"
  python organize_downloads.py --watch    # continuous monitor (requires watchdog)
  python organize_downloads.py --dry-run # show what would be done
"""
from __future__ import annotations
import argparse
import logging
import os
import platform
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, Optional

TEMP_EXTS = {'.crdownload', '.part', '.tmp', '.partial'}
DEFAULT_MAP: Dict[str, Iterable[str]] = {
    "Images": ("jpg","jpeg","png","gif","webp","tiff","svg"),
    "Videos": ("mp4","mkv","avi","mov","webm"),
    "Documents": ("pdf","doc","docx","xls","xlsx","pptx","txt","odt"),
    "Audio": ("mp3","wav","m4a","flac","aac"),
    "Archives": ("zip","rar","7z","tar","gz"),
    "Installers": ("exe","msi","msix","pkg","deb","rpm"),
    "Code": ("py","js","java","cs","cpp","c","rb","go","php","html","css"),
}

def get_known_downloads() -> Path:
    home = Path.home()
    # Windows: prefer USERPROFILE\Downloads
    if platform.system() == "Windows":
        up = os.environ.get("USERPROFILE") or os.environ.get("HOME")
        if up:
            p = Path(up) / "Downloads"
            if p.exists():
                return p
    # XDG user dirs (Linux)
    config = home / ".config" / "user-dirs.dirs"
    if config.exists():
        try:
            text = config.read_text(encoding="utf-8")
            m = re.search(r'XDG_DOWNLOAD_DIR\s*=\s*"(.*)"', text)
            if m:
                p = m.group(1).replace("$HOME", str(home)).replace("~", str(home))
                return Path(p).expanduser()
        except Exception:
            pass
    # Common fallback names
    for candidate in (home / "Downloads", home / "Descargas"):
        if candidate.exists():
            return candidate
    # Last resort: return ~/Downloads (may not exist yet)
    return home / "Downloads"

def ext_to_category(ext: str, mapping: Dict[str, Iterable[str]]) -> str:
    e = ext.lower().lstrip(".")
    for cat, exts in mapping.items():
        if e in exts:
            return cat
    return "Others"

def safe_move(src: Path, dest: Path, dry_run: bool=False) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        base = dest.stem
        suf = dest.suffix
        n = 1
        while True:
            candidate = dest.with_name(f"{base} ({n}){suf}")
            if not candidate.exists():
                dest = candidate
                break
            n += 1
    if dry_run:
        logging.info("DRY: move %s -> %s", src, dest)
    else:
        shutil.move(str(src), str(dest))
        logging.info("Moved %s -> %s", src, dest)
    return dest

def organize_once(path: Path, mapping: Dict[str, Iterable[str]], date_by: str="mtime", target_parent: Optional[Path]=None, dry_run: bool=False):
    if target_parent is None:
        target_parent = path
    for p in path.iterdir():
        if p.is_dir():
            continue
        if p.suffix.lower() in TEMP_EXTS:
            logging.debug("Skipping temp file %s", p.name)
            continue
        try:
            stat = p.stat()
        except Exception:
            logging.exception("stat failed for %s", p)
            continue
        if date_by == "mtime":
            dt = datetime.fromtimestamp(stat.st_mtime)
        elif date_by == "ctime":
            dt = datetime.fromtimestamp(stat.st_ctime)
        else:
            dt = datetime.now()
        date_str = dt.strftime("%Y-%m-%d")
        cat = ext_to_category(p.suffix, mapping)
        dest_dir = target_parent / cat / date_str
        dest = dest_dir / p.name
        safe_move(p, dest, dry_run=dry_run)

def parse_args():
    ap = argparse.ArgumentParser(description="Organize Downloads by type and date")
    ap.add_argument("--path", "-p", help="Downloads folder path (overrides auto-detect)")
    ap.add_argument("--watch", "-w", action="store_true", help="Run in monitor mode (requires watchdog)")
    ap.add_argument("--dry-run", action="store_true", help="Do not move files, only log actions")
    ap.add_argument("--log", default="organize_downloads.log", help="Log file path")
    ap.add_argument("--date-by", choices=("mtime","ctime","now"), default="mtime", help="Which date to use for folder names")
    return ap.parse_args()

def main():
    args = parse_args()
    logging.basicConfig(level=logging.INFO, filename=args.log, filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    logging.getLogger().addHandler(console)

    downloads = Path(args.path) if args.path else get_known_downloads()
    logging.info("Using downloads path: %s", downloads)
    if not downloads.exists():
        logging.error("Path does not exist: %s", downloads)
        sys.exit(1)

    if args.watch:
        try:
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler, FileCreatedEvent
        except Exception:
            logging.error("watchdog not installed. Install with: pip install watchdog")
            sys.exit(1)

        class Handler(FileSystemEventHandler):
            def on_created(self, event):
                if isinstance(event, FileCreatedEvent):
                    import time
                    time.sleep(1)
                    try:
                        organize_once(downloads, DEFAULT_MAP, date_by=args.date_by, dry_run=args.dry_run)
                    except Exception:
                        logging.exception("Error organizing on event")

        observer = Observer()
        observer.schedule(Handler(), str(downloads), recursive=False)
        observer.start()
        logging.info("Watching %s ...", downloads)
        try:
            while True:
                import time
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        organize_once(downloads, DEFAULT_MAP, date_by=args.date_by, dry_run=args.dry_run)
        logging.info("Done organizing %s", downloads)

if __name__ == "__main__":
    main()
