from pydantic import BaseModel

class ProdutoFaturaVenda(BaseModel):
    quantidade: int
    preco_unidade: float
    desc_comercial: int
