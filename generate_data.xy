import random

phishing_samples = [
    "Verify your account at http://fakebank.com",
    "Urgent login attempt detected http://192.168.1.1",
    "Reset your password immediately",
    "Click here to claim prize http://scam.xyz"
]

safe_samples = [
    "Meeting at 3pm tomorrow",
    "Project deadline extended",
    "Lunch with team today",
    "Monthly report attached"
]

with open("data/emails.csv", "w") as f:
    f.write("text\n")
    
    for _ in range(10000):
        if random.random() > 0.5:
            f.write(random.choice(phishing_samples) + "\n")
        else:
            f.write(random.choice(safe_samples) + "\n")

print("Dataset generated: 10,000 emails")
