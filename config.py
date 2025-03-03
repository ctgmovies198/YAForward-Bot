# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "28148293")
    API_HASH = environ.get("API_HASH", "32ce81ffdd4684a856370eccf62b1f80")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7561827913').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://i.ibb.co.com/wDn9z1L/images-18.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://besuduso:0B4FAHGCcjxkj54m@cluster0.qhjtc.mongodb.net/?retryWrites=true&w=majority&appName=")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002381954054'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002393900827") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
