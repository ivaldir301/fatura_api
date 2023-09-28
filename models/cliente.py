from pydantic import BaseModel

class Cliente2(BaseModel):
    codigo: str = None
    ind_coletivo: str
    designacao: str
    descricao: str
    nif: int
    numero_cliente: str
    email: str
    telefone: int
    geografia_id: str
    coordenadas: str
    endereco: str
    dt_registro: str
    dt_alteracao: str
    estado: str
    pessoa_contacto: str
    is_cliente_validado: str
    pr_enquadramento_id: str
    glb_user_id: str
    entidade_id: str

        