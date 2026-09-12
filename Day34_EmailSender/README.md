# 📧 Day 34 - Email Sender

A Python program that sends an email to a specified recipient using SMTP (Simple Mail Transfer Protocol).

## 🎯 Objective

To create an Email Sender that automates sending emails directly from Python using SMTP servers.

## 🛠️ Concepts Used

- File Handling  
- Functions  
- Exception Handling  
- User Input  
- SMTP Protocol  
- EmailMessage Class

## 📚 Required Libraries

This project uses Python’s built‑in libraries:

- `smtplib`  
- `email.message`  

No external installations are required unless using Gmail (App Passwords recommended for security).

## ⚙️ How It Works

1. The user enters sender email, password (or app password), receiver email, subject, and body.  
2. An `EmailMessage` object is created with the provided details.  
3. The program connects to Gmail’s SMTP server (`smtp.gmail.com`, port 465).  
4. The sender logs in using credentials.  
5. The email is sent to the recipient.  
6. Success or error messages are displayed depending on the outcome.

## 💻 Example Output

```text
=== Email Sender ===
Enter your email: your.email@gmail.com
Enter your email password or app password: ************
Enter receiver email: friend@example.com
Enter subject: Hello from Python!
Enter email body: This is a test email sent using Python.
✅ Email sent successfully!
```

*If authentication fails, the program displays: ❌ Authentication failed. Check email or password.*

## 🧠 What I Learned

- Sending emails using Python’s `smtplib`  
- Creating structured email messages with `EmailMessage`  
- Handling authentication and SMTP errors  
- Automating communication tasks  
- Building a practical real‑world utility

## ▶️ How to Run

```bash
python main.py
```

Make sure you have internet access and valid email credentials.  
For Gmail, enable **App Passwords** for secure authentication.

## 📁 Project Structure

```text
Day34_EmailSender/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 34/50** — Learn • Build • Improve

