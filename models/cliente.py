from pydantic import BaseModel

class Cliente2(BaseModel):
    ind_coletivo: str = None
    designacao: str = None
    descricao: str = None
    nif: int = None
    numero_cliente: str = None
    email: str = None
    telefone: int = None
    geografia_id: str = None
    endereco: str = None
    pessoa_contacto: str = None
    entidade_id: str = None

        