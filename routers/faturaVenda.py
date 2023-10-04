import sys
from authentication.autoDocumentationAuthentication import check_entity_credencials

sys.path.insert(1, "/Users/ivaldir/Desktop/coding/ApiFaturacao-Producao")

from models.venda.faturaVenda import FaturaVenda
import http.client
import json
from fastapi import Body, APIRouter, Depends, HTTPException, status

router = APIRouter() 

@router.post("/faturavenda", tags=["Fatura Venda"])
def insertNewFaturaVenda(faturaVenda: FaturaVenda = Body(...), username: str = Depends(check_entity_credencials)):
    conn = http.client.HTTPSConnection("fatura.opentec.cv")
    
    faturaVendaJson = json.dumps(faturaVenda ,default=lambda o:  o.__dict__, sort_keys=False, indent=4)
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_csrf=ac410cbb999a9149a88e8b1f8e76fa45d2b12cb8d865ba3d822d54de6d800b9ba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22rSDvz6Gq7hxMWmfIX23oruyQvEuQrHnS%22%3B%7D; app-opentec-lab=j6tlei98du7fbtc7siaukhn84r'
    }
        
    try:
        conn.request("POST", "/web/index.php?r=remote-venda/create", faturaVendaJson, headers)
        res = conn.getresponse()
        data = res.read()
        if str(data).find("false"):
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Operação não completa devido a um erro",
                    headers={"WWW-Authenticate": "Basic"},
            )
        elif str(data).find("true"):     
            raise HTTPException(
                    status_code=status.HTTP_202_ACCEPTED,
                    detail="Operação bem sucedida",
                    headers={"WWW-Authenticate": "Basic"},
            )
    except Exception as e:
        print(e)
       
    
    
