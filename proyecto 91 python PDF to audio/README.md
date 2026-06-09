# PDF to Audio

This project converts a PDF file to an MP3 audiobook using Python.

## Requirements
- Python 3.8+

## Install dependencies
```powershell
py -3 -m pip install --upgrade pip
py -3 -m pip install -r requirements.txt
```

## Run
```powershell
py -3 audio.py "mi_archivo.pdf" -o "mi_audio.mp3"
```

## Notes
- `ffmpeg` is no longer required for this version.
- If the PDF is scanned images instead of text, the script will not extract text correctly.
- For a scanned PDF, OCR is needed (`pytesseract` + `pdf2image`).
