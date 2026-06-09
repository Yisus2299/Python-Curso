import io
from pathlib import Path
from gtts import gTTS
from PyPDF2 import PdfReader

def pdf_to_text(path):
    reader = PdfReader(path)
    pages = [p.extract_text() or "" for p in reader.pages]
    return "\n".join(pages)

def chunk_text(text, max_chars=4000):
    words = text.split()
    chunks, cur = [], []
    cur_len = 0
    for w in words:
        if cur_len + len(w) + 1 > max_chars:
            chunks.append(" ".join(cur))
            cur, cur_len = [], 0
        cur.append(w); cur_len += len(w) + 1
    if cur: chunks.append(" ".join(cur))
    return chunks

def save_mp3_chunks(chunks, out_path, lang="en"):
    with open(out_path, "wb") as out_file:
        for chunk in chunks:
            tts = gTTS(text=chunk, lang=lang)
            buffer = io.BytesIO()
            tts.write_to_fp(buffer)
            out_file.write(buffer.getvalue())

def pdf_to_audio(pdf_path, out_mp3="audiobook.mp3", lang="en"):
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    text = pdf_to_text(pdf_file)
    if not text.strip():
        raise ValueError("No extractable text found in PDF.")

    chunks = chunk_text(text)
    save_mp3_chunks(chunks, out_mp3, lang=lang)
    print("Saved:", out_mp3)

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="PDF → MP3 (gTTS)")
    p.add_argument("pdf", help="Path to PDF file")
    p.add_argument("-o", "--out", default="audiobook.mp3")
    p.add_argument("--lang", default="en")
    args = p.parse_args()
    pdf_to_audio(args.pdf, args.out, args.lang)