import re
from os import environ

# Bot Session Name
SESSION = environ.get('SESSION', 'TechVJBot')

# Your Telegram Account Api Id And Api Hash
API_ID = int(environ.get('API_ID', '25227969'))
API_HASH = environ.get('API_HASH', 'd59f6e3de4671401515bd1d8e303329f')

# Bot Token, This Is Main Bot
BOT_TOKEN = environ.get('BOT_TOKEN', "7691749001:AAFEDr-IN7H5mGqePlPRQtih2ufAW6G1MqY")

# Admin Telegram Account Id For Withdraw Notification Or Anything Else
ADMIN = int(environ.get('ADMIN', '6387781595'))

# Back Up Bot Token For Fetching Message When Floodwait Comes
BACKUP_BOT_TOKEN = environ.get('BACKUP_BOT_TOKEN', "7894735775:AAGMxFg5_fWasTrtAtw4bO4VrF30I-XZXm8")

# Log Channel, In This Channel Your All File Stored.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002257450133'))

# Mongodb Database For User Link Click Count Etc Data Store.
MONGODB_URI = environ.get("MONGODB_URI", "mongodb+srv://mihaja5084:yeIh95RrMkRNZ3It@cluster0.6voc3fm.mongodb.net/?retryWrites=true&w=majority")

# Stream Url Means Your Deploy Server App Url, Here You Media Will Be Stream And Ads Will Be Shown.
STREAM_URL = environ.get("STREAM_URL", "https://videoplayerbh-081337d07f95.herokuapp.com/")

# This Link Used As Permanent Link That If Your Deploy App Deleted Then You Change Stream Url, So This Link Will Redirect To Stream Url.
LINK_URL = environ.get("LINK_URL", "https://techvjyt.blogspot.com/2024/08/techvj.html")

# Others, Not Usefull
PORT = environ.get("PORT", "8080")
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
