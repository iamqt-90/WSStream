"""
WSStream Backend Main Application
"""
import asyncio
import json
import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import uvicorn
from groq import Groq
from uuid import uuid4

from config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="WSStream", version="1.0.0")

# Initialize Groq client
groq_client = Groq(api_key=settings.groq_api_key)

# Store active connections
active_connections = {}

@app.get("/")
async def get_index():
    """Serve the main frontend page"""
    try:
        with open("../frontend/index.html") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        with open("frontend/index.html") as f:
            return HTMLResponse(content=f.read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Main WebSocket endpoint"""
    await websocket.accept()
    session_id = str(uuid4())
    active_connections[session_id] = websocket
    
    logger.info(f"Client {session_id} connected")
    
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            if message_data.get("type") == "message":
                content = message_data.get("content", "")
                logger.info(f"Received message: {content}")
                
                # Send acknowledgment
                await websocket.send_text(json.dumps({
                    "type": "received",
                    "message_id": session_id
                }))
                
                # Process with Groq
                try:
                    response = groq_client.chat.completions.create(
                        model=settings.model_name,
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant. Keep responses concise and friendly."},
                            {"role": "user", "content": content}
                        ],
                        max_tokens=1000,
                        temperature=0.7
                    )
                    
                    bot_response = response.choices[0].message.content
                    
                    # Send processed response
                    await websocket.send_text(json.dumps({
                        "type": "response",
                        "message_id": session_id,
                        "content": bot_response
                    }))
                    
                except Exception as e:
                    logger.error(f"Error processing message: {e}")
                    await websocket.send_text(json.dumps({
                        "type": "error",
                        "message": f"Error processing message: {str(e)}"
                    }))
                    
    except WebSocketDisconnect:
        if session_id in active_connections:
            del active_connections[session_id]
        logger.info(f"Client {session_id} disconnected")

if __name__ == "__main__":
    logger.info("🚀 Starting WSStream Backend...")
    logger.info(f"📱 Open http://localhost:{settings.port} in your browser")
    uvicorn.run(app, host=settings.host, port=settings.port)