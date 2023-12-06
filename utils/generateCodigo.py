import sys
 
sys.path.insert(1, "C:/Users/USER/Documents/faturacv")

from repository.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

def check_if_new_codigo_exists_and_generate_new(codigoUseType: int) -> str:
    if codigoUseType == 1:
        queryMaiorCodigoNaBaseDeDados = "SELECT MAX(CODIGO) FROM cliente;"
    else:
        queryMaiorCodigoNaBaseDeDados = "SELECT MAX(CODIGO) FROM produto;"
        
    mysqlDBTest = DatabaseConnectorAndQuery(
                env['DATABASE_IP_ADRESS'],
                env['DATABASE_PORT'],
                env["DATABASE_NAME"],
                env['DATABASE_USER_NAME'],
                env['DATABASE_PASSWORD'],
                queryMaiorCodigoNaBaseDeDados,
                1
    )
    defaultCode = "0"

    result = (((((((str(mysqlDBTest.connect_to_database())).replace('(', '', 1)).replace(')', '', 1)).replace(',', '', 1)).replace("'", '', 2)).replace('[', '', 1)).replace(']', '', 1))
    if result != "None":
        return str(int(result) + 1).zfill(5) 
    else:
        return defaultCode

print(check_if_new_codigo_exists_and_generate_new(1))