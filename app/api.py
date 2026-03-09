from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.parser import parse_user_query
from app.router import handle_query

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "answer": None, "question": None},
    )


@router.post("/ask", response_class=HTMLResponse)
def ask(request: Request, question: str = Form(...)):
    parsed = parse_user_query(question)
    answer = handle_query(parsed)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "answer": answer,
            "question": question,
        },
    )