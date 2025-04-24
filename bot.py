import os
import uvicorn
from fastapi import FastAPI

# Создание экземпляра приложения FastAPI
fastapi_app = FastAPI()

@fastapi_app.get("/")
async def read_root():
    return {"message": "Hello World"}

# Получение порта из переменной окружения или установка по умолчанию
port = int(os.getenv("PORT", 10000))  # Если переменная окружения PORT не найдена, то используем 10000

if __name__ == "__main__":
    print("🤖 Bot is starting...")
    # Запуск приложения FastAPI с указанным портом и хостом
    uvicorn.run(fastapi_app, host="0.0.0.0", port=port)
