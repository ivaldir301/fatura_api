from pydantic import BaseModel
import sys

sys.path.insert(1, '/Users/ivaldir/Desktop/coding/ApiFaturacao')
from models.produtoFaturaVenda import ProdutoFaturaVenda

class FaturaVenda(BaseModel):    
        tipoFaturaId: str             
        serie_id: str 
        data_venda: str
        condicoes_pagamento: str 
        cliente_id: str
        produtos: list[ProdutoFaturaVenda] 
        requisicao: str 
        desconto_financeiro: float 
        nota: str 

