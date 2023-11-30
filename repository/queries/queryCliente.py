class queryCliente:
    def __init__(self,
                id: str = None,
                codigo: str = None,
                ind_coletivo: str = None, 
                designacao: str = None,
                descricao: str = None, 
                nif: int = None, 
                numero_cliente: int = None,
                email: str = None, 
                telefone: int = None,
                geografia_id: str = None,
                endereco: str = None,
                dt_registro: str = None,
                dt_alteracao = None,
                pessoa_contacto: str = None,
                entidade_id: str = None) -> None:
       
        self.__id = id
        self.__codigo = codigo
        self.__ind_coletivo = ind_coletivo
        self.__designacao = designacao
        self.__descricao = descricao
        self.__nif = nif
        self.__numero_cliente = numero_cliente
        self.__email = email
        self.__telefone = telefone
        self.__geografia_id = geografia_id
        self.__endereco = endereco
        self.__dt_registro = dt_registro
        self.__dt_alteracao = dt_alteracao
        self.__pessoa_contacto = pessoa_contacto
        self.__entidade_id = entidade_id
    

    def insert_new_client_in_database(self) -> str:
        return """
                INSERT INTO `cliente`(`ID`,
                    `CODIGO`,
                    `IND_COLETIVO`,
                    `DESIG`, 
                    `DESCR`,
                    `NIF`,
                    `NUM_CLIENTE`,
                    `EMAIL`,
                    `TELEFONE`,
                    `GEOGRAFIA_ID`,
                    `ENDERECO`,
                    `DT_REGISTO`,
                    `PESSOA_CONTACTO`,
                    `Entidade_ID`) VALUES (
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}');
                    """.format(
                            self.__id,
                            self.__codigo,
                            self.__ind_coletivo,
                            self.__designacao,
                            self.__descricao,
                            self.__nif,
                            self.__numero_cliente,
                            self.__email,
                            self.__telefone,
                            self.__geografia_id,
                            self.__endereco,
                            self.__dt_registro,
                            self.__pessoa_contacto,
                            self.__entidade_id)

    def get_all_clients_in_database(self) -> str:
        return "SELECT * FROM cliente;"
    
    def get_client_with_id(self):
        return """
                SELECT * FROM cliente WHERE id = '{}';
            """.format(self.__id)
    
    def update_client_with_codigo(self, codigo) -> str:
        return """
                UPDATE cliente SET 
                    `IND_COLETIVO`='{}',
                    `DESIG`='{}',
                    `DESCR`='{}',
                    `NIF`='{}',
                    `NUM_CLIENTE`='{}',
                    `EMAIL`='{}',
                    `TELEFONE`='{}',
                    `GEOGRAFIA_ID`='{}',
                    `ENDERECO`='{}',
                    `DT_ALTERACAO`='{}',
                    `PESSOA_CONTACTO`='{}',
                    'Entidade_ID' = '{}',
            WHERE CODIGO = '{}'
            """.format(self.__ind_coletivo,
                       self.__designacao,
                       self.__descricao,
                       self.__nif,
                       self.__numero_cliente,
                       self.__email,
                       self.__telefone,
                       self.__geografia_id,
                       self.__endereco,
                       self.__dt_alteracao,
                       self.__pessoa_contacto,
                       self.__entidade_id,
                       codigo)
    
    def delete_client_with_codigo(self, codigo: str) -> str:
        return "DELETE FROM cliente WHERE CODIGO = '{}'".format(codigo)