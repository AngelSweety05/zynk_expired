import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7588025019:AAFD6eBXhqaLMS2eSXMH-uDecbv_0n2worI")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23265307"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cc2b82ee80cabeba9a3408a6972d0ab2")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002337928239"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "admiinn101")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7245587256"))

#Port
PORT = os.environ.get("PORT", "8030")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://adonee777:adonee777@cluster0.bqbic.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002452174007"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002255055538"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "5"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds

HOW_TO_DOWNLOAD_LINK = os.environ.get('HOW_TO_DOWNLOAD_LINK', "https://t.me/How_to_watch_gurujiurl/3")
#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first},!\n\nI’m your File Store Bot, here to safely store and manage your private files. Upload them to the specified channel, and share them with others using a unique link. Let’s keep your files organized and accessible!</b>")
try:
    ADMINS=[5965340120]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>👋 Hello, {first}!\n\nYou need to join in my Channel/Group to use me\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 ᴏʜ ɴᴏ! ᴡʜᴇʀᴇ'ʀᴇ ʏᴏᴜʀ ʜᴀɴᴅs?!"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

# IS_LAZYUSER_VERIFICATION = is_enabled((environ.get("IS_LAZYUSER_VERIFICATION","True")), False) # make it true to enable url shortner in groups or pm
TOKEN_VERIFICATION = True if os.environ.get('TOKEN_VERIFICATION', "False") == "True" else False
LAZY_SHORTNER_URL = os.environ.get('LAZY_SHORTNER_URL', 'gurujiurl.com')
LAZY_SHORTNER_API = os.environ.get('LAZY_SHORTNER_API', 'de6ec2c9eee42e35075d440e63aee0e660bd12cf') #Always use website url from api section 
# LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', 0))

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
