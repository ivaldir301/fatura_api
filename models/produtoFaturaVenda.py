from pydantic import BaseModel

class ProdutoFaturaVenda(BaseModel):
    produto_codigo: str
    qttd: int
    preco_unid: float
    desc_comercial: int
