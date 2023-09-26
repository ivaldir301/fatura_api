from pydantic import BaseModel

class ProdutoFaturaVenda(BaseModel):
    produto_id: str
    qttd: int
    preco_unid: float
    desc_comercial: int
