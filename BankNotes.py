import imp
from lib2to3.pytree import Base
from pydantic import BaseModel

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float