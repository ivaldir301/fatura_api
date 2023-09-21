from database.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from database.queries.queryCliente import queryCliente
from models.cliente import Cliente

def generateNewClientId():
    return "id"

newClient = Cliente(
    'opentec-logo.png',
    '1969',
    'S',
    'Ivaldir Batalha update funciona',
    'Ivaldir',
    '130042552',
    '',
    'ivalbat1@gmail.com',
    '2385925264',
    'CV774741741037410303',
    '',
    '2023-09-19 11:44:20',
    '2023-09-20 11:44:10',
    'A',
    'teste',
    '',
    '567ED7F5-8F21-4467-AF3C-D25230233421',
    '1fd8fc20-d611-11e8-a359-a0d3c1588c38',
    'A56CA66F-54DB-4953-88FE-47C8C7D653B3',
    '000189f4-f5b1-a5c0-65b4-90b1b4b0ffd4')


queryClientTest = queryCliente(
    newClient.id,
    newClient.foto_perfil,
    newClient.codigo,
    newClient.ind_coletivo,
    newClient.designacao,
    newClient.descricao,
    newClient.nif,
    newClient.numero_cliente,
    newClient.email,
    newClient.telefone,
    newClient.geografia_id,
    newClient.coordenadas,
    newClient.dt_registro,
    newClient.dt_alteracao,
    newClient.estado,
    newClient.pessoa_contacto,
    newClient.is_cliente_validado,
    newClient.pr_enquadramento_id,
    newClient.glb_user_id,
    newClient.entidade_id
)

def test_query_update_client():
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryClientTest.update_client_with_id(),
                3
    )
    
    
    dbQueryResults = mysqlDBTest.connect_to_database()
    assert dbQueryResults == "Data updated sucessfully"
