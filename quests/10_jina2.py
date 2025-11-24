from fastapi import FastAPI
from fastapi.templating import Jinja2Templates # 템플릿 엔진(Jinja2) 사용을 위한 임포트
from fastapi.requests import Request # 템플릿 렌더링 시 필요한 HTTP 요청 객체

app = FastAPI()
from fastapi.requests import Request # 템플릿 렌더링 시 필요한 HTTP 요청 객체

templates = Jinja2Templates(directory="quests/templates")

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