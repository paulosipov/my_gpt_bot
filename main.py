import os
import uvicorn
from fastapi import FastAPI, Request
from bot import build_app          # ← обратите внимание: без .app

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

fastapi_app = FastAPI()
telegram_app = build_app()
telegram_app.bot_data["TELEGRAM_TOKEN"] = TELEGRAM_TOKEN   # передаём токен

@fastapi_app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    await telegram_app.initialize()
    await telegram_app.process_update(data)
    return {"ok": True}

if __name__ == "__main__":
    uvicorn.run("main:fastapi_app", host="0.0.0.0", port=10000)
