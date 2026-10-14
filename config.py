import os
from dotenv import load_dotenv

# Local computer par .env file load karega
load_dotenv()

BOT_TOKEN = os.getenv("8907760148:AAHZC9Pj-4CbbfiX9uCAVxWN6l7aFxrS_5I")

if not BOT_TOKEN:
    raise ValueError(
        "BOT_TOKEN nahi mila. Railway Variables mein BOT_TOKEN add karo."
    )
