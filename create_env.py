#!/usr/bin/env python3
"""
Script to create .env file with proper encoding
"""

env_content = """MAIL_USERNAME=onepercentage51@gmail.com
MAIL_PASSWORD=xyhu ogta jffu vxhp
SECRET_KEY=cybernaut-secret-key-2024
FLASK_APP=app.py
FLASK_ENV=development
"""

# Write .env file with UTF-8 encoding
with open('.env', 'w', encoding='utf-8') as f:
    f.write(env_content)

print("✅ .env file created successfully!")
print("📧 Mail Username: onepercentage51@gmail.com")
print("🔑 Mail Password: xyhu ogta jffu vxhp")
print("🔐 Secret Key: cybernaut-secret-key-2024")
print("\nYou can now test the email functionality!") 