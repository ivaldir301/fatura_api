import sys
 
sys.path.insert(1, '/Users/ivaldir/Desktop/coding/ApiFaturacao')

from repository.configuration.databaseConfigurationAndQuery import DatabaseConnectorAndQuery


def check_if_new_codigo_exists_and_generate_new(codigoUseType: int) -> str:
    queryMaiorCodigoNaBaseDeDados = ""

    if codigoUseType == 1:
        queryMaiorCodigoNaBaseDeDados = "SELECT (CODIGO) FROM `cliente` ORDER BY CODIGO DESC LIMIT 5000;"
    else:
        queryMaiorCodigoNaBaseDeDados = "SELECT (CODIGO) FROM `produto` ORDER BY CODIGO DESC LIMIT 5000;"
        
    mysqlDBTest = DatabaseConnectorAndQuery(
                '127.0.0.1',
                'faturacao',
                'root',
                '',
                queryMaiorCodigoNaBaseDeDados,
                1
    )
    
    result = mysqlDBTest.connect_to_database()
    
    print(result[0])
       
    sanitazedResult = (((((str(result[0]).replace('(', '', 1))).replace(')', '', 1)).replace(',', '', 1)).replace("'", '', 2))
    return str(int(sanitazedResult) + 1).zfill(5) 

# print(check_if_new_codigo_exists_and_generate_new(2))