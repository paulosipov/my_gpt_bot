# bot.py  – минимальная версия: /start отвечает приветствием

import os
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler, ContextTypes, filters
)

TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    """Ответ на команду /start и любые текстовые сообщения."""
    await update.message.reply_text("Привет! Я живой на Render 🎉")


def build_app() -> Application:
    """Создаёт и возвращает объект Telegram‑приложения."""
    app = Application.builder().token(TOKEN).build()

    # /start
    app.add_handler(CommandHandler("start", start))
    # любое текстовое сообщение
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))

    return app
