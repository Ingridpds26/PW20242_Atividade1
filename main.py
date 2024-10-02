from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
import uvicorn


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def paginainicial(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/cadastro")
def get_contato(request: Request):
     return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/post_cadastro")
def post_cadastro(
    request: Request, 
    nome: str = Form(...), 
    descricao: str = Form(...), 
    estoque: str = Form(...), 
    preco: str = Form(...)):
    

    return RedirectResponse("/", 303)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)