from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler, ContextTypes, filters
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я GPT‑бот. Напиши вопрос — отвечу 😊")

def build_app() -> Application:
    return (
        Application.builder()
        .token(context.bot_data["TELEGRAM_TOKEN"])   # мы передадим переменную в main.py
        .build()
        .add_handler(CommandHandler("start", start))
        .add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))
    )
