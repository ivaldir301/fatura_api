from typing import Union

class queryCliente:
    def __init__(self,
                id: str = None,
                nome: str = None,
                individual_coletivo: str = None,
                designacao: str = None,
                descricao: str = None,
                nif: str = None,
                email: str = None,
                telefone: int = None,
                data_registro: str = None,
                data_alteracao: str = None,
                estado: str = None,
                pr_enquadramento_id: str = None,
                pessoa_de_contacto: str = None,
                glb_user: str = None,
                entidade_id: str = None) -> None:
       
        self.__id = id
        self.__nome = nome
        self.__individual_coletivo = individual_coletivo
        self.__designacao = designacao
        self.__nif = nif
        self.__email = email
        self.__telefone = telefone
        self.__data_registro = data_registro
        self.__data_alteracao = data_alteracao
        self.__estado = estado
        self.__pr_enquadramento_id = pr_enquadramento_id
        self.__pessoa_de_contacto = pessoa_de_contacto
        self.__descricao = descricao
        self.__glb_user = glb_user
        self.__entidade_id = entidade_id 
    
    def insert_new_client_in_database(self):
        return """"
                INSERT INTO `cliente`(`ID`,
                      `DESIG`,
                      `IND_COLETIVO`,
                      `DESCR`, 
                      `NIF`,
                      `EMAIL`,
                      `TELEFONE`,
                      `DT_REGISTO`,
                      `DT_ALTERACAO`,
                      `ESTADO`,
                      `pr_enquadramento_ID`,
                      `PESSOA_CONTACTO`,
                       glb_user_ID`,
                      `Entidade_ID) VALUES ('{}',
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
                                             '{}')
            """.format(self.__id,
                       self.__designacao,
                       self.__individual_coletivo,
                       self.__descricao,
                       self.__nif,
                       self.__email,
                       self.__telefone,
                       self.__data_registro,
                       self.__data_alteracao,
                       self.__estado,
                       self.__pr_enquadramento_id,
                       self.__pessoa_de_contacto,
                       self.__glb_user,
                       self.__entidade_id)

    def get_all_clients_in_database(self) -> None:
        return "SELECT * FROM cliente;"
    
    def get_client_with_id(self):
        return """
                SELECT * FROM cliente WHERE id = {};
            """.format(self.__id)
    
    def update_client_with_id(self):
        return """
                UPDATE cliente SET 
                    nome = '{}',
                    IND_COLETIVO = '{}',
                    NIF = '{}',
                    EMAIL = '{}',
                    TELEFONE = {},
                    pr_enquadramento_ID = '{}',
                    PESSOA_CONTACTO = '{}',
                    DESCR = '{}'
                WHERE ID = '{}'
            """.format(self.__nome, 
                       self.__individual_coletivo,
                       self.__nif,
                       self.__email,
                       self.__telefone,
                       self.__pr_enquadramento_id,
                       self.__pessoa_de_contacto,
                       self.__descricao,
                       self.__id)
    
    def delete_client_with_id(self):
        return "DELETE FROM cliente WHERE ID = '{}".format(self.__id)