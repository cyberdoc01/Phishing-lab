
# Phishing Detection Lab

## Overview
This project is a Python-based phishing detection system designed to analyze real email data from Gmail using IMAP. It scans incoming messages, extracts relevant indicators, and identifies potentially malicious emails based on predefined security rules.

The goal of this lab is to simulate a real-world email security workflow and demonstrate practical cybersecurity skills in email threat detection.

---

## Features
- Connects to Gmail using IMAP protocol
- Fetches and processes real email messages
- Extracts:
  - Sender information
  - Subject lines
  - Email body content
  - Embedded links
nano README.md- Detects phishing indicators such as:
  - Suspicious keywords (e.g., "verify", "urgent", "login")
  - Potentially malicious URLs
- Generates:
  - Structured CSV output for analysis
  - Clean, readable report for review

---

## Technologies Used
- Python 3
- IMAP (email retrieval)
- Pandas (data processing)
- Regular Expressions (pattern detection)

---

## Project Structure


---

## How It Works
1. The script connects to a Gmail account via IMAP.
2. It retrieves a specified number of recent emails.
3. Each email is parsed and analyzed.
4. Phishing indicators are detected using rule-based logic.
5. Results are saved for further analysis.

---

## Sample Output



---

## Use Case
This project demonstrates:
- Email security analysis
- Threat detection logic
- Data parsing and automation
- Practical cybersecurity workflow

---

## Disclaimer
This project is for educational and ethical cybersecurity purposes only. It should not be used for unauthorized access or malicious activities.

---

## Author
Cybersecurity Enthusiast | Python Developer | Email Security Analyst
