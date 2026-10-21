from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from datetime import datetime

class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    email: EmailStr = Field(..., description="E-mail válido")
    senha: str = Field(..., min_length=8)

    # @fiel-validator valida o campo 'nome' antes de salva
    # Se a validação falhar: raise ValueError com a mensagem de erro
    # Se a passar: return valor (o valor é validado)
    @field_validator('nome')
    @classmethod
    def nome_sem_numeros(cls, valor:str) -> str:
         if any(char.isdigit() for char in valor):
              raise ValueError('Nome não pode conter números')
         if not valor.strip():
              raise ValueError('Nome não pode ser só espaços')
         return valor.strip()

    @field_validator('senha')
    @classmethod
    def senha_deve_ter_letra_e_numero(cls, valor:str) -> str:
         tem_letra = any(caracter.isalpha() for caracter in valor)
         tem_numero = any(caracter.isdigit() for caracter in valor)
         if not tem_letra or not tem_numero:
              raise ValueError('Senha deve conter letras e números')
         return valor

class UsuarioPatch(BaseModel):
    nome: Optional[str] = Field(default=None, min_length=2, max_length=100)
    email: Optional[EmailStr] = Field(default=None, description="E-mail válido")

    @field_validator('nome')
    @classmethod
    def nome_sem_numeros(cls, valor):
         if valor and any(char.isdigit() for char in valor):
              raise ValueError('Nome não pode conter números')
         return valor.strip() if valor else valor

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