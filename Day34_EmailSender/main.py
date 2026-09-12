import smtplib
from email.message import EmailMessage

def send_email(sender_email, sender_password, receiver_email, subject, body):
    try:
        # Create email message
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.set_content(body)

        # Connect to SMTP server (Gmail SMTP used here)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

        print("\n✅ Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed. Check email or password.")
    except smtplib.SMTPException as e:
        print(f"❌ SMTP Error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("\n=== Email Sender ===\n")
    sender_email = input("Enter your email: ").strip()
    sender_password = input("Enter your email password or app password: ").strip()
    receiver_email = input("Enter receiver email: ").strip()
    subject = input("Enter subject: ").strip()
    body = input("Enter email body: ").strip()
    send_email(sender_email, sender_password, receiver_email, subject, body)
