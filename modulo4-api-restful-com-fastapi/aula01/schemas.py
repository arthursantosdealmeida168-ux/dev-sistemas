from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Entrada: POST e PUT (campos obrigatórios)
class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    preco: float = Field(..., gt=0) # gt=0 - O valor do produto tem que ser maior que zero
    estoque: int = Field(0, ge=0) # ge=0 - O valor é maior ou igual a zero

# Entrada: PATCH (todos opcionais)
class ProdutosPatch(BaseModel):
    nome: Optional[str] = Field(None,min_length=2, max_length=100)
    preco: Optional[str] = Field(None, gt=0)
    estoque: Optional[str] = Field(None, ge=0)

# Saída: o que a API retorna
class ProdutivoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    ativo: bool
    criado_em: datetime

    class Config:
        from_attributes = True # permite converter SQLALchemy > Pydantic