#!/usr/bin/env python3
# analyzer.py
# -----------------------------
# Phishing Email Analyzer v1.0
# -----------------------------

import imaplib
import email
from email.header import decode_header
from datetime import datetime
import pandas as pd
import os
import re

# -----------------------------
# CONFIGURATION
# -----------------------------
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "wiseworld247@gmail.com"
EMAIL_PASSWORD = "lbgfdvwoiiusshhg"  # Use Gmail App Password

MAILBOX = "INBOX"
NUM_EMAILS = 20  # Number of recent emails to fetch
RESULTS_DIR = "results"
PHISHING_KEYWORDS = [
    "verify", "account", "password", "click", "login", "urgent",
    "suspend", "bank", "credit", "confirm"
]

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def clean_text(text):
    """Clean text for CSV export."""
    return re.sub(r'\s+', ' ', text).strip()

def extract_links(body):
    """Extract all URLs from email body."""
    return re.findall(r'https?://[^\s]+', body)

def check_phishing(subject, body):
    """Check if email contains phishing keywords."""
    text = f"{subject} {body}".lower()
    matches = [kw for kw in PHISHING_KEYWORDS if kw in text]
    return matches if matches else None

# -----------------------------
# MAIN SCRIPT
# -----------------------------
def main():
    start_time = datetime.now()
    print(f"[INFO] Starting analysis at {start_time}")

    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    # Connect to Gmail
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
    mail.select(MAILBOX)

    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()
    email_ids = email_ids[-NUM_EMAILS:]  # Get last NUM_EMAILS emails

    results = []

    for eid in email_ids:
        res, msg_data = mail.fetch(eid, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                # Decode email subject
                subject, encoding = decode_header(msg.get("Subject"))[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8", errors="ignore")
                subject = clean_text(subject)

                # Get sender
                from_ = msg.get("From")
                from_ = clean_text(from_)

                # Get body
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            try:
                                body = part.get_payload(decode=True).decode()
                                break
                            except:
                                continue
                else:
                    body = msg.get_payload(decode=True).decode(errors="ignore")
                body = clean_text(body)

                # Extract links
                links = extract_links(body)

                # Check phishing
                phishing_matches = check_phishing(subject, body)

                results.append({
                    "From": from_,
                    "Subject": subject,
                    "Body": body,
                    "Links": ", ".join(links),
                    "Phishing Indicators": ", ".join(phishing_matches) if phishing_matches else ""
                })

    # Save results
    df = pd.DataFrame(results)
    output_file = os.path.join(RESULTS_DIR, "output.csv")
    df.to_csv(output_file, index=False)
    print(f"[INFO] Analysis complete! Results saved to {output_file}")

    end_time = datetime.now()
    print(f"[INFO] Finished at {end_time} | Duration: {end_time - start_time}")

if __name__ == "__main__":
    main()
