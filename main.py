from fastapi import FastAPI
import threading
from bot import run_bot

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Бот работает и FastAPI тоже!"}

threading.Thread(target=run_bot).start()
