from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from uuid import uuid4

from database import engine, SessionLocal
from models import Base, Rose

# Create DB tables
Base.metadata.create_all(bind=engine)

# 👇 THIS IS WHAT UVICORN IS LOOKING FOR
app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def create_page(request: Request):
    return templates.TemplateResponse(
        "create.html",
        {"request": request}
    )


@app.post("/create", response_class=HTMLResponse)
def create_rose(
    request: Request,
    name: str = Form(...),
    message: str = Form(...)
):
    db = SessionLocal()
    rose_id = str(uuid4())

    rose = Rose(
        id=rose_id,
        name=name,
        message=message
    )

    db.add(rose)
    db.commit()
    db.close()

    share_link = f"{request.base_url}rose/{rose_id}"

    return templates.TemplateResponse(
        "share.html",
        {
            "request": request,
            "link": share_link
        }
    )


@app.get("/rose/{rose_id}", response_class=HTMLResponse)
def view_rose(request: Request, rose_id: str):
    db = SessionLocal()
    rose = db.query(Rose).filter(Rose.id == rose_id).first()
    db.close()

    return templates.TemplateResponse(
        "rose.html",
        {"request": request, "rose": rose}
    )
