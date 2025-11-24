import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 1. 현재 실행 위치 확인
current_dir = os.getcwd()
print(f"📍 현재 실행 위치: {current_dir}")

# 2. templates 폴더 경로 확인 및 자동 생성
templates_dir = os.path.join(current_dir, "templates")
if not os.path.exists(templates_dir):
    print(f"⚠️ 'templates' 폴더가 없어서 자동으로 생성합니다: {templates_dir}")
    os.makedirs(templates_dir)
else:
    print(f"✅ 'templates' 폴더 확인됨: {templates_dir}")

# 3. main.html 파일 확인 및 자동 생성
template_file = os.path.join(templates_dir, "main.html")
if not os.path.exists(template_file):
    print(f"⚠️ 'main.html' 파일이 없어서 자동으로 생성합니다: {template_file}")
    with open(template_file, "w", encoding="utf-8") as f:
        f.write("<h1>자동 생성된 main.html 입니다!</h1>")
else:
    print(f"✅ 'main.html' 파일 확인됨")

# 4. Jinja2Templates 설정
# directory에 절대 경로를 넣어주면 실행 위치에 상관없이 안전하게 찾습니다.
templates = Jinja2Templates(directory=templates_dir)

@app.get("/main_html")
def main_html(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

if __name__ == "__main__":
    print("🚀 진단 완료. 서버를 시작합니다...")
    # host="0.0.0.0" 으로 설정하여 외부 접속 허용
    uvicorn.run(app, host="0.0.0.0", port=8000)