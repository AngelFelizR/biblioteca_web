"""
This estrategy was taken from:
    - Mapping Declaratively with Reflected Tables (https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#orm-declarative-reflected)
"""

from config import engine
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from typing import List
import pandas as pd

class Base(DeclarativeBase):
    pass

Base.metadata.reflect(engine)

class Autor(Base):
    __table__ = Base.metadata.tables["tblAutores"]
    # Un autor tiene muchos libros
    libros: Mapped[List["Libro"]] = relationship(back_populates="autor") 

class Categoria(Base):
    __table__ = Base.metadata.tables["tblCategorías"]
    # Una categoría tiene muchos libros
    libros: Mapped[List["Libro"]] = relationship(back_populates="categoria") 

class Libro(Base):
    __table__ = Base.metadata.tables["tblLibros"]
    # Un libro tiene un autor y una categoría (relación many-to-one)
    autor: Mapped["Autor"] = relationship(back_populates="libros")
    categoria: Mapped["Categoria"] = relationship(back_populates="libros")
    
    # Un libro puede tener muchos préstamos a lo largo del tiempo
    prestamos: Mapped[List["Prestamo"]] = relationship(back_populates="libro")

class Usuario(Base):
    __table__ = Base.metadata.tables["tblUsuarios"]
    # Un usuario tiene muchos préstamos
    prestamos: Mapped[List["Prestamo"]] = relationship(back_populates="usuario")

class Prestamo(Base):
    __table__ = Base.metadata.tables["tblPrestamos"]
    # Un préstamo pertenece a un usuario y a un libro
    usuario: Mapped["Usuario"] = relationship(back_populates="prestamos")
    libro: Mapped["Libro"] = relationship(back_populates="prestamos")

def print_class_metadata(class_name):
    """
    Imprime los nombres de las columnas y sus tipos de datos,
    eliminando la información de COLLATION si está presente,
    con tabulación alineada.
    """
    COL_WIDTH = 24

    table_to_check = {
        "Autor": "tblAutores",
        "Categoria": "tblCategorías",
        "Libro": "tblLibros",
        "Prestamo": "tblPrestamos",
        "Usuario": "tblUsuarios"
    }[class_name]
    
    print(f"\n--- Metadatos de la clase {class_name} ({table_to_check}) ---")
    print(f"{'COLUMNA':<{COL_WIDTH}} | TIPO DE DATO")
    print("-" * (COL_WIDTH + 25))
    
    for col in Base.metadata.tables[table_to_check].columns:
        col_type_str = str(col.type)
        clean_type = col_type_str.split(" COLLATE")[0].strip()
        print(f"{col.name:<{COL_WIDTH}} | {clean_type}")

# To list tables in DB
if __name__ == "__main__":
    
    print(list(Base.metadata.tables.keys()))

    print_class_metadata("Libro")

    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM tblLibros;"))
        column_names = result.keys()
        data = result.fetchall()
        df_libros = pd.DataFrame(data, columns=column_names)
        print(df_libros)

