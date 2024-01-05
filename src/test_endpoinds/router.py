from fastapi import APIRouter, Depends
from src.auth.models import User
from src.auth.base_config import current_user

# Add router
router = APIRouter(
    prefix='/test_protected_routers',
    tags=['test_protected_routers']
)


# Logic proctected endpoint use Depends
@router.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


# Logic free
@router.get("/unprotected-route")
def unprotected_route():
    return f"ZXC"
