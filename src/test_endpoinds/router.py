from fastapi import APIRouter, Depends
from src.auth.models import User
from src.auth.base_config import current_user

router = APIRouter(
    prefix='/test_protected_routers',
    tags=['test_protected_routers']
)


@router.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@router.get("/unprotected-route")
def unprotected_route():
    return f"ZXC"
