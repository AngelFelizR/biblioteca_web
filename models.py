from config import engine
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

Base.metadata.reflect(engine)

# To list tables in DB
list(Base.metadata.tables.keys())

class Autor(Base):
    __table__ = Base.metadata.tables["tblAutores"]

class Categoria(Base):
    __table__ = Base.metadata.tables["tblCategorías"]

class Libro(Base):
    __table__ = Base.metadata.tables["tblLibros"]

class Prestamo(Base):
    __table__ = Base.metadata.tables["tblPrestamos"]

class Usuario(Base):
    __table__ = Base.metadata.tables["tblUsuarios"]

def print_class_metadata(class_name):
    """
    Imprime los nombres de las columnas y sus tipos de datos,
    eliminando la información de COLLATION si está presente,
    con tabulación alineada.
    """
    table_to_check = {
        "Autor": "tblAutores",
        "Categoria": "tblCategorías",
        "Libro": "tblLibros",
        "Prestamo": "tblPrestamos",
        "Usuario": "tblUsuarios"
    }[class_name]
    
    print(f"\n--- Metadatos de la clase {class_name} ({table_to_check}) ---")
    
    COL_WIDTH = 20
    
    print(f"{'COLUMNA':<{COL_WIDTH}} | TIPO DE DATO")
    print("-" * (COL_WIDTH + 25))
    
    for col in Base.metadata.tables[table_to_check].columns:
        col_type_str = str(col.type)
        clean_type = col_type_str.split(" COLLATE")[0].strip()
        print(f"{col.name:<{COL_WIDTH}} | {clean_type}")