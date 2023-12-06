from models.cliente import Cliente2

class queryCliente:
    def __init__(self, cliente: Cliente2 = None) -> None:
        self.__cliente = cliente

    def insert_new_client_in_database(self, id: str, codigo: str, data_registro: str) -> str:
        # print(self.__endereco)
        # print(self.__dt_registro)
        print(data_registro)
        print(self.__cliente.pessoa_contacto)
        print(self.__cliente.entidade_id)
        
        query = """
            INSERT INTO cliente (
                ID,
                CODIGO,
                IND_COLETIVO,
                DESIG,
                DESCR,
                NIF,
                NUM_CLIENTE,
                EMAIL,
                TELEFONE,
                GEOGRAFIA_ID,
                ENDERECO,
                DT_REGISTO,
                PESSOA_CONTACTO,
                Entidade_ID
            ) VALUES (
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
                {},
                {}
            );
        """.format(
            id,
            codigo,
            self.__cliente.ind_coletivo,
            self.__cliente.designacao,
            self.__cliente.descricao,
            self.__cliente.nif,
            self.__cliente.numero_cliente,
            self.__cliente.email,
            self.__cliente.telefone,
            self.__cliente.geografia_id,
            self.__cliente.endereco,
            data_registro,
            "'{}'".format(self.__cliente.pessoa_contacto) if self.__cliente.pessoa_contacto is not None else 'NULL',
            "'{}'".format(self.__cliente.entidade_id) if self.__cliente.entidade_id is not None else 'NULL'
        )

        return query


    def get_all_clients_in_database(self) -> str:
        return "SELECT * FROM cliente;"
    
    def get_client_with_id(self, id):
        return """
                SELECT * FROM cliente WHERE id = '{}';
            """.format(id)
    
    def update_client_with_codigo(self, codigo: str, data_alteracao: str) -> str:
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
                    `Entidade_ID` = '{}'
                WHERE CODIGO = '{}';
            """.format(self.__cliente.ind_coletivo,
                        self.__cliente.designacao,
                        self.__cliente.descricao,
                        self.__cliente.nif,
                        self.__cliente.numero_cliente,
                        self.__cliente.email,
                        self.__cliente.telefone,
                        self.__cliente.geografia_id,
                        self.__cliente.endereco,
                        data_alteracao,
                        self.__cliente.pessoa_contacto,
                        self.__cliente.entidade_id,
                        codigo)
    
    def delete_client_with_codigo(self, codigo: str) -> str:
        return "DELETE FROM cliente WHERE CODIGO = '{}'".format(codigo)