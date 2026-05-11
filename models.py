
from sqlalchemy import Column, Integer, String
from database import Base 


class FocoBanco(Base):
    __tablename__ = 'Banco_de_Dados'


    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nivel_foco = Column(Integer)
    tempo_minutos = Column(Integer)
    comentario = Column(String)
    categoria = Column(String)

    