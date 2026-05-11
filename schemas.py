

from pydantic import BaseModel



class FocoInput(BaseModel):
    nivel_foco: int
    tempo_minutos: int
    comentario: str
    categoria: str

