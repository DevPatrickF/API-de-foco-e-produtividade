from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import FocoBanco
from sqlalchemy import func
from dependencies import save_db

performance_router = APIRouter(prefix='/performance') #router responsavel pelo endpoint de registro de performance


def gerar_feedback(foco: float): #função responsavel por gerar o feedback baseado no nivel de foco

    if foco < 2:
        return 'Seu foco esta muito baixo, tente reduzir suas distraçoes'
    
    elif foco < 3:
        return 'Seu foco está inconsistente, tente melhorar'
    
    elif foco < 4:
        return 'Você está em um bom nível de produtividade'
    
    else:
        return 'Parabéns, excelente desempenho, você está em estado de FLOW!!'
    

def gerar_registros(db):
    registros = db.query(FocoBanco).all()

    if not registros: #caso não haja registro armazenado retorna um error

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Nenhum registro encontrado.')
    

    media_foco = db.query(func.avg(FocoBanco.nivel_foco)).scalar() #calcula a media geral de nivel de foco baseado em todos os registross armazenados

    tempo_total = db.query(func.sum(FocoBanco.tempo_minutos)).scalar()

    total_registros = db.query(func.count(FocoBanco.id)).scalar()

    categoria_produtiva = db.query(  
        FocoBanco.categoria,
        func.count(FocoBanco.categoria)).group_by(FocoBanco.categoria).order_by(func.count(FocoBanco.categoria).desc()).first()

    
    feedback = gerar_feedback(media_foco)
    

    return {
        'Mensagem': 'Regitro de performance',
        'Performance': {
        'media_foco': round(media_foco, 2),
        'tempo_total_focado': tempo_total,
        'total_registros': total_registros,
        'categoria_mais_produtiva': categoria_produtiva[0],
        'feedback': feedback
    }
}

@performance_router.get('/diagnostico-produtividade', status_code=status.HTTP_200_OK)
async def diagnostico_produtividade(
    db: Session = Depends(save_db)
):

    return gerar_registros(db)