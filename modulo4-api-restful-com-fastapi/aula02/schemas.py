from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from datetime import datetime

class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    email: EmailStr = Field(..., description="E-mail válido")
    senha: str = Field(..., min_length=8)

class UsuarioPatch(BaseModel):
    nome: Optional[str] = Field(default=None, min_length=2, max_length=100)
    email: Optional[EmailStr] = Field(default=None, description="E-mail válido")

class UsuarioResponse(BaseModel):
       id: int
       nome: str
       email: str
       ativo: bool
       criado_em: datetime

       class Config:
            from_attributes = True

class ErroResponse(BaseModel):
     erro: str = Field(..., description="Mensagem de erro")
     detalhe: Optional[str] = Field(default=None, description="Adicição opcional de erro")