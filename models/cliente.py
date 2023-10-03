from pydantic import BaseModel

class Cliente2(BaseModel):
    codigo: str = None
    ind_coletivo: str = None
    designacao: str = None
    descricao: str = None
    nif: int = None
    numero_cliente: str = None
    email: str = None
    telefone: int = None
    geografia_id: str = None
    coordenadas: str = None
    endereco: str = None
    dt_registro: str = None
    dt_alteracao: str = None
    estado: str = None
    pessoa_contacto: str = None
    is_cliente_validado: str = None
    pr_enquadramento_id: str = None
    glb_user_id: str = None
    entidade_id: str = None

        