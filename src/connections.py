from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, list[WebSocket]] = {}

    async def connect(self, group_id: str, websocket: WebSocket):
        await websocket.accept()
        if group_id not in self.active_connections:
            self.active_connections[group_id] = []
        self.active_connections[group_id].append(websocket)

    def disconnect(self, group_id: str, websocket: WebSocket):
        self.active_connections[group_id].remove(websocket)
        if not self.active_connections[group_id]:
            del self.active_connections[group_id]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def broadcast(self, message: str, group_id: str):
        for connection in self.active_connections[group_id]:
            await connection.send_text(message)

    def get_connections_info(self):
        info = {}
        for group_id, connections in self.active_connections.items():
            # Aquí asumimos que solo queremos el conteo de conexiones por grupo
            info[group_id] = len(connections)
        return info