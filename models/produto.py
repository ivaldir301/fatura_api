from pydantic import BaseModel

# class Produto:
#     def __init__(self, 
#                  id: str = None,
#                  codigo: int = None,
#                  designacao: str = None,
#                  produto_servico: str = None,
#                  vendivel: str = None,
#                  compravel: str = None,
#                  preco_custo: float = None,
#                  preco_venda: float = None,
#                  pr_categoria_id: str = None,
#                  entidade_id: str = None,
#                  glb_user_id: str = None,
#                  pr_iva_id: str = None,
#                  pr_iva_compra_id: str = None,
#                  pr_unidade_id: str = None,
#                  dt_registro = None,
#                  dt_alteracao = None,
#                  estado: str = None,
#                  desconto_comercial: float = None,
#                  foto_perfil: str = None) -> None:
        
#             self.id = id
#             self.codigo = codigo
#             self.designacao = designacao
#             self.produto_servico = produto_servico
#             self.vendivel = vendivel
#             self.compravel = compravel
#             self.preco_custo = preco_custo
#             self.preco_venda = preco_venda
#             self.pr_categoria_id = pr_categoria_id
#             self.entidade_id = entidade_id
#             self.glb_user_id = glb_user_id
#             self.pr_iva_id = pr_iva_id
#             self.pr_iva_compra_id = pr_iva_compra_id
#             self.pr_unidade_id = pr_unidade_id
#             self.dt_registro = dt_registro
#             self.dt_alteracao = dt_alteracao
#             self.estado = estado
#             self.desconto_comercial = desconto_comercial
#             self.foto_perfil = foto_perfil
            
class Produto2(BaseModel):
    id: str 
    codigo: str 
    designacao: str 
    produto_servico: str 
    vendivel: str 
    compravel: str 
    preco_custo: float 
    preco_venda: float 
    pr_categoria_id: str 
    entidade_id: str 
    glb_user_id: str 
    pr_iva_id: str 
    pr_iva_compra_id: str 
    pr_unidade_id: str 
    dt_registro: str
    dt_alteracao: str
    estado: str 
    desconto_comercial: float
    foto_perfil: str 