# SudoR2spr WOODcraft
# Add your details here and then deploy

import os

API_ID    = int(os.environ.get("API_ID", "38498066"))
API_HASH  = os.environ.get("API_HASH", "c9696114751feacdeb1b4487f5839a1a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# ✅ Add this (IMPORTANT)
OWNER = int(os.environ.get("OWNER", "8703802029"))  # apna Telegram ID daal

# ✅ Fix webhook & port
WEBHOOK = bool(os.environ.get("WEBHOOK", False))
PORT = int(os.environ.get("PORT", 8080))
