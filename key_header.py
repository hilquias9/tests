from fastapi import FastAPI,Depends,HTTPException, status
from fastapi.security import APIKeyHeader
#python -m uvicorn test:app --reload

app=FastAPI()

seguranca=APIKeyHeader(name="Authorization")

def verificacao(token: str=Depends(seguranca)):
    token_valido="token_secreto_super_uper123"

    if token!=token_valido:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="ACESSO NEGADO!")
    return "Hilquias"

@app.get("/perfil")
def carregar_perfil(usuario: str=Depends(verificacao)):
    return {"msg":f"Bem vindo {usuario}!"}
