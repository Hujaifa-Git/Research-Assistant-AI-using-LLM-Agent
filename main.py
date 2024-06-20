import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import config as ctg
from inference import create_agent, generate

app = FastAPI()
templates = Jinja2Templates(directory="templates")
agent_executor = None

@app.on_event("startup")
async def startup_event():
    global agent_executor
    agent_executor = create_agent()  # Initialize the agent executor

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": "", "selected_option": "", "query": ""})

@app.post("/", response_class=HTMLResponse)
async def handle_form(request: Request, option: str = Form(...), query: str = Form(...)):
    global agent_executor
    query += ctg.option_dict_for_web[option]
    response = generate(agent_executor, query)
    return templates.TemplateResponse("index.html", {"request": request, "response": response['output'], "selected_option": option, "query": query})



if __name__ == "__main__":
    # agent_executor = create_agent()
    uvicorn.run(app, host="0.0.0.0", port=8000)