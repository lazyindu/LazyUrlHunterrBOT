# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/LazyUrlHunterrBOT'>Lazy Url Hunterr</a> is an open source project.

    Devs: 
        <a href='https://t.me/mRiderDM'>β€οΈ LazyDeveloper β€οΈ</a>
    
    
π€ My Name: <a href='https://t.me/Official_Movies_Group'>Mdisk Search Robot</a>

π Language: <a href='https://www.python.org'>Python V3</a>

π Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

π‘ Server: <a href='https://heroku.com'>Heroku</a>

π‘ Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

π¨βπ» Developer Channel: <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a></b>
"""

    ABOUT_HELP_TEXT = """<b>π Developer : <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {}π,

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

Β»Β»Β» <b>Happy Hunting</b> Β«Β«Β«

πΊThank You <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>πΊ </b>
"""


    START_MSG = """
<b>Hello Baby ! {}π,

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   Β»Β»Β»Β» <b>Happy Hunting</b> Β«Β«Β«Β«

πΈ<b>Donate us to Keep service Alive.πΈ</b>
Β»Β» A small amount of βΉ5 - βΉ20 - βΉ50 - βΉ100 will be great help !
πΊ Thank You πΊ 
"""

