class queryProduto:
    def __init__(self, 
                 id: str = None,
                 codigo: str = None,
                 designacao: str = None,
                 produto_servico: str = None,
                 vendivel: str = None,
                 compravel: str = None,
                 preco_custo: str = None,
                 preco_venda: str = None,
                 pr_categoria_id: str = None,
                 entidade_id: str = None,
                 glb_user_id: str = None,
                 pr_iva_id: str = None,
                 pr_iva_compra_id: str = None,
                 pr_unidade_id: str = None,
                 data_registro: str = None,
                 data_alteracao: str = None,
                 estado: str = None,
                 desconto_comercial: bool = None,
                 foto_perfil: str = None) -> None:
                 
        self.__id = id
        self.__codigo = codigo
        self.__designacao = designacao
        self.__produto_servico = produto_servico
        self.__vendivel = vendivel
        self.__compravel = compravel
        self.__preco_custo = preco_custo
        self.__preco_venda = preco_venda
        self.__pr_categoria_id = pr_categoria_id
        self.__entidade_id = entidade_id
        self.__glb_user_id = glb_user_id
        self.__pr_iva_id = pr_iva_id
        self.__pr_iva_compra_id = pr_iva_compra_id
        self.__pr_unidade_id = pr_unidade_id
        self.__data_registro = data_registro
        self.__data_alteracao = data_alteracao
        self.__estado = estado
        self.__desconto_comercial = desconto_comercial
        self.__foto_perfil = foto_perfil

    def insert_new_product_in_database(self):
        return """
                INSERT INTO `produto`(`ID`,
                      `CODIGO`,
                      `DESIG`,
                      `Produto_servico`,
                      `Vendivel`,
                      `Compravel`,
                      `Preco_custo`,
                      `Preco_venda`,
                      `pr_categoria_ID`,
                      `Entidade_ID`,
                      `glb_user_ID`,
                      `pr_iva_ID`,
                      `PR_IVA_COMPRA_ID`,
                      `pr_unidade_ID`,
                      `DT_REGISTO`,
                      `DT_ALTERACAO`,
                      `ESTADO`,
                      `DESCONTO_COMERCIAL`,
                      `FOTO_PERFIL`) VALUES ('{}',
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
                                             '{}',
                                             '{}',
                                             '{}',
                                             '{}',
                                             '{}',
                                             '{}',
                                             {},
                                             '{}');
            """.format(
                self.__id,
                self.__codigo,
                self.__designacao,
                self.__produto_servico,
                self.__vendivel,
                self.__compravel,
                self.__preco_custo,
                self.__preco_venda,
                self.__pr_categoria_id,
                self.__entidade_id,
                self.__glb_user_id,
                self.__pr_iva_id,
                self.__pr_iva_compra_id,
                self.__pr_unidade_id,
                self.__data_registro,
                self.__data_alteracao,
                self.__estado,
                self.__desconto_comercial,
                self.__foto_perfil)

    def get_all_products_in_database(self) -> str:
        return "SELECT * FROM produto;"
    
    def get_product_with_id(self) -> str:
        return "SELECT * FROM produto WHERE ID = '{}';".format(self.__id)
    
    def update_product_with_id(self) -> str:
        return """
                UPDATE `produto` SET 
                    `CODIGO`='{}',
                    `DESIG`='{}',
                    `Produto_servico`='{}',
                    `Vendivel`='{}',
                    `Compravel`='{}',
                    `Preco_custo`= {},
                    `Preco_venda`= {},
                    `pr_categoria_ID`='{}',
                    `Entidade_ID`='{}',
                    `glb_user_ID`='{}',
                    `pr_iva_ID`='{}',
                    `PR_IVA_COMPRA_ID`='{}',
                    `pr_unidade_ID`='{}',
                    `DT_REGISTO`='{}',
                    `DT_ALTERACAO`='{}',
                    `ESTADO`='{}',
                    `DESCONTO_COMERCIAL`= {},
                    `FOTO_PERFIL`='{}'
                WHERE ID = '{}';""".format(
                                        self.__codigo,
                                        self.__designacao,
                                        self.__produto_servico,
                                        self.__vendivel,
                                        self.__compravel,
                                        self.__preco_custo,
                                        self.__preco_venda, 
                                        self.__pr_categoria_id,
                                        self.__entidade_id,
                                        self.__glb_user_id,
                                        self.__pr_iva_id,
                                        self.__pr_iva_compra_id,
                                        self.__pr_unidade_id,
                                        self.__data_registro,
                                        self.__data_alteracao,
                                        self.__estado,
                                        self.__desconto_comercial,
                                        self.__foto_perfil,
                                        self.__id)

    def delete_product_with_id(self) -> str:
        return "DELETE FROM produto WHERE ID = '{}';".format(self.__id)
    

