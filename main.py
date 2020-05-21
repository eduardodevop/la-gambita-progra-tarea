# Importamos las librerias necesarias para el archivo main.py
import importlib.machinery
import sqlite3

# Importamos las utilidades necesarias para el archivo main.py
loader = importlib.machinery.SourceFileLoader('mainMenu', './modules/common/mainMenu.module.py')
mainMenu = loader.load_module('mainMenu')

# Nos conectamos a la base de datos y creamos un cursor
dbConection = sqlite3.connect('./_database_/db.sql')
db = dbConection.cursor()

# Creamos tabla de clientes si es que no existe
db.execute('''
CREATE TABLE IF NOT EXISTS clientes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(100) NOT NULL,
  nit VARCHAR(50) NOT NULL
);
''')

# Creamos tabla de inventario si es que no existe
db.execute('''
CREATE TABLE IF NOT EXISTS inventario (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre_prod VARCHAR(100) NOT NULL,
  desc_prod VARCHAR(255),
  precio_prod REAL NOT NULL,
  stock integer NOT NULL DEFAULT 0
);
''')

# Creamos tabla de proveedores si es que no existe
db.execute('''
CREATE TABLE IF NOT EXISTS proveedores (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(100) NOT NULL,
  nit VARCHAR(50) NOT NULL
);
''')

# Creamos tabla de ventas y productos de las ventas si es que no existe
db.execute('''
CREATE TABLE IF NOT EXISTS ventas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cliente INTEGER NOT NULL,
  total REAL NOT NULL
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS prod_ventas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_venta INTEGER NOT NULL,
  id_producto INTEGER NOT NULL,
  nombre_prod VARCHAR(100) NOT NULL,
  desc_prod VARCHAR(255),
  precio_prod REAL NOT NULL,
  cantidad INTEGER NOT NULL
);
''')

# Guardamos los cambios en la base de datos
dbConection.commit()

# Nos desconectamos de la base de datos
dbConection.close()

### Gatillamos el proceso del programa llamando al menu por primera vez ###
mainMenu.drawMenu()
### Gatillamos el proceso del programa llamando al menu por primera vez ###