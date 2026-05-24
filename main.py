import os
from fastapi import FastAPI, Request
import httpx
import uvicorn

app = FastAPI()

# Берем ключ из настроек окружения на Рендере
API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={API_KEY}"

@app.post("/proxy")
async def proxy(request: Request):
    data = await request.json()
    async with httpx.AsyncClient() as client:
        # Пересылаем запрос в Google
        response = await client.post(GEMINI_URL, json=data)
        return response.json()

if __name__ == "__main__":
    # Используем порт, который выдает Рендер
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
