BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Roles y Permisos" (
	"Administrador"	INTEGER NOT NULL DEFAULT 1 UNIQUE,
	"User"	INTEGER NOT NULL DEFAULT 2
);
CREATE TABLE IF NOT EXISTS "Usuarios" (
	"id"	INTEGER UNIQUE,
	"Apelllido y Nombre"	TEXT NOT NULL,
	"DNI"	NUMERIC NOT NULL,
	"Password"	TEXT NOT NULL,
	"Telefono"	NUMERIC,
	"Email"	TEXT
);
CREATE TABLE IF NOT EXISTS "Producto" (
	"Id"	INTEGER UNIQUE,
	"Stock"	NUMERIC UNIQUE,
	"Importe"	REAL NOT NULL,
	"Tipo"	TEXT NOT NULL,
	"Nombre-Producto"	INTEGER NOT NULL,
	"fecha de Vencimiento"	INTEGER,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Carrito" (
	"Productos"	TEXT NOT NULL,
	"Pago"	REAL NOT NULL,
	"Medios de Pago"	TEXT NOT NULL
);
COMMIT;
