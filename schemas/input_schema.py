from typing import Optional




class InputSchema():
    id: Optional[str]
    field_1: str
    author: str
    description: str
    my_numeric_field: float
    def __init__(self, field_1: str, author: str, description: str, my_numeric_field: float):
        self.field_1 = field_1
        self.author = author.upper()
        self.description = description
        self.my_numeric_field = my_numeric_field
