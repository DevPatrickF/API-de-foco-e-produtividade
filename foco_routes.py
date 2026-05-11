from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import FocoInput
from models import FocoBanco
from dependencies import save_db

foco_router = APIRouter(prefix='/foco') #router responsavel pelo endpoint de registro de foco



def descricao_foco(nivel_foco: int):
    niveis = {
        1: 'Muito distraido',
        2: 'Pouco foco',
        3: 'Foco moderado',
        4: 'Muito focado',
        5: 'Estado de flow, parabéns'
    }

    return niveis.get(nivel_foco)


@foco_router.post('/registro-foco', status_code= status.HTTP_201_CREATED, summary='Registro de sessão de foco')
async def registrar_foco(dados: FocoInput, db: Session = Depends(save_db)):

    if dados.nivel_foco <1 or dados.nivel_foco >5:
         return {
            'Error': 'O nivel de foco deve estar entre 1 e 5'
        }
    
    if dados.tempo_minutos <1 or dados.tempo_minutos > 720:
        return {
            'Error': 'O limite de tempo tem que ser maior que 1 minuto e menor que 720 minutos'
        }
    

    novo_registro = FocoBanco(
        nivel_foco = dados.nivel_foco,
        tempo_minutos = dados.tempo_minutos,
        comentario = dados.comentario,
        categoria = dados.categoria
    )
    

    db.add(novo_registro)
    db.commit()
    

    return {
        'mensagem': 'Registro criado com sucesso!',
        'registro': {
            'id': novo_registro.id,
            'nivel_foco': novo_registro.nivel_foco,
            'descricao_foco': descricao_foco(novo_registro.nivel_foco),
            'tempo_minutos': novo_registro.tempo_minutos,
            'comentario': novo_registro.comentario,
            'categoria': novo_registro.categoria
        }
    }