import uvicorn
from fastapi import FastAPI, Request
from .bot import build_app

fastapi_app = FastAPI()
telegram_app = build_app()

@fastapi_app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    await telegram_app.initialize()
    await telegram_app.process_update(data)
    return {"ok": True}

if __name__ == "__main__":
    uvicorn.run("app.main:fastapi_app", host="0.0.0.0", port=10000)
