CREATE TABLE "CARRITO" (
	"id_carrito"	INTEGER NOT NULL,
	"id_usuario"	INTEGER NOT NULL,
	"id_producto"	INTEGER NOT NULL,
	"cantidad"	NUMERIC NOT NULL,
	PRIMARY KEY("id_carrito")
)
CREATE TABLE "DOMICILIO" (
	"id_domicilio"	INTEGER NOT NULL,
	"id_usuario"	INTEGER NOT NULL,
	"barrio"	TEXT NOT NULL,
	"calle"	TEXT NOT NULL,
	"altura"	NUMERIC NOT NULL,
	"ciudad"	TEXT NOT NULL,
	"provincia"	TEXT NOT NULL,
	"cp"	INTEGER NOT NULL,
	PRIMARY KEY("id_domicilio")
)
CREATE TABLE "METODO_PAGO" (
	"id_metodo_pago"	INTEGER NOT NULL,
	"Efectivo"	INTEGER NOT NULL,
	"tarjeta_credito"	INTEGER NOT NULL,
	"tarjeta_debito"	INTEGER NOT NULL,
	PRIMARY KEY("id_metodo_pago")
)
CREATE TABLE "ORDEN" (
	"id_orden"	INTEGER NOT NULL,
	"id_usuario"	INTEGER NOT NULL,
	"id_metodopago"	INTEGER NOT NULL,
	"total"	NUMERIC NOT NULL,
	"id_domicilio"	INTEGER NOT NULL,
	PRIMARY KEY("id_orden")
)
CREATE TABLE "ORDEN_DETALLE" (
	"id_orden_detalle"	INTEGER NOT NULL,
	"id_orden"	INTEGER NOT NULL,
	"Id_producto"	INTEGER NOT NULL,
	"cantidad"	NUMERIC NOT NULL,
	"precio"	NUMERIC NOT NULL,
	"fecha"	INTEGER NOT NULL,
	PRIMARY KEY("id_orden_detalle")
CREATE TABLE "PRODUCTO" (
	"id_producto"	INTEGER NOT NULL,
	"nombre_producto"	INTEGER NOT NULL UNIQUE,
	"categoria_producto"	INTEGER NOT NULL,
	"precio_producto"	INTEGER NOT NULL,
	PRIMARY KEY("id_producto" AUTOINCREMENT)
)
CREATE TABLE "USUARIO" (
	"id_usuario"	INTEGER NOT NULL,
	"nombre_usuario"	INTEGER(50) NOT NULL UNIQUE,
	"dni_usuario"	INTEGER(8) NOT NULL,
	"email_usuario"	INTEGER(30) NOT NULL,
	"password_usuario"	INTEGER NOT NULL,
	PRIMARY KEY("id_usuario" AUTOINCREMENT)
)

CREATE TABLE sqlite_sequence(name,seq)
)
