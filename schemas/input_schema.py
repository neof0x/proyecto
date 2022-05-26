from pydantic import BaseModel
from typing import Optional




class InputSchema(BaseModel):
    id: Optional[str]
    field_1: str
    author: str
    description: str
    my_numeric_field: float

    def maysucula_field_1(self, field_1: str, author: str, description: str, my_numeric_field: float):

        self.field_1 = field_1.upper()
        self.author = author
        self.description = description
        self.my_numeric_field = my_numeric_field


    def maysucula_author(self, field_1: str, author: str, description: str, my_numeric_field: float):

        self.field_1 = field_1
        self.author = author.upper()
        self.description = description
        self.my_numeric_field = my_numeric_field


    def maysucula_description(self, field_1: str, author: str, description: str, my_numeric_field: float):

        self.field_1 = field_1
        self.author = author
        self.description = description.upper()
        self.my_numeric_field = my_numeric_field

