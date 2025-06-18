#!/usr/bin/env python3
"""
Test script to verify email functionality
Run this script to test if the email configuration is working correctly.
"""

import os
from dotenv import load_dotenv
from flask import Flask
from flask_mail import Mail, Message

# Load environment variables
load_dotenv()

# Create a minimal Flask app for testing
app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'onepercentage51@gmail.com')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME', 'onepercentage51@gmail.com')

mail = Mail(app)

def test_email():
    """Test email functionality"""
    try:
        with app.app_context():
            # Create a test email
            msg = Message(
                subject="Test Email from One Percentage Website",
                recipients=['onepercentageedu@gmail.com'],
                body="""
This is a test email from the One Percentage website contact form.

Test Details:
- Name: Test User
- Email: test@example.com
- Subject: Test Message
- Message: This is a test message to verify email functionality.

---
This email was sent from the contact form on the One Percentage website.
                """
            )
            
            # Send the email
            mail.send(msg)
            print("✅ Email sent successfully!")
            print("📧 Check your inbox at onepercentageedu@gmail.com")
            
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure you have set up the .env file with MAIL_USERNAME and MAIL_PASSWORD")
        print("2. Verify that MAIL_PASSWORD is a valid Gmail app password")
        print("3. Ensure 2-Step Verification is enabled on your Gmail account")
        print("4. Check that the app password is generated for 'Mail'")

if __name__ == "__main__":
    print("🧪 Testing Email Functionality...")
    print("=" * 50)
    
    # Check environment variables
    mail_username = os.getenv('MAIL_USERNAME')
    mail_password = os.getenv('MAIL_PASSWORD')
    
    print(f"📧 Mail Username: {mail_username}")
    print(f"🔑 Mail Password: {'*' * len(mail_password) if mail_password else 'NOT SET'}")
    
    if not mail_password:
        print("\n⚠️  Warning: MAIL_PASSWORD not set in .env file")
        print("Please create a .env file with your Gmail app password")
    
    print("\n" + "=" * 50)
    test_email() 