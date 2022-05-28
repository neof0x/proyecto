from sqlalchemy import Table, Column 
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta





inputs = Table("inputs", meta,
            Column("id", Integer),
            Column("field_1", String(255),nullable=False),
            Column("author", String(255),nullable=False),
            Column("description", String(255),nullable=False),
            Column("my_numeric_field", Integer))


meta.create_all(engine)

