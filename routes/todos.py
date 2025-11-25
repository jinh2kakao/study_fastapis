from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

# http://localhost:8000/todos/
@router.get("/")
async def get_todos_html(request: Request):
    context = {
        "request": request
        }
    # todos = [
    #     {"id": 1, "task": "Buy groceries", "completed": False},
    #     {"id": 2, "task": "Read a book", "completed": True},
    #     {"id": 3, "task": "Write code", "completed": False}
    # ]
    return templates.TemplateResponse("/todos/merged_todo.html", context)