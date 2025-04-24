from telegram.ext import Application, CommandHandler

# Функция, которая будет вызываться при команде /start
def start(update, context):
    update.message.reply_text("Привет! Я твой бот!")

# Основная функция для настройки бота
def main():
    # Инициализация приложения с токеном
    application = Application.builder().token("7576203575:AAEp6cuj1K2RqMb1Fp7z0TC86mWxP3R5LjQ").build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

# Проверка, что скрипт запускается напрямую
if __name__ == "__main__":
    main()
