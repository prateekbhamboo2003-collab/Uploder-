#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27991871"))
API_HASH = environ.get("API_HASH", "8dda0c086a4bb6cd0f5a3b74b55fdee3")
BOT_TOKEN = environ.get("BOT_TOKEN", "7697319919:AAH2n7nirJAthAksLdSB5C-fg7dLz1sF7Ec")

OWNER = int(environ.get("OWNER", "7734031129"))
CREDIT = environ.get("CREDIT", "CutePie")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7734031129').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7734031129').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
