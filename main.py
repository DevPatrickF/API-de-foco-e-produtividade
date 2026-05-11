
from fastapi import FastAPI
from foco_routes import foco_router
from performance_routes import performance_router
from database import engine
from models import FocoBanco, Base

Base.metadata.create_all(bind=engine) #criação do db


app = FastAPI(
    title='Api de performance',
    description= 'Api para monitorar foco e produtividade'
)

app.include_router(foco_router) #registra rotas relacionadas ao foco
app.include_router(performance_router) #registra rotas relacionadas a performance

@app.get('/teste-api')  #rota de teste.
def teste():
    return {
        'message': 'Api funcionando'
    }