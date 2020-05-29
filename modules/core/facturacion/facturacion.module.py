# Importamos las librerias necesarias para el modulo
import os
import sqlite3
import importlib.machinery

# Importamos las utilidades necesarias para el archivo main.py
loader = importlib.machinery.SourceFileLoader('inputU', './modules/utilities/input.utilities.py')
inputU = loader.load_module('inputU')

def facturacion(dbConection, db):
  factura = inputU.inputNumber('Ingresa el numero de factura para ver: ')

  db.execute('SELECT * FROM ventas WHERE id=' + str(factura))
  results = db.fetchall()
  if len(results) < 1:
    print("\nFactura inexistente\n")
  else:
    for row in results:

      id_venta, id_cliente, total = row

      db.execute('SELECT nombre_prod, precio_prod FROM prod_ventas WHERE id_venta=' + str(id_venta))
      results = db.fetchall()

      if len(results) > 0:
        for prod in results:
          nombre_prod, precio_prod = prod
          print("\nNombre del producto: %s\nPrecio del producto:%f" % (nombre_prod, precio_prod))

      print("\n-------------------------------")
      print("Nit del consumidor: %i" % (id_cliente))
      print("Total de la compra: %s" % (str(round(total, 2))))
      print("-------------------------------\n")

  input('Precione enter para continuar...')


# Funcion que es llamada al seleccionar el modulo de facturacion en el menu principal
def mainFunction(mainMenu):
  # Usamos cls para borrar la terminal en windows o clear para linux
  os.system('cls' if os.name == 'nt' else 'clear')

  # Nos conectamos a la base de datos y creamos un cursor
  dbConection = sqlite3.connect('./_database_/db.sql')
  db = dbConection.cursor()


  '''
    Codigo del modulo
  '''
  facturacion(dbConection, db)
  '''
    Codigo del modulo
  '''


  # Nos desconectamos de la base de datos
  dbConection.close()

  # REGRESAL AL MENU PRINCIPAL
  mainMenu()