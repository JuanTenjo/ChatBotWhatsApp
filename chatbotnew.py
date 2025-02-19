from fastapi import FastAPI, HTTPException, Request
import requests
import os

app = FastAPI()

# Configuración de credenciales de WhatsApp Cloud API
ACCESS_TOKEN = "82das23dsj323j8"
WHATSAPP_API_URL = "https://graph.facebook.com/v18.0/3006012318/messages"

# Enviar mensaje a un número específico
def send_whatsapp_message(number: str, text: str):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {"body": text}
    }
    response = requests.post(WHATSAPP_API_URL, json=payload, headers=headers)
    return response.json()

# Endpoint para recibir mensajes de WhatsApp
@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    try:
        body = await request.json()
        message = body.get("entry", [{}])[0].get("changes", [{}])[0].get("value", {}).get("messages", [{}])[0]
        
        if message:
            number = message.get("from")
            text = message.get("text", {}).get("body", "")
            reply_text = f"Recibí tu mensaje: {text}"
            send_whatsapp_message(number, reply_text)
        
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint de verificación de Meta
@app.get("/webhook")
def verify_token(hub_mode: str, hub_challenge: str, hub_verify_token: str):
    VERIFY_TOKEN = "TU_VERIFY_TOKEN"
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)
    return HTTPException(status_code=403, detail="Invalid token")

# Endpoint para enviar mensaje manualmente
@app.post("/send")
def send_message(number: str, text: str):
    response = send_whatsapp_message(number, text)
    return response
