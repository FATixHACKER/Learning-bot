import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("8907760148:AAHZC9Pj-4CbbfiX9uCAVxWN6l7aFxrS_5I")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN نہیں ملا۔ .env فائل چیک کریں۔")