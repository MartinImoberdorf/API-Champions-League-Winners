from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from bd.database import  engine, base

from routers.winners import routerWinner

app= FastAPI(
    title='Winners of the UEFA Champions League',
    description='Information about UEFA Champions League finals',
    version='0.0.1'
)

base.metadata.create_all(bind=engine)

@app.get('/', tags=['Inicio'])
def read_root():
    with open('web/index.html', 'r') as archivo_html:
        contenido_html = archivo_html.read()
    return HTMLResponse(content=contenido_html, status_code=200)

app.include_router(routerWinner)

