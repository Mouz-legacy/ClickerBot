import os


BOT_TOKEN = os.getenv("BOT_TOKEN", "1974470706:AAEA5cPdLBqtYng_uEbZDmi2E8ADj2J_rCw")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://f6ae-178-122-208-31.ngrok.io")
URL_WEB = os.getenv("URL_WEB", "https://cf45-178-122-208-31.ngrok.io")
TELEGRAM_URL = "https://api.telegram.org"
DATA = {"url": WEBHOOK_URL}
SET_WEBHOOK_URL = f"{TELEGRAM_URL}/bot{BOT_TOKEN}/setWebhook"
BOT_URL = f"{TELEGRAM_URL}/bot{BOT_TOKEN}/"
