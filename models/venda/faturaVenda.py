from pydantic import BaseModel
from models.produtoFaturaVenda import ProdutoFaturaVenda

class FaturaVenda(BaseModel):                 
        serie_id: str
        data_venda: str
        condicao_pagamento: str 
        cliente_id: str
        produtos: ProdutoFaturaVenda = []
        requisicao: str 
        desconto_financeiro: float 
        nota: str 
    
    