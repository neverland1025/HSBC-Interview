from fastapi import FastAPI, WebSocket
from typing import List
import uvicorn

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    # Connect client
    await manager.connect(websocket)
    try:
        while True:
            # Wait for any message from the client
            data = await websocket.receive_text()
            message = f"{username}: {data}"
            # Broadcast message
            await manager.broadcast(message)
    except Exception as e:
        # Handle errors e.g., client disconnects
        print(f"Error: {e}")
    finally:
        # Disconnect client
        manager.disconnect(websocket)

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)