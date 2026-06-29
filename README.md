# 📧 Automated Job Application Email Sender

A Python-based email automation tool that sends personalized job application emails with resume attachments to multiple recipients. The application reads email addresses and message content from external text files, attaches a PDF resume, and sends emails sequentially through Gmail SMTP with configurable delays to reduce the likelihood of triggering spam filters.

---

## 📌 Overview

As a job seeker, I found that applying to multiple companies often meant repeatedly sending the same email with my resume attached to different recruiters and hiring managers. While the recipient changes, the process itself is repetitive and time-consuming.

I built this project to simplify that workflow for myself and a few friends by automating the repetitive parts of the application process. The tool reads a list of recipient email addresses, loads a predefined email template, attaches a resume, and sends emails sequentially with a configurable delay using Gmail SMTP.

The goal of this project is not bulk marketing or spam, but to automate a common, legitimate task while learning practical concepts such as SMTP communication, secure authentication, file handling, and workflow automation in Python.
---

## 🚀 Features

* 📨 Send emails to multiple recipients
* 📄 Attach a PDF resume automatically
* 📝 Load email content from an external text file
* 📋 Read recipient email addresses from a text file
* ⏱️ Configurable delay between emails
* 🔒 Secure Gmail SMTP authentication using App Passwords
* ✅ Success and failure logging for every email
* 🛠️ Simple configuration through constants

---

## 🛠️ Technologies Used

* Python
* smtplib
* email.mime
* os
* time

---

## 📂 Project Structure

```text
Automated-Job-Application-Email-Sender/
│
├── email_sender.py
├── msg.txt
├── mails.txt
├── Resume.pdf
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuration

Update the following configuration values before running the application:

```python
YOUR_EMAIL = "your_email@gmail.com"
YOUR_PASSWORD = "your_gmail_app_password"
SUBJECT = "Your Name – Application"

MESSAGE_FILE = "msg.txt"
EMAIL_LIST_FILE = "mails.txt"
ATTACHMENT_FILE = "Resume.pdf"

DELAY_SECONDS = 5
```

---

## 📄 Input Files

### `mails.txt`

Contains one email address per line.

Example:

```text
hr1@company.com
hr2@company.com
careers@company.com
```

---

### `msg.txt`

Contains the email body.

Example:

```text
Dear Hiring Manager,

I hope you are doing well.

Please find my resume attached for your consideration.

Thank you for your time.

Best regards,
Your Name
```

---

## 🔄 Project Workflow

### 1. Load Email Addresses

The application reads all recipient email addresses from `mails.txt`.

---

### 2. Load Email Template

The email body is loaded from `msg.txt`.

---

### 3. Create Email

For each recipient, the application:

* Creates a multipart email
* Adds the email body
* Attaches the resume PDF
* Sets the sender, recipient, and subject

---

### 4. Connect to Gmail SMTP

The application securely connects to Gmail's SMTP server using TLS encryption and authenticates with your Gmail App Password.

---

### 5. Send Emails

Emails are sent one at a time with a configurable delay between each message.

Console output indicates whether each email was sent successfully or failed.

---

## ▶️ Running the Project

Install Python if it is not already installed.

Run the script:

```bash
python email_sender.py
```

Example output:

```text
Total emails found: 20
Starting safe mode (5 sec delay)...

[OK] Email sent to: hr1@company.com
[OK] Email sent to: hr2@company.com
[FAIL] Failed to send to: invalid@email.com

All emails processed.
```

---

## 📦 Requirements

This project uses only Python's standard library.

No third-party packages are required.

Python 3.8 or later is recommended.

---

## 🔒 Gmail Setup

To use Gmail SMTP:

1. Enable Two-Step Verification on your Google account.
2. Generate a Gmail App Password.
3. Replace the `YOUR_PASSWORD` value with the generated App Password.
4. Use your Gmail address as `YOUR_EMAIL`.

> Never use your regular Gmail password in the source code.

---

## 📚 Learning Outcomes

Through this project, I explored:

* SMTP email automation
* Secure email authentication
* Working with MIME email messages
* File handling in Python
* Exception handling
* Sending email attachments
* Automating repetitive workflows

---

## 🔮 Future Improvements

* Support HTML email templates
* Personalize emails with recipient names
* Add CC and BCC support
* Support multiple attachments
* Read recipient data from CSV or Excel files
* Retry failed email deliveries
* Generate detailed email delivery reports
* Build a desktop GUI using Tkinter or PyQt

---

## ⚠️ Disclaimer

This project is intended for legitimate email automation purposes, such as sending job applications or professional communications. Users are responsible for complying with email provider policies and applicable laws. Avoid sending unsolicited or spam emails.

---

## 🎓 About This Project

This is a personal project that I built to automate a repetitive task I frequently encountered while applying for software engineering roles. Instead of manually composing the same email and attaching my resume for every application, this tool streamlines the process by reading recipient details from a file and sending emails automatically with a configurable delay.

Beyond solving a real-world problem, the project helped me gain hands-on experience with Python's SMTP library, MIME email handling, file processing, exception handling, and automation. It also proved useful to friends who were going through similar job application processes.
