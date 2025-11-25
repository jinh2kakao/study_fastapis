from fastapi import FastAPI
from fastapi import Request

# 1. FastAPI 인스턴스 생성
# 'app'은 전체 웹 애플리케이션을 관리하는 객체입니다.
app = FastAPI()

# roudtes 폴더의 todos.py 모듈에서 정의한 라우터를 임포트
from routes.todos import router as todos_router
app.include_router(todos_router, prefix="/todos")

# ==========================================
# Case 1: 기본 JSON 응답 (API 서버의 기본 동작)
# ==========================================
# @app.get("/") : HTTP GET 요청이 루트 경로("/")로 들어오면 아래 함수를 실행합니다.
@app.get("/")

# http://localhost:8000/
async def root():
    # 딕셔너리(dict)를 리턴하면 FastAPI가 자동으로 JSON으로 변환하여 응답합니다.
    # Content-Type: application/json
    return {"message": "Hello, World!"}

# ==========================================
# Case 2: HTML 문자열 직접 반환 (HTMLResponse)
# ==========================================
# response_class=HTMLResponse :
# 이 설정이 없으면 문자열이 그냥 텍스트(text/plain)나 JSON 문자열로 취급됩니다.
# 이 설정 덕분에 브라우저가 "아, 이건 HTML이구나"라고 인식하고 화면을 그립니다.
# http://localhost:8000/html
@app.get("/html")
async def root_html():
    # HTML 코드를 문자열 변수에 담습니다. (간단한 페이지용)
    # 내용이 길어지면 관리가 힘들어서 보통 Case 3(템플릿) 방식을 씁니다.
    html_content = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <div>My name is Audio Library.</div>
        </body>
        </html>'''
    return html_content

from fastapi.templating import Jinja2Templates # 템플릿 엔진(Jinja2) 사용을 위한 임포트
from fastapi.requests import Request # 템플릿 렌더링 시 필요한 HTTP 요청 객체

# ==========================================
# Case 3: 템플릿 엔진 사용 (Jinja2) - 코드와 디자인 분리
# ==========================================

# [수정됨] 변수명 충돌 방지 및 디렉토리 설정
# directory="templates" : 현재 폴더 내의 'templates' 폴더에서 html 파일을 찾겠다는 의미입니다.
templates = Jinja2Templates(directory="templates")

# http://localhost:8000/main_html
@app.get("/main_html")
def main_html(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

# http://localhost:8000/main_html_context
@app.get("/main_html_context")
def main_html_context(request: Request):
    # 템플릿에 전달할 데이터
    context = {
        "request": request,
        "title": "FastAPI + Jinja Example",
        "items": ["Apple", "Banana", "Cherry"],
        "user": {"name": "Sanghun", "age": 33}
    }
    return templates.TemplateResponse("main_context.html", context)


@app.get("/user_list")
def user_list(request: Request):
    # 템플릿에 전달할 데이터
    context = {
        "request": request,
        "users": [
            {"name": "Alice", "age": 25, "city": "Seoul"},
            {"name": "Bob", "age": 30, "city": "Busan"},
            {"name": "Charlie", "age": 28, "city": "Daegu"}
        ]
    }
    return templates.TemplateResponse("users/list.html", context)

# 정적 파일 설정
from fastapi.staticfiles import StaticFiles
# 정적 파일(이미지, CSS, JS 등)을 제공하기 위한 설정
# URL 경로 "/images"으로 접근하면 로컬 'resources/images' 폴더의 파일들이 제공됩니다.
app.mount("/images", StaticFiles(directory="resources/images"))
app.mount("/css", StaticFiles(directory="resources/css"))

@app.get("/jina2")
def jina2(request: Request):
    # 템플릿에 전달할 데이터
    context = {
        "request": request,
        "products": [
            {
                "name": "Laptop",
                "price": 1200,
                "tags": ["electronics", "office"]
            },
            {
                "name": "Smartphone",
                "price": 800,
                "tags": ["mobile", "electronics"]
            },
            {
                "name": "Keyboard",
                "price": 100,
                "tags": ["accessories"]
            }
        ]
    }
    return templates.TemplateResponse("10_jina2.html", context)

# http://localhost:8000/board/detail_json?title=Third%20Post&content=This%20is%20the%20third%20post
@app.get("/board/detail_json")
async def board_details_json(request: Request):
    # 템플릿에 전달할 데이터
    params = dict(request.query_params)
    return {"title":params['title'], "content":params['content']}

@app.post("/board/detail_post_json")
async def board_details_post_json(request: Request):
    # 템플릿에 전달할 데이터
    params = dict(await request.form())
    return {"title":params['title'], "content":params['content']}

# http://localhost:8000/board/detail_html/{detail_id}
@app.get("/board/detail_html/{detail_id}}")
async def board_details_html(request: Request, detail_id):
    return templates.TemplateResponse("boards/detail.html", {"request": request})

@app.get("/board/detail_html")
async def board_details_html(request: Request):
    return templates.TemplateResponse("boards/detail.html", {"request": request})

