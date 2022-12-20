import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", "15352099"))
API_HASH = os.getenv("API_HASH", "a5fddd08a3d1375fef2eef6d3e8a8186")
SESSION = os.getenv("SESSION"‚ "AQCufBi6WZQVhznPt4k60AwqIgPoWAOQpxD_XOwrnHLE_GCfFyItAnpFs2XuxRY4YCwgmHlBv_NhXQvf0mYv4iKs9rXedFYjsv2Uz0SVk4OMHzFNumIUU5IDbNjsZ1jW3Fi4ZM40wq06AZJC7zqGA2s3zZycHtFJ5Ywn-3w0WJi_xzWgOCx8XQRcXn953u-pGeNdztCiSmM5kEzNpl5Cxp14nO9iFBBP9fiptTLyTv3QxWzsST9g4DNJ5oQ8xYAyMiUNyoKoVDSjcyGoF7dgjoFq-QBrvWIlGOymd9IPds9t1H309_zWtO4swfl3AT-NEiizBXz4NMI9LP_ofB0eZbr-AAAAATZe0mAA")
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="plugins"))
call_py = PyTgCalls(bot)
