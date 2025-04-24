import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция обработки команды start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет, мир!')

def main():
    # Вставь сюда свой API-токен
    # Замените 'YOUR_API_TOKEN' на настоящий токен вашего бота
    updater = Updater("7576203575:AAEp6cuj1K2RqMb1Fp7z0TC86mWxP3R5LjQ", use_context=True)

    # Получаем диспатчер для обработки сообщений
    dp = updater.dispatcher

    # Обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()

    # Бот будет работать до тех пор, пока не будет прерван
    updater.idle()

if __name__ == '__main__':
    main()
