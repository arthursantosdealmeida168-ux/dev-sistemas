import bcrypt
from jose import JWSError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRECT_KEY = 'poder-ser-qualquer-mensagem'
ALGORITHM = 'HS256'
EXPIRA_MIN = 60

# HTTPBearer faz o Swagger monstrar um campo simples para colar o token
# Em vez de OAuthPasswordBearer que pede username/password
security = HTTPBearer()

# Criar função criar_hash
def criar_hash(senha: str) -> str:
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

# Criar função verificar_senha
def verificar_senha(senha: str, hash_salvo: str) -> bool:
    return bcrypt.checkpw(senha.encode(), hash_salvo.encode())

# Criar função criar_token
def criar_token(dados: dict) -> str:
    payload = dados.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=EXPIRA_MIN)
    return jwt.encode(payload, SECRECT_KEY, algorithm=ALGORITHM)

# Criar função usuario_logado
def usuario_logado(
        credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> str:
    token = credentials.credentials        # pega só token, sem Bearer
    try:
        payload = jwt.decode(token, SECRECT_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(401, "token inválido")
        return email
    except JWSError:
        raise HTTPException(401, "Token inválido ou expirado")