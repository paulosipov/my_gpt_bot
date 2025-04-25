import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, мир!")

def run_bot():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise Exception("TELEGRAM_TOKEN не найден в .env")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    logging.info("Бот запущен...")
    app.run_polling()
