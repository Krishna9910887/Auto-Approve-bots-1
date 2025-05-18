from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "24828197"))
    API_HASH = getenv("API_HASH", "d36e278e89ebeb900aeda4128d413a77")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "SECRECT_BOT_UPDATES")
    CHID = int(getenv("CHID", "-1000112234"))
    SUDO = list(map(int, getenv("SUDO","7660990923").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
