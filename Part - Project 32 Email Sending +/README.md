# Email Sending Application

## Project Overview
A Python application that sends automated emails using SMTP protocol with Gmail integration. This project demonstrates email automation with secure credential handling.

## Technologies Used
- Python 3.x
- smtplib (email sending)
- email.message (email composition)
- dotenv (environment variable management)
- SSL/TLS encryption

## Project Structure
```
Part - Project 32 Email Sending +/
├── main.py              # Main email sending script
├── .env                 # Environment variables (not in repo)
├── quotes.txt           # Collection of quotes for email content
├── time.py             # Time-related utilities
└── README.md           # This file
```

## Features
- Secure email sending via Gmail SMTP
- Environment variable based credential management
- Email message composition with headers and body
- SSL/TLS encryption for secure transmission
- Configurable sender/recipient addresses

## Prerequisites
1. Gmail account with 2-factor authentication enabled
2. App password generated from Google Account settings
3. Python 3.x installed

## Setup Instructions
1. Create a `.env` file in the project root:
   ```
   GMAIL_PASSWORD=your_gmail_app_password
   ```
2. Install required dependencies:
   ```
   pip install python-dotenv
   ```

## How to Run
1. Update the email addresses in `main.py`:
   ```python
   email_sender = "your_email@gmail.com"
   email_reciver = "recipient_email@gmail.com"
   ```
2. Run the script:
   ```
   python main.py
   ```

## Email Configuration
The application uses the following email settings:
- SMTP Server: `smtp.gmail.com`
- Port: 465 (SSL)
- Security: SSL/TLS encryption
- Authentication: App password based

## Customization
1. **Email Content**: Modify the `subject` and `body` variables in `main.py`
2. **Dynamic Content**: Load quotes from `quotes.txt` for automated content
3. **Multiple Recipients**: Modify the code to support multiple recipients
4. **HTML Email**: Extend to send HTML formatted emails

## Security Notes
⚠️ **IMPORTANT SECURITY PRACTICES:**
- Never commit `.env` files to version control
- Use app passwords instead of regular passwords
- Store sensitive credentials in environment variables
- Regularly rotate app passwords

## Error Handling
The application includes error handling for:
- Missing environment variables
- Network connectivity issues
- Invalid email addresses
- Authentication failures

## Project Purpose
This project demonstrates:
- Secure email automation in Python
- Environment variable management best practices
- SMTP protocol implementation
- Professional email composition techniques