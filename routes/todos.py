from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from services.db import get_db_connection
from psycopg2.extras import DictCursor

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/delete/{todo_id}")
def delete_todo_item(request: Request, todo_id: str):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(f"""DELETE FROM todos WHERE id = '{todo_id}';""")
        conn.commit()
        
        cursor.execute("""SELECT id, item
                        from todos""")
        todos = cursor.fetchall()
    conn.close()
    
    context = {
        "request": request,
        "todos": todos
    }
    return templates.TemplateResponse("/todos/merged_todo.html", context)

@router.post("/")
async def add_todo_to_db(request: Request):
    params = await request.form()
    conn = get_db_connection()
    with conn.cursor() as cursor:
        pass
        cursor.execute(f"""INSERT INTO todos (item)
                        VALUES ('{params['item']}');""")
        conn.commit()
        cursor.execute("""SELECT id, item
                        from todos""")
        todos = cursor.fetchall()
    conn.close()

    context = {
        "request": request,
        "todos": todos
    }
    return templates.TemplateResponse("/todos/merged_todo.html", context)

# http://localhost:8000/todos/
@router.get("/{todo_id}")
async def get_todo(request: Request, todo_id: str):
    conn = get_db_connection()
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute(f"""SELECT id, item 
                        FROM todos 
                        WHERE id = '{todo_id}';""")
        todo = cursor.fetchone()
        
        cursor.execute("""SELECT id, item
                        from todos""")
        todos = cursor.fetchall()
    conn.close()
    
    context = {
        "request": request,
        "todo": todo,
        "todos": todos
    }
    return templates.TemplateResponse("/todos/merged_todo.html", context)

# http://localhost:8000/todos/
@router.get("/")
async def get_todos_html(request: Request):
    conn = get_db_connection()
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute("""SELECT id, item
                        from todos""")
        todos = cursor.fetchall()
    conn.close()
    
    context = {
        "request": request,
        "todos": todos
        }
    return templates.TemplateResponse("/todos/merged_todo.html", context)