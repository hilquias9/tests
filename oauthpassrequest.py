from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm,HTTPBearer,HTTPAuthorizationCredentials
from datetime import timedelta,datetime,timezone
import jwt

CHAVE_SECRETA="SUPER_UPER_CHAVE_SECRETA"
ALGORITMO="HS256"

usuarios={"0":[{"Nome":"Hilquias","Senha":"123"}]}

def gerar_token(username):
    payload={
        "usuario_id":0,
        "usuario_name":username,
        "exp":datetime.now(timezone.utc)+timedelta(minutes=1)
    }
    token=jwt.encode(payload,CHAVE_SECRETA,algorithm=ALGORITMO)
    return token

app=FastAPI()
security=HTTPBearer()


@app.post("/login")
def login(form:OAuth2PasswordRequestForm=Depends()):
    if form.username!="hilquias" or form.password!="123":
        raise HTTPException(status_code=400,detail="incorreto")
    else:
        token=gerar_token("hilquias")
        return {"msg":["Token_gerado!",token]}

@app.get("/perfil")
def perfil(credentials:HTTPAuthorizationCredentials=Depends(security)):
    token=credentials.credentials
    try:
        payload=jwt.decode(token,CHAVE_SECRETA,algorithms=ALGORITMO)
        return payload
    except Exception:
        raise HTTPException(status_code=401,detail="Usuário não autorizado!")
