#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "32376938"))
API_HASH = environ.get("API_HASH", "19b476b60eac5933ab6d27f0f61123b2")
BOT_TOKEN = environ.get("BOT_TOKEN", "8447929222:AAFKWbbiTwKU1RU1oR3SPKKFZ8rsTiOkUvk")

OWNER = int(environ.get("OWNER", "2128328460"))
CREDIT = environ.get("CREDIT", "Prateek")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7734031129').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '2128328460').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

