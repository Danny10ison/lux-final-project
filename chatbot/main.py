# documentation

from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from models import MyForm

app = FastAPI()

templates = Jinja2Templates(directory="core/templates/")
app.mount("/core/static", StaticFiles(directory="core/static/"), name="static" )



@app.get("/")
async def get_root():
    return {"Hello": "World"}

@app.get('/home', response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})