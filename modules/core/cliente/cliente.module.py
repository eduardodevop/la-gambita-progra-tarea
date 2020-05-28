# Importamos las librerias necesarias para el modulo
import os
import sqlite3
import importlib.machinery

# Importamos las utilidades necesarias para el archivo main.py
loader = importlib.machinery.SourceFileLoader('inputU', './modules/utilities/input.utilities.py')
inputU = loader.load_module('inputU')

# Menu del modulo
def moduleMenu(dbConection, db, titulo = '+++ Seleccione una opción del menú +++'):
  # Usamos cls para borrar la terminal en windows o clear para linux
  os.system('cls' if os.name == 'nt' else 'clear')

  print('Modulo de clientes', '\n')
  print(titulo, '\n')
  print('1. Mostrar clientes')
  print('2. Agregar nuevo cliente')
  print('3. Eliminar cliente')
  print('4. Regresar al menu principal')

  opcion = inputU.inputNumber("\n-> ")

  # Llamamos a la funcion correcta para cada opcion del menu
  if opcion == 1:
    showClients(dbConection, db)
  elif opcion == 2:
    addClient(dbConection, db)
  elif opcion == 3:
    removeClient(dbConection, db)
  elif opcion == 4:
    pass

  else:
    # Si no se ingreso un valor valido entonces regresamos al usuario al menu con un mensaje de error
    moduleMenu(dbConection, db, titulo = '+++ Error: Opción no valida\t\t+++\n+++ Seleccione una opción del menú\t+++')

# Funcion para mostrar clientes
def showClients(dbConection, db):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-> Mostrando clientes <-\n')

  '''
    Codigo del modulo
  '''

  db.execute('SELECT * FROM clientes')

  results = db.fetchall()

  if len(results) < 1:
    print('No hay registros en la base de datos')
  else:
    for row in results:
      print("Nombre: " + str(row[1]) + "\tNit: " + str(row[2]))


  input('\nPrecione enter para continuar...')

  '''
    Codigo del modulo
  '''

  moduleMenu(dbConection, db)

# Funcion para agregar clientes
def addClient(dbConection, db):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-> Agregar un cliente <-\n')

  nombre = inputU.inputRequired('Nombre: ')
  nit = inputU.inputNumber('Nit: ')

  db.execute('INSERT INTO clientes (nombre, nit) VALUES ("' + nombre + '", ' + str(nit)  + ')')

  dbConection.commit()

  input('\nPrecione enter para continuar...')
  moduleMenu(dbConection, db)

# Funcion para borrar clientes
def removeClient(dbConection, db):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-> Eliminar un cliente <-\n')

  nit = inputU.inputNumber('Nit: ')

  db.execute('DELETE FROM clientes WHERE nit=' + str(nit))

  dbConection.commit()

  input('\nPrecione enter para continuar...')
  moduleMenu(dbConection, db)

# Funcion que es llamada al seleccionar el modulo de cliente en el menu principal
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