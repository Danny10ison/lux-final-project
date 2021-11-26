'''Run the app

'''

from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Chatbot API - Product Chat Assis",
    description="A simple API that helps you when you have a problem with a product from a company, eg.TV from samsung ",
    version="0.1",
)

templates = Jinja2Templates(directory="core/templates/")
app.mount("/core/static", StaticFiles(directory="core/static/"), name="static" )



@app.get('/home', response_class=HTMLResponse)
async def get_assistant(request: Request):
    '''Get Assisstant
       
       Display bot UI
    '''
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/home', response_class=HTMLResponse)
async def get_user_message(request: Request, message: str = Form(...)):
    '''Is able to print user message in server'''
    print(f"message: {message}")
    return templates.TemplateResponse("index.html", {"request": request})