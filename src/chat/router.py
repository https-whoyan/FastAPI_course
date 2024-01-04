from typing import List

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.chat.manager import ConnectionManager
from src.database import get_async_session
from src.chat.models import messages
from sqlalchemy import select
from src.chat.utils import validate_to_dict



router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)


manager = ConnectionManager()


@router.get(path="/get_last_messages")
async def get_last_messages(
        session: AsyncSession = Depends(get_async_session),
):
    query = select(messages).order_by(messages.c.id.desc()).limit(5)
    query_messages = await session.execute(query)
    all_messages_sql = query_messages.all()
    all_message_json = [validate_to_dict(sqlMessage) for sqlMessage in all_messages_sql]
    return all_message_json


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Чат с ID #{client_id} сказал: {data}", add_to_database=True)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Час с ID = #{client_id} покинул чат", add_to_database=False)
