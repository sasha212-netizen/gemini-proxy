from fastapi import FastAPI, Request
import httpx
import uvicorn

app = FastAPI()
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=ТВОЙ_API_КЛЮЧ"

@app.post("/proxy")
async def proxy(request: Request):
    data = await request.json()
    async with httpx.AsyncClient() as client:
        # Пересылаем запрос в Google от имени сервера в США
        response = await client.post(GEMINI_URL, json=data)
        return response.json()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
