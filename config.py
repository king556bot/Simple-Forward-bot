# config.py
from os import environ

API_ID = int(environ.get("API_ID", "25049176"))
API_HASH = environ.get("API_HASH", "7729713683:AAGOEtndJw9_Ao0HE-7NlVcBHV9VLFy0lhM")
BOT_TOKEN = environ.get("BOT_TOKEN", "7616359279:AAGMB2Pct7rHQBuTvh6W3ris8SFvrMhNbAg")
MONGO_URI = environ.get("MONGO_URI", "")
OWNER_ID = int(environ.get("OWNER_ID", "7146651806"))
