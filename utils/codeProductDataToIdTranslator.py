prIvaCodigoToId = {
    'NA' : 'B14B2AF5-BA35-465E-A25D-D4FA8D66BCBD',
    'TEU': '7F2A6B40-3755-4732-9C80-0E0D9166C450',
    'IVA': '36B46EFB-CBEB-4E1F-97F9-C77D2C79F08C', 
    'IR': 'E3812D20-47B5-416A-A5F0-4A1E9FB9FE3A', 
    'IS': '1d130664-d627-56fa-02e7-7dccb00c73e7'
}

prUnidadeCodigoToId = {
    'EA' : 'C6F795C4-E589-4A03-B596-3A1FD7AED1F3',
    'MTR': 'ab911f17-f2d0-e0ed-8225-aec5b6c74f65',
    'LTR': 'ABF074C2-2374-463F-ACB5-CE395E311396',
    'KGM': '867AD89B-5560-4F1B-8058-1F94589A2ABF',
    'MTQ': '805a2f7a-07cb-15e6-eb66-ce1c4fa231fe',
    'MTX': '3065de0c-12e1-90cf-34e3-aeb33264b519'
}

def prIvaCodigoTranslator(pr_iva_codigo: str):
    return prIvaCodigoToId[pr_iva_codigo]

def prUnidadeCodigoTranslator(pr_unidade_codigo: str):
    return prUnidadeCodigoToId[pr_unidade_codigo]

