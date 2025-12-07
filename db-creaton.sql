
-- Crear la base de datos:

CREATE DATABASE BibliotecaDB;

GO;

USE BibliotecaDB;

GO;

-- Crear tablas básicas
CREATE TABLE tblAutores (
	IdAutor INT IDENTITY(1,1) PRIMARY KEY,
	Nombres NVARCHAR(100) NOT NULL,
	Apellidos NVARCHAR(100) NOT NULL,
	Nacionalidad NVARCHAR(100) NOT NULL,
	OtrosDetalles NVARCHAR(MAX)
);

GO;

CREATE TABLE tblUsuarios (
	IdUsuario INT IDENTITY(1,1) PRIMARY KEY,
	Nombres NVARCHAR(100) NOT NULL,
	Apellidos NVARCHAR(100) NOT NULL,
	Direccion NVARCHAR(200),
	CorreoElectronico NVARCHAR(200) NOT NULL,
	OtrosDetalles NVARCHAR(MAX)
);

GO;

CREATE TABLE tblCategorías (
	IdCategoría INT IDENTITY(1,1) PRIMARY KEY,
	Descripción NVARCHAR(100) NOT NULL,
	OtrosDetalles NVARCHAR(MAX)
);

GO;

CREATE TABLE tblLibros (
	ISBN DECIMAL(13,0) PRIMARY KEY,
	Título NVARCHAR(200) NOT NULL,
	Publicación NVARCHAR(100) NOT NULL,
	FechaPublicación DATETIME NOT NULL,
	IdCategoría INT NOT NULL,
	IdAutor INT NOT NULL,
	OtrosDetalles NVARCHAR(MAX),
	
	CONSTRAINT FK_Libros_Autores FOREIGN KEY (IdAutor)
	REFERENCES tblAutores(IdAutor)
	ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT FK_Libros_Categorias FOREIGN KEY (IdCategoría)
	REFERENCES tblCategorías(IdCategoría)
	ON DELETE CASCADE ON UPDATE CASCADE
);

GO;

CREATE TABLE tblPrestamos (
	IdPrestamo INT IDENTITY(1,1) PRIMARY KEY,
	IdUsuario INT NOT NULL,
	ISBN DECIMAL(13,0) NOT NULL,
	FechaPréstamo DATETIME NOT NULL,
	FechaVencimiento DATETIME NOT NULL,
	FechaDevolución DATETIME NOT NULL,
	MultaPagar DECIMAL(10,2),
	OtrosDetalles NVARCHAR(MAX),
	
	CONSTRAINT FK_Prestamo_Libros FOREIGN KEY (ISBN)
	REFERENCES tblLibros(ISBN)
	ON DELETE CASCADE ON UPDATE CASCADE,
	
	CONSTRAINT FK_Prestamo_Usuario FOREIGN KEY (IdUsuario)
	REFERENCES tblUsuarios(IdUsuario)
	ON DELETE CASCADE ON UPDATE CASCADE
);

GO;

-- Agregar campo a tabla
ALTER TABLE tblLibros
	ADD Disponible BIT DEFAULT 1;

GO;


--  Eliminar por ser creado por error
CREATE TABLE Paises (
	PaisID INT IDENTITY(1,1) PRIMARY KEY,
	Siglas VARCHAR(5) NOT NULL,
	Nombre NVARCHAR(100) NOT NULL
);

GO;

DROP TABLE Paises;

-- Crear una restricción que evite préstamos con fecha de devolución anterior al préstamo.

ALTER TABLE tblPrestamos
	ADD CONSTRAINT check_fecha_devolución
	CHECK(FechaPréstamo < FechaDevolución);

GO;

-- Practicar ALTER TABLE para agregar un campo “Editorial” a la tabla Libros.

ALTER TABLE tblLibros
	ADD Editorial NVARCHAR(100) NULL;


-- Agregando libros vencidos para ejercicio 5

ALTER TABLE tblPrestamos
	ALTER COLUMN FechaDevolución DATETIME NULL

