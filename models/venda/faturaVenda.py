from pydantic import BaseModel
import sys

sys.path.insert(1, '/Users/ivaldir/Desktop/coding/ApiFaturacao')
from models.produtoFaturaVenda import ProdutoFaturaVenda

class FaturaVenda(BaseModel):    
        tipoFaturaId: str             
        condicoes_pagamento: str 
        cliente_codigo: str
        produtos: list[ProdutoFaturaVenda] 
        requisicao: str 
        desconto_financeiro: float 
        nota: str 

