from pydantic import BaseModel
from typing import List

class Symbol(BaseModel):
    id: int
    name: str
    confidence: float
    bbox: List[int]

class DetectResponse(BaseModel):
    file_name: str
    symbols: List[Symbol]

