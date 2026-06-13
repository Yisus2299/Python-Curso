# Birthday Email Gift Project

This is an automated Python application that sends birthday greeting emails to people in a CSV file.

## Overview

This project is a scheduled automation script that checks a CSV file containing birthdays and sends automated email greetings to anyone whose birthday matches the current date. It uses Gmail SMTP to send emails and reads configuration from a .env file.

## Features

- **CSV-based Data**: Store contacts with name, email, month, and day
- **Automated Birthday Detection**: Compares today's date with CSV records
- **Email Automation**: Sends personalized birthday emails via Gmail SMTP
- **Environment Variables**: Secure credential management via .env file
- **Error Handling**: Validates emails, dates, and handles missing files
- **Timezone Support**: Configurable timezone for accurate date matching

## Tech Stack

- **Language**: Python
- **Email**: smtplib with SSL
- **Data**: CSV file handling
- **Configuration**: python-dotenv
- **Date/Time**: datetime, zoneinfo (Python 3.9+)

## Project Structure

```
09/07/2026 proyecto 32 Email Gift Birthay/
├── birthay_gif_proyect.py   # Main application
├── birthdays.csv            # Contact database
├── .env                     # Environment variables (credentials)
└── README.md                # This file
```

## CSV File Format

The `birthdays.csv` file should have the following columns:

```csv
nombre,email,mes,dia
John Doe,john@example.com,6,15
Jane Smith,jane@example.com,6,20
```

| Column | Description |
|--------|-------------|
| nombre | Person's name |
| email | Email address |
| mes | Month (1-12) |
| dia | Day (1-31) |

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
   pip install python-dotenv
   ```

4. **Configure .env file**:

   Create a `.env` file with:
   ```env
   EMAIL_SENDER=your-email@gmail.com
   GMAIL_PASSWORD=your-app-password
   TZ=America/New_York
   ```

5. **Create/update birthdays.csv**:
   ```csv
   nombre,email,mes,dia
   John Doe,john@example.com,6,12
   Jane Smith,jane@example.com,6,15
   ```

6. **Run the application**:
   ```bash
   python birthay_gif_proyect.py
   ```

## How It Works

### Step 1: Load Environment Variables

```python
from dotenv import load_dotenv

load_dotenv(dotenv_path=ENV_FILE, override=True)

EMAIL_SENDER = get_env_value("EMAIL_SENDER")
PASSWORD = get_env_value("GMAIL_PASSWORD")
TZ = get_env_value("TZ") or "America/Santiago"
```

### Step 2: Get Current Date

```python
from datetime import datetime
from zoneinfo import ZoneInfo

today = datetime.now(ZoneInfo(TZ))
month_today, day_today = today.month, today.day
```

### Step 3: Read CSV and Find Birthdays

```python
with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        nombre = row["nombre"].strip()
        email = row["email"].strip()
        mes = int(row["mes"])
        dia = int(row["dia"])
        
        if mes == month_today and dia == day_today:
            birthdays_today.append((nombre, email))
```

### Step 4: Validate Data

```python
def email_valid(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1]

# Validate each row
if not email_valid(email):
    print(f"Invalid email ({email}), the row is skipped.")
    continue

if not (1 <= mes <= 12) or not (1 <= dia <= 31):
    print(f"Invalid date ({mes}/{dia}) for {nombre}, the row is skipped.")
    continue
```

### Step 5: Send Emails

```python
import ssl
import smtplib
from email.message import EmailMessage

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(EMAIL_SENDER, PASSWORD)
    
    for name, email in birthdays_today:
        msg = EmailMessage()
        msg["From"] = EMAIL_SENDER
        msg["To"] = email
        msg["Subject"] = f"For {name} on their unique and special day 🎉🌙💛🌻🌸"
        msg.set_content(
            f"Hello {name},\n\n"
            f"Happy birthday, {name}! 🎉🎂\n\n"
            f"Have a wonderful day and that all your wishes come true.\n\n"
            f"With love, Jesus\n"
        )
        
        smtp.send_message(msg)
        print(f"Sent to {name} <{email}>")
```

## Email Configuration

### Gmail App Password

To send emails via Gmail, you need an **App Password** (not your regular password):

1. Go to Google Account → Security
2. Enable 2-Factor Authentication
3. Search for "App Passwords" in settings
4. Generate a new app password for "Mail"
5. Use the 16-character password in your .env file

### Alternative Email Providers

To use a different SMTP provider, modify the SMTP settings:

```python
# Outlook
with smtplib.SMTP_SSL("smtp-mail.outlook.com", 587, context=context) as smtp:

# Yahoo
with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465, context=context) as smtp:
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| FileNotFoundError | CSV file missing | Check file path |
| ValueError | Missing .env variables | Configure EMAIL_SENDER and GMAIL_PASSWORD |
| SMTPAuthenticationError | Invalid credentials | Use Gmail App Password |
| Invalid timezone | TZ invalid | Use valid IANA timezone (e.g., "America/New_York") |

## Scheduling the Script

### Using Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (daily at specific time)
4. Action: Start a program
5. Point to your Python script

### Using Cron (Mac/Linux)

```bash
# Run daily at 9 AM
0 9 * * * /path/to/venv/bin/python /path/to/birthay_gif_proyect.py
```

### Using Python Schedule

```python
import schedule
import time

def run_script():
    import birthay_gif_proyect

schedule.every().day.at("09:00").do(run_script)

while True:
    schedule.run_pending()
    time.sleep(60)
```

## Security Considerations

1. **Never commit .env file** to version control
2. Add `.env` to `.gitignore`
3. Use App Passwords, not regular passwords
4. Validate all CSV data before processing
5. Limit email sending rate to avoid spam filters

## .gitignore Entry

```
.env
```

## Customization

### Change Email Content

```python
msg.set_content(
    f"Hello {name},\n\n"
    f"Happy Birthday! 🎂\n\n"
    f"Wishing you an amazing day!\n\n"
    f"Best regards,\nYour Name\n"
)
```

### Add HTML Email

```python
msg.add_alternative("""\
<html>
  <body>
    <h1>Happy Birthday, {name}!</h1>
    <p>Wishing you a wonderful day!</p>
  </body>
</html>
""", subtype='html')
```

### Add CC/BCC

```python
msg["Cc"] = "other@example.com"
```

## Example Output

```
Using .env file: ...\birthays.csv
CSV_FILE resolved to: ...\birthays.csv
EMAIL_SENDER: your-email@gmail.com
GMAIL_PASSWORD length: 16
Sent to John Doe <john@example.com>
Sent to Jane Smith <jane@example.com>
```

Or if no birthdays:

```
Today there are no birthdays.
```

## Requirements

```
python-dotenv
```

Python 3.9+ for zoneinfo module (use `pytz` for older versions).

## License

(Just in case, this project is just for educational purposes, i don't know own anything of all this plus it's just a practice.)