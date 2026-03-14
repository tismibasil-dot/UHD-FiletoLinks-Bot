# 🗿  Visit & Support us - @UHD_NETWORK
# ⚡️ Do Not Remove Credit - Made by @UHDBots
# 💬 For Any Help Join Support Group: @UHDBots_Support
# 🚫 Removing or Modifying these Lines will Cause the bot to Stop Working.


import re
from os import environ


id_pattern = re.compile(r'^-?\d+$')


SESSION = environ.get("SESSION", "UHDFiletoLinksBot")
API_ID = int(environ.get("API_ID", "39498514"))
API_HASH = environ.get("API_HASH", "92db71e8f0b39dac859b7ee1c41edecd")
BOT_TOKEN = environ.get("BOT_TOKEN", "8524536924:AAGq1Xknx9bGwc4wKZZ85F4tmEscHptEoc4")


PORT = int(environ.get("PORT", "8080"))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
ON_HEROKU = "DYNO" in environ
URL = environ.get("URL", "")


LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "0"))
ADMINS = [
    int(admin) if id_pattern.match(admin) else admin
    for admin in environ.get("ADMINS", "").split()
]


DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://<db_username>:<db_password>@cluster0.gkrporp.mongodb.net/?appName=Cluster0")
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
