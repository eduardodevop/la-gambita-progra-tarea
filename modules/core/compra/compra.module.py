# Importamos las librerias necesarias para el modulo
import os
import sqlite3
import importlib.machinery
# Importamos las utilidades necesarias
loader = importlib.machinery.SourceFileLoader('inputU', './modules/utilities/input.utilities.py')
inputU = loader.load_module('inputU')
'''
  Proovedores
'''
# Menu del modulo
def moduleMenu(dbConection, db,titulo="+++ Selecciona una opcion +++"):
  # Usamos cls para borrar la terminal en windows o clear para linux
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Modulo de Compras', '\n')
  print(titulo)
  print('1. Agregar compra')
  print('2. Mostrar Proveedores')
  print('3. Agregar nuevo Proveedor')
  print('4. Eliminar Proveedor')
  print('5. Regresar al menu principal')
  opcion = inputU.inputNumber("\n-> ")
  # Llamamos a la funcion correcta para cada opcion del menu
  if opcion == 1:
    compra(dbConection, db)
  elif opcion == 2:
    showProvs(dbConection, db)
  elif opcion == 3:
    addProv(dbConection, db)
  elif opcion == 4:
    removeProv(dbConection, db)
  elif opcion == 5:
    pass
  else:
    # Si no se ingreso un valor valido entonces regresamos al usuario al menu con un mensaje de error
    moduleMenu(dbConection, db, titulo = '+++ Error: Opción no valida\t\t+++\n+++ Seleccione una opción del menú\t+++')
# Funcion para mostrar Proveedores
def showProvs(dbConection, db):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-> Mostrando proveedores <-\n')
  db.execute('SELECT * FROM proveedores')
  results = db.fetchall()
  if len(results) < 1:
    print('No hay registros en la base de datos')
  else:
    for row in results:
      print("Nombre: " + str(row[1]) + "\tNit: " + str(row[2]))
  input('\nPrecione enter para continuar...')
  moduleMenu(dbConection, db)
# Funcion para agregar Proveedor
def addProv(dbConection, db):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-> Agregar un Proveedor <-\n')
  nombre = inputU.inputRequired('Nombre: ')
  nit = inputU.inputNumber('Nit: ')
  db.execute('INSERT INTO proveedores (nombre, nit) VALUES ("' + nombre + '", ' + str(nit)  + ')')
  dbConection.commit()
  input('\nPrecione enter para continuar...')
  moduleMenu(dbConection, db)
# Funcion para borrar Proveedores
def removeProv(dbConection, db):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-> Eliminar un Proveedor <-\n')
  nit = inputU.inputNumber('Nit: ')
  db.execute('DELETE FROM proveedores WHERE nit=' + str(nit))
  dbConection.commit()
  input('\nPrecione enter para continuar...')
  moduleMenu(dbConection, db)
# Funcion que es llamada al seleccionar el modulo de compra en el menu principal
'''
  Compras
'''
#modulo para agregar nueva compra
def compra(dbConection, db):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('-> Agregar una compra <-\n')
  nombreprod = inputU.inputRequired('Nombre del producto: ')
  #Seleccionamos el nombre del producto de la base de datos
  db.execute('SELECT nombre_prod FROM inventario WHERE nombre_prod ="'+nombreprod+'"')
  results = db.fetchall()
  #Si no hay resultados significa que es un nuevo producto y se procede a añadirlo
  if len(results) < 1:
    descripcionprod = inputU.inputRequired('Descripcion del producto: ')
    precioprod = inputU.inputNumber('Precio del producto: ')
    unidadesprod = inputU.inputNumber('Unidades adquiridas: ')
    #Se añade el nuevo producto a la base de datos
    db.execute('INSERT INTO inventario (nombre_prod, desc_prod, precio_prod, stock) VALUES ("' + nombreprod + '", "'+descripcionprod + '",'  +  str(precioprod)  +','+  str(unidadesprod)  +')')
  else:
    print("+++ El producto ya existe esta apunto de actualizar las unidades +++")
    unidadesprod = inputU.inputNumber('Unidades adquiridas: ')
    #Seleccionamos las unidades disponibles en la base de datos
    db.execute('SELECT stock FROM inventario WHERE nombre_prod ="'+nombreprod+'"')
    results = db.fetchall()
    #Sumamos las nuevas unidades a las unidades disonibles
    for row in results:
      unidadesprod = unidadesprod + int(row[0])
    #Actualizamos las unidades en la base de datos
    db.execute('UPDATE inventario SET stock = '+str(unidadesprod)+' WHERE nombre_prod ="'+nombreprod+'"')
  dbConection.commit()
  input('\nPrecione enter para continuar...')
  moduleMenu(dbConection, db)
'''
  main
'''
def mainFunction(mainMenu):
  # Usamos cls para borrar la terminal en windows o clear para linux
  os.system('cls' if os.name == 'nt' else 'clear')
  # Nos conectamos a la base de datos y creamos un cursor
  dbConection = sqlite3.connect('./_database_/db.sql')
  db = dbConection.cursor()
  #
  moduleMenu(dbConection, db)
  # Nos desconectamos de la base de datos
  dbConection.close()
  # REGRESAL AL MENU PRINCIPAL
  mainMenu()