# PDF to Audio Converter

A Python application that converts PDF documents into audiobooks using text-to-speech technology.

## Overview

This project converts PDF files into MP3 audio files using Google's Text-to-Speech (gTTS) service. It extracts text from PDF documents, splits it into manageable chunks (to avoid API limits), and generates audio files that can be played on any MP3 player.

## Features

- **PDF Text Extraction**: Reads text from PDF files using PyPDF2
- **Text Chunking**: Splits large text into chunks under 4000 characters
- **Text-to-Speech**: Generates MP3 audio using gTTS
- **Multi-language Support**: Works with multiple languages
- **Command-line Interface**: Easy to use via command line arguments

## Tech Stack

- **PDF Processing**: PyPDF2
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Audio Handling**: io.BytesIO for in-memory processing

## Project Structure

```
Part - Project 91 python PDF to audio/
├── audio.py                 # Main application
├── requirements.txt         # Python dependencies
├── audiobook.mp3           # Sample output file
├── hola me llamo zyran.pdf # Sample input file
└── README.md               # This file
```

## Installation & Setup

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line

```bash
python audio.py <pdf_file> [-o output.mp3] [--lang en]
```

#### Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `pdf_file` | Path to input PDF | Required |
| `-o, --out` | Output MP3 filename | `audiobook.mp3` |
| `--lang` | Language code | `en` |

#### Example

```bash
python audio.py "my_document.pdf" -o "audiobook.mp3" --lang es
```

### As a Python Module

```python
from audio import pdf_to_audio

# Convert PDF to MP3
pdf_to_audio("document.pdf", "output.mp3", lang="en")
```

## Supported Languages

gTTS supports many languages including:

| Code | Language |
|------|----------|
| `en` | English |
| `es` | Spanish |
| `fr` | French |
| `de` | German |
| `it` | Italian |
| `pt` | Portuguese |
| `ru` | Russian |
| `ja` | Japanese |
| `ko` | Korean |
| `zh` | Chinese |

## How It Works

### 1. PDF Text Extraction

```python
def pdf_to_text(path):
    reader = PdfReader(path)
    pages = [p.extract_text() or "" for p in reader.pages]
    return "\n".join(pages)
```

- Opens PDF using PyPDF2
- Extracts text from each page
- Joins all pages into single string

### 2. Text Chunking

```python
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
```

- Splits text into chunks under 4000 characters
- Respects word boundaries (doesn't cut words)
- gTTS has a 5000 character limit, so we use 4000 as safety margin

### 3. MP3 Generation

```python
def save_mp3_chunks(chunks, out_path, lang="en"):
    with open(out_path, "wb") as out_file:
        for chunk in chunks:
            tts = gTTS(text=chunk, lang=lang)
            buffer = io.BytesIO()
            tts.write_to_fp(buffer)
            out_file.write(buffer.getvalue())
```

- Creates gTTS object for each chunk
- Writes audio to in-memory buffer
- Appends each chunk to output file

### 4. Main Function

```python
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
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| `FileNotFoundError` | PDF file doesn't exist | Check file path |
| `ValueError` | No extractable text (scanned PDF) | Use OCR instead |
| gTTS errors | Network issues | Check internet connection |

## Limitations

1. **Scanned PDFs**: Cannot extract text from scanned images (needs OCR)
2. **Complex Formatting**: May not preserve complex layouts
3. **Language Detection**: Must specify language manually
4. **Internet Required**: gTTS requires internet connection
5. **Character Limits**: gTTS has API limits (handled by chunking)

## Alternatives for Production

For production use, consider:

- **pyttsx3**: Offline TTS (less natural voice)
- **Amazon Polly**: Professional TTS
- **Azure Speech**: Microsoft TTS service
- **OCR + TTS**: For scanned documents

## Example Output

```
$ python audio.py "hola me llamo zyran.pdf" -o "my_audiobook.mp3" --lang es
Saved: my_audiobook.mp3
```

## Requirements

```
PyPDF2>=3.0.0
gTTS>=2.3.0
```

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)