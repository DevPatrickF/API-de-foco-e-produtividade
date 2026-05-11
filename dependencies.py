from database import SessionLocal

def save_db():
    db = SessionLocal() #abrindo conexao e criando sessao do banco de dados

    try:    
        yield db

    finally:
        db.close()
