import smtplib
import time
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# -----------------------------
# CONFIGURATION
# -----------------------------
YOUR_EMAIL = "username@gmail.com"
YOUR_PASSWORD = "xxxx xxxx xxxx xxxx"  # Replace with your Gmail App Password
SUBJECT = "Name – Application"

MESSAGE_FILE = r"path\msg.txt"
EMAIL_LIST_FILE = r"path\mails.txt"
ATTACHMENT_FILE = r"path\Name_Resume.pdf"

DELAY_SECONDS = 5

# -----------------------------
# LOAD EMAIL LIST
# -----------------------------
def load_emails(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# -----------------------------
# LOAD MESSAGE
# -----------------------------
def load_message(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# -----------------------------
# SEND EMAIL
# -----------------------------
def send_email(receiver, message):
    try:
        msg = MIMEMultipart()
        msg["From"] = YOUR_EMAIL
        msg["To"] = receiver
        msg["Subject"] = SUBJECT

        # Email body
        msg.attach(MIMEText(message, "plain", "utf-8"))

        # Attachment
        with open(ATTACHMENT_FILE, "rb") as f:
            attachment = MIMEApplication(f.read(), _subtype="pdf")
            attachment.add_header(
                "Content-Disposition",
                "attachment",
                filename=os.path.basename(ATTACHMENT_FILE)
            )
            msg.attach(attachment)

        # SMTP connection (auto-closes safely with 'with')
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.send_message(msg)

        print(f"[OK] Email sent to: {receiver}")

    except Exception as e:
        print(f"[FAIL] Failed to send to {receiver}: {e}")

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    emails = load_emails(EMAIL_LIST_FILE)
    message = load_message(MESSAGE_FILE)

    print(f"Total emails found: {len(emails)}")
    print(f"Starting safe mode ({DELAY_SECONDS} sec delay)...")

    for email in emails:
        send_email(email, message)
        time.sleep(DELAY_SECONDS)

    print("All emails processed.")
