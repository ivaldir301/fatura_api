from typing import Union

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
                coordenadas: str = None,
                endereco: str = None,
                dt_registro = None,
                dt_alteracao = None,
                estado: str = None,
                pessoa_contacto: int = None,
                is_cliente_validado: bool = None,
                pr_enquadramento_id: str = None,
                glb_user_id: str = None,
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
        self.__coordenadas = coordenadas
        self.__endereco = endereco
        self.__dt_registro = dt_registro
        self.__dt_alteracao = dt_alteracao
        self.__estado = estado
        self.__pessoa_contacto = pessoa_contacto
        self.__is_cliente_validado = is_cliente_validado
        self.__pr_enquadramento_id = pr_enquadramento_id
        self.__glb_user_id = glb_user_id
        self.__entidade_id = entidade_id
    

    def insert_new_client_in_database(self) -> str:
        return """
                INSERT INTO `cliente`(`ID`,
                    `FOTO_PERFIL`,
                    `CODIGO`,
                    `IND_COLETIVO`,
                    `DESIG`, 
                    `DESCR`,
                    `NIF`,
                    `NUM_CLIENTE`,
                    `EMAIL`,
                    `TELEFONE`,
                    `GEOGRAFIA_ID`,
                    `COORDENADAS`,
                    `ENDERECO`,
                    `DT_REGISTO`,
                    `DT_ALTERACAO`,
                    `ESTADO`,
                    `PESSOA_CONTACTO`,
                    `IS_CLIETE_VALIDADO`,
                    `pr_enquadramento_ID`,
                    `glb_user_ID`,
                    `Entidade_ID`) VALUES ('{}',
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
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}',
                    '{}');
                    """.format(
                            self.__id,
                            self.__foto_perfil,
                            self.__codigo,
                            self.__ind_coletivo,
                            self.__designacao,
                            self.__descricao,
                            self.__nif,
                            self.__numero_cliente,
                            self.__email,
                            self.__telefone,
                            self.__geografia_id,
                            self.__coordenadas,
                            self.__endereco,
                            self.__dt_registro,
                            self.__dt_alteracao,
                            self.__estado,
                            self.__pessoa_contacto,
                            self.__is_cliente_validado,
                            self.__pr_enquadramento_id,
                            self.__glb_user_id,
                            self.__entidade_id)

    def get_all_clients_in_database(self) -> str:
        return "SELECT * FROM cliente;"
    
    def get_client_with_id(self):
        return """
                SELECT * FROM cliente WHERE id = '{}';
            """.format(self.__id)
    
    def update_client_with_id(self) -> str:
        return """
                UPDATE cliente SET 
                    `FOTO_PERFIL`='{}',
                    `CODIGO`='{}',
                    `IND_COLETIVO`='{}',
                    `DESIG`='{}',
                    `DESCR`='{}',
                    `NIF`='{}',
                    `NUM_CLIENTE`='{}',
                    `EMAIL`='{}',
                    `TELEFONE`='{}',
                    `GEOGRAFIA_ID`='{}',
                    `COORDENADAS`='{}',
                    `ENDERECO`='{}',
                    `DT_REGISTO`='{}',
                    `DT_ALTERACAO`='{}',
                    `ESTADO`='{}',
                    `PESSOA_CONTACTO`='{}',
                    `IS_CLIETE_VALIDADO`='{}',
                    `pr_enquadramento_ID`='{}',
                    `glb_user_ID`='{}',
                    `Entidade_ID`='{}'
            WHERE ID = '{}'
            """.format(self.__foto_perfil,
                       self.__codigo,
                       self.__ind_coletivo,
                       self.__designacao,
                       self.__descricao,
                       self.__nif,
                       self.__numero_cliente,
                       self.__email,
                       self.__telefone,
                       self.__geografia_id,
                       self.__coordenadas,
                       self.__endereco,
                       self.__dt_registro,
                       self.__dt_alteracao,
                       self.__estado,
                       self.__pessoa_contacto,
                       self.__is_cliente_validado,
                       self.__pr_enquadramento_id,
                       self.__glb_user_id,
                       self.__entidade_id,
                       self.__id)
    
    def delete_client_with_id(self) -> str:
        return "DELETE FROM cliente WHERE ID = '{}'".format(self.__id)