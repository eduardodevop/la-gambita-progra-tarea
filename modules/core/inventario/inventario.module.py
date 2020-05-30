# Importamos las librerias necesarias para el modulo
import os
import sqlite3
# Importamos la libreria para llamar algunas utilidades
import importlib.machinery

# Importamos las utilidades necesarias para el archivo main.py
loader = importlib.machinery.SourceFileLoader('inputU', './modules/utilities/input.utilities.py')
inputU = loader.load_module('inputU')

# Menu del modulo
def moduleMenu(dbConection, db, titulo = '+++ Seleccione una opción del menú +++'):
  # Usamos cls para borrar la terminal en windows o clear para linux
  os.system('cls' if os.name == 'nt' else 'clear')

  print('Modulo de inventario', '\n')
  print(titulo, '\n')
  print('1. Mostrar productos')
  print('2. Agregar nuevo producto')
  print('3. Editar producto')
  print('4. Eliminar producto')
  print('5. Regresar al menu principal')

  opcion = inputU.inputNumber("\n-> ")

  # Llamamos a la funcion correcta para cada opcion del menu
  if opcion == 1:
    showProducts(dbConection, db)
  elif opcion == 2:
    addProduct(dbConection, db)
  elif opcion == 3:
    editProduct(dbConection, db)
  elif opcion == 4:
    removeProduct(dbConection, db)
  elif opcion == 5:
    pass

  else:
    # Si no se ingreso un valor valido entonces regresamos al usuario al menu con un mensaje de error
    moduleMenu(dbConection, db, titulo = '+++ Error: Opción no valida\t\t+++\n+++ Seleccione una opción del menú\t+++')

# Funcion para mostrar clientes
def showProducts(dbConection, db):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-> Mostrando productos <-\n')

  '''
    Codigo del modulo
  '''

  db.execute('SELECT * FROM inventario')

  results = db.fetchall()

  if len(results) < 1:
    print('No hay registros en la base de datos')
  else:
    for row in results:
      print("ID:" + str(row[0]) + "\nNombre: " + str(row[1]) + "\nDescripcion: " + str(row[2]) + "\nPrecio: " + str(row[3]) + "\nUnidades disponibles: " + str(row[4]) )
      print('*********************')


  input('\nPrecione enter para continuar...')

  '''
    Codigo del modulo
  '''

  moduleMenu(dbConection, db)

# Funcion para agregar clientes
def addProduct(dbConection, db):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-> Agregar un producto <-\n')

  nombre = inputU.inputRequired('Nombre: ')
  descripcion = inputU.inputRequired('Descripcion: ')
  precio = inputU.inputNumber('Precio: ')
  stock = inputU.inputNumber('Unidades disponibles: ')

  db.execute('INSERT INTO inventario (nombre_prod, desc_prod, precio_prod, stock) VALUES ("' + nombre + '", "' + descripcion + '", ' + str(precio)  + ', ' + str(stock)  + ')')

  dbConection.commit()

  input('\nPrecione enter para continuar...')
  moduleMenu(dbConection, db)

# Funcion para editar productos
def editProduct(dbConection, db):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-> Editar un producto <-\n')

  nombre = inputU.inputRequired('Nombre: ')

  db.execute('SELECT * FROM inventario WHERE nombre_prod = "' + str(nombre) + '"')

  results = db.fetchall()

  if len(results) < 1:
    print('No se encontro el producto')
  else:

    descripcion = inputU.inputRequired('Nueva descripcion: ')
    precio = inputU.inputNumber('Nuevo precio: ')
    stock = inputU.inputNumber('Nuevas unidades disponibles: ')

    db.execute('UPDATE inventario SET desc_prod = "' + descripcion + '", precio_prod = ' + str(precio)  + ', stock = ' + str(stock)  + ' WHERE nombre_prod = "' + str(nombre) +'"')

    dbConection.commit()
    print('Producto actualizado')

  input('\nPrecione enter para continuar...')
  moduleMenu(dbConection, db)

# Funcion para borrar productos
def removeProduct(dbConection, db):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-> Eliminar un producto <-\n')

  nombre = inputU.inputRequired('Nombre: ')

  db.execute('DELETE FROM inventario WHERE nombre_prod="' + str(nombre) + '"')

  dbConection.commit()

  input('\nPrecione enter para continuar...')
  moduleMenu(dbConection, db)

# Funcion que es llamada al seleccionar el modulo de inventario en el menu principal
def mainFunction(mainMenu):
  # Usamos cls para borrar la terminal en windows o clear para linux
  os.system('cls' if os.name == 'nt' else 'clear')

  # Nos conectamos a la base de datos y creamos un cursor
  dbConection = sqlite3.connect('./_database_/db.sql')
  db = dbConection.cursor()

  '''
    Codigo del modulo
  '''
  moduleMenu(dbConection, db)
  '''
    Codigo del modulo
  '''

  # Nos desconectamos de la base de datos
  dbConection.close()

  # REGRESAL AL MENU PRINCIPAL
  mainMenu()