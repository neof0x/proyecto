from pydantic import BaseModel
from typing import Optional




class InputSchema(BaseModel):
    id: Optional[str]
    field_1: str
    author: str
    description: str
    my_numeric_field: float
