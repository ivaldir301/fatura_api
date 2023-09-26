from pydantic import BaseModel
         
class Produto2(BaseModel):
    # id: str
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
        
   