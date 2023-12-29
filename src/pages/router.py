from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from src.operations.router import get_specific_operations

rounter = APIRouter(
    prefix="/pages",
    tags=["pages"]
)

templates = Jinja2Templates(directory="src/templates")


@rounter.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@rounter.get("/search/{operation_type}")
def get_base_page(request: Request, operations=Depends(get_specific_operations)):
    return templates.TemplateResponse("/search.html", {
        "request": request,
        "operations": operations["data"],
    })
