from pydantic import BaseModel
         
class Produto2(BaseModel):
    designacao: str 
    descricao: str
    produto_servico: str 
    vendivel: str  
    preco_custo: float 
    preco_venda: float 
    entidade_id: str 
    pr_iva_codigo: str 
    pr_unidade_codigo: str   
        
   