def get_codigo_int_auto(model, length):
    # Consulta o valor máximo de CODIGO no modelo e ordena em ordem decrescente
    queryMaiorCodigoNaBaseDeDados = ""

    if not queryMaiorCodigoNaBaseDeDados:
        resultado = 1
    else:
        resultado = 0

    # Retorna o resultado formatado com zeros à esquerda
    return str(resultado + 1).zfill(length)