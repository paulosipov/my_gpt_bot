from fastapi import FastAPI
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Инициализация FastAPI
app = FastAPI()

# Установим ключ API для OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Создание Telegram-приложения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot_app = Application.builder().token(TELEGRAM_TOKEN).build()

# Функция ответа через ChatGPT
async def ask_openai(question: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # или "gpt-4", если у тебя есть доступ
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Ошибка: {str(e)}"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я GPT-бот. Напиши мне что-нибудь, и я отвечу.")

# Ответ на текстовые сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    reply = await ask_openai(user_input)
    await update.message.reply_text(reply)

# Роут для проверки состояния сервера
@app.get("/")
def read_root():
    return {"status": "бот работает"}

# Запуск Telegram-бота асинхронно
@app.on_event("startup")
async def startup_event():
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    bot_app.run_polling()

