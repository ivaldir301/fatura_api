from pydantic import BaseModel

# class Cliente(BaseModel):
#     def __init__(self,
#                   id: str, 
#                   foto_perfil: str, 
#                   codigo: str, 
#                   ind_coletivo: str, 
#                   designacao: str,
#                   descricao: str, 
#                   nif: int, 
#                   numero_cliente: int,
#                   email: str, 
#                   telefone: int,
#                   geografia_id: str,
#                   coordenadas: str,
#                   endereco: str,
#                   dt_registro,
#                   dt_alteracao,
#                   estado: str,
#                   pessoa_contacto: int,
#                   is_cliente_validado: bool,
#                   pr_enquadramento_id: str,
#                   glb_user_id: str,
#                   entidade_id: str) -> None:
    
#         self.id = id
#         self.foto_perfil = foto_perfil
#         self.codigo = codigo
#         self.ind_coletivo = ind_coletivo
#         self.designacao = designacao
#         self.descricao = descricao
#         self.nif = nif
#         self.numero_cliente = numero_cliente
#         self.email = email
#         self.telefone = telefone
#         self.geografia_id = geografia_id
#         self.coordenadas = coordenadas
#         self.endereco = endereco
#         self.dt_registro = dt_registro
#         self.dt_alteracao = dt_alteracao
#         self.estado = estado
#         self.pessoa_contacto = pessoa_contacto
#         self.is_cliente_validado = is_cliente_validado
#         self.pr_enquadramento_id = pr_enquadramento_id
#         self.glb_user_id = glb_user_id
#         self.entidade_id = entidade_id

class Cliente2(BaseModel):
    id: str
    foto_perfil: str
    codigo: str
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

        