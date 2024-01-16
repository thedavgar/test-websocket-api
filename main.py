import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.templating import Jinja2Templates

from src.connections import ConnectionManager
stop_task = asyncio.Event()



@asynccontextmanager
async def app_lifespan(app: FastAPI):
    task = asyncio.create_task(report_active_connections())
    yield
    stop_task.set()
    await task

async def report_active_connections():
    try:
        while not stop_task.is_set():
            info = manager.get_connections_info()
            print(f"Reporte actualizado: {info}")
            await asyncio.sleep(30)
    except Exception as e:
        # Manejo adecuado de excepciones
        print(f"Error en la tarea de reporte: {e}")


app = FastAPI(lifespan=app_lifespan)
templates = Jinja2Templates(directory="templates")
manager = ConnectionManager()



@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws/{group_id}/{client_id}")
async def websocket_endpoint(websocket: WebSocket, group_id: str, client_id: int):
    await manager.connect(group_id, websocket)
    try: 
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}", group_id)
    except WebSocketDisconnect:
        manager.disconnect(group_id, websocket)
        await manager.broadcast(f"Client #{client_id} has left the group {group_id}", group_id)
