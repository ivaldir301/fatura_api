from pydantic import BaseModel
import sys

sys.path.insert(1, '/Users/ivaldir/Desktop/coding/ApiFaturacao')
from models.produtoFaturaVenda import ProdutoFaturaVenda

class FaturaVenda(BaseModel):    
        tipoFaturaId: str             
        serie_id: str 
        data_venda: str
        condicao_pagamento: str 
        cliente_id: str
        produtos: list[ProdutoFaturaVenda] 
        requisicao: str 
        desconto_financeiro: float 
        nota: str 


# test = FaturaVenda(serie_id = "fdsafsd",
#                    produtos=[{"quantidade":10, "preco_unidade": 1000, "desc_comercial": 10},
#                              {"quantidade":15, "preco_unidade": 1500, "desc_comercial": 20}
#                              ]
# )


# print(vars(test))

    