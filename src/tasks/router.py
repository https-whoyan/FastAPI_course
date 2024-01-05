from fastapi import APIRouter, Depends, BackgroundTasks
from src.auth.base_config import current_user
from src.tasks.tasks import send_email_report_dashboard
from src.auth.models import User

router = APIRouter(
    prefix="/report",
    tags=['report']
)


# Add BackGroud Task
@router.get("/dashboard")
def get_dashboard_report(background_taks: BackgroundTasks, user: User = Depends(current_user)):
    background_taks.add_task(send_email_report_dashboard, user.username, user.email)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None,
    }
