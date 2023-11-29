from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.exc import DBAPIError, IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.operations.models import operation
from src.operations.schema import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            "status": 200,
            "data": result.mappings().all(),
            "details": None,
        }
    except Exception:
        return HTTPException(status_code=500, detail={
            "status": "error",
            "data": "Произошла ошибка при получении данных об финансовых операциях",
            "details": None,
        })


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(operation).values(**new_operation.model_dump())
        await session.execute(stmt)
        await session.commit()
        return {
            "status": 200,
            "data": None,
            "details": "Добавление данных произошло успешно!",
        }
    except DBAPIError as e:
        if e.__class__ == IntegrityError:
            return HTTPException(status_code=500, detail={
                "status": "error",
                "data": None,
                "details": "Ты добавляешь айдишник, который уже есть в БД!",
            })
        return HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": "БД жалуется на данные!",
        })
    except Exception as e:
        return HTTPException(status_code=500, detail={
            "status": "error",
            "data": "Произошла ошибка при добавлении финансой операции",
            "details": None,
        })
