from models.produto import Produto2

class queryProduto:
    def __init__(self, produto: Produto2 = None) -> None:
        self.__produto = produto

    def insert_new_product_in_database(self, id: str, codigo: str, data_registro: str) -> str:
        return """
                INSERT INTO `produto`(`ID`,
                      `CODIGO`,
                      `DESIG`,
                      `DESCR`,
                      `Produto_servico`,
                      `Vendivel`,
                      `Preco_custo`,
                      `Preco_venda`,
                      `Entidade_ID`,
                      `pr_iva_ID`,
                      `pr_unidade_ID`,
                      `DT_REGISTO`) VALUES ('{}',
                                             '{}',
                                             '{}',
                                             '{}',
                                             '{}',
                                             '{}',
                                             {},
                                             {},
                                             '{}',
                                             '{}',
                                             '{}',
                                             '{}');
            """.format(
                id,
                codigo,
                self.__produto.designacao,
                self.__produto.descricao,
                self.__produto.produto_servico,
                self.__produto.vendivel,
                self.__produto.preco_custo,
                self.__produto.preco_venda,
                self.__produto.entidade_id,
                self.__produto.pr_iva_codigo,
                self.__produto.pr_unidade_codigo,
                data_registro)

    def get_all_products_in_database(self) -> str:
        return "SELECT * FROM produto;"
    
    def get_product_with_id(self) -> str:
        return "SELECT * FROM produto WHERE ID = '{}';".format(self.__id)
    
    def update_product_with_codigo(self, codigo: str, data_alteracao: str) -> str:
        return """
                UPDATE `produto` SET 
                      `DESIG` = '{}',
                      `DESCR` = '{}',
                      `Produto_servico` = '{}',
                      `Vendivel` = '{}',
                      `Preco_custo` = '{}',
                      `Preco_venda` = '{}',
                      `Entidade_ID` = '{}',
                      `pr_iva_ID` = '{}',
                      `pr_unidade_ID` = '{}',
                      `DT_ALTERACAO` = '{}'
                WHERE CODIGO = '{}';""".format(
                                        self.__produto.designacao,
                                        self.__produto.descricao,
                                        self.__produto.produto_servico,
                                        self.__produto.vendivel,
                                        self.__produto.preco_custo,
                                        self.__produto.preco_venda,
                                        self.__produto.entidade_id,
                                        self.__produto.pr_iva_codigo,
                                        self.__produto.pr_unidade_codigo,
                                        data_alteracao,
                                        codigo)

    def delete_product_with_codigo(self, codigo) -> str:
        return "DELETE FROM produto WHERE CODIGO = '{}';".format(codigo)
    

