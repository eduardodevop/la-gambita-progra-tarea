# Importamos las librerias necesarias para el modulo
import os
import sqlite3
import importlib.machinery

# Importamos las utilidades necesarias para el archivo main.py
loader = importlib.machinery.SourceFileLoader('inputU', './modules/utilities/input.utilities.py')
inputU = loader.load_module('inputU')

def panelDeVenta(dbConection, db, carrito = [], titulo = ''):
  # Usamos cls para borrar la terminal en windows o clear para linux
  os.system('cls' if os.name == 'nt' else 'clear')

  if len(carrito) < 1:
    print("Aun no tienes productos en el carrito")
  else:
    print("Productos en el carrito:\n")
    total = 0
    for i in range(len(carrito)):
      print('Producto: ' + str(carrito[i][1]) + '\nPrecio: ' + str(carrito[i][3]) + '\n')
      total = round(total + carrito[i][3], 2)
    print('Costo total del pedido: %s' % (str(total)))

  if len(titulo) > 0:
    print('\n' + titulo)

  entrada = inputU.inputRequired('\nIngresa el ID del producto para agregarlo al carrito o escribe FIN para finalizar la venta -> ')

  if entrada == "FIN":

    # Usamos cls para borrar la terminal en windows o clear para linux
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(carrito) < 1:
      print("No tienes productos en el carrito, venta cancelada")
      input('Precione enter para continuar...')
    else:

      nit = inputU.inputNumber('Ingrese el nit del cliente: ')
      total = 0
      for i in range(len(carrito)):
        total = round(total + carrito[i][3], 2)

      db.execute("INSERT INTO ventas (id_cliente, total) VALUES (" + str(nit) + ", " + str(total) + ")")
      dbConection.commit()
      idFactura = db.lastrowid

      for i in range(len(carrito)):
        db.execute("INSERT INTO prod_ventas (id_venta, id_producto, nombre_prod, desc_prod, precio_prod, cantidad) VALUES (" + str(idFactura) + ", " + str(carrito[i][0]) + ", '" + str(carrito[i][1]) + "', '" + str(carrito[i][2]) + "', " + str(carrito[i][3]) + ", 1)")
        dbConection.commit()

      del carrito[:]
      print("Venta concluida, tu id de factura es %i por favor guardalo" % (idFactura))
      input('Precione enter para continuar...')

  else:
    try:
      entrada = int(entrada)
    except ValueError:
      panelDeVenta(dbConection, db, titulo = 'ERROR: Tienes que ingresar un numero o la palabra FIN')

    db.execute('SELECT * FROM inventario WHERE id=' + str(entrada))
    results = db.fetchall()
    if len(results) < 1:
      panelDeVenta(dbConection, db, titulo = 'ERROR: Producto inexistente')
    else:
      for row in results:

        _, nombre, descripcion, precio, stock = row

        if stock < 1:
          panelDeVenta(dbConection, db, titulo = 'El producto "' + nombre + '" esta agotado')

        carrito.append(row)

    panelDeVenta(dbConection, db, titulo = '-> Producto agregado correctamente <-')

# Funcion que es llamada al seleccionar el modulo de venta en el menu principal
def mainFunction(mainMenu):
  # Usamos cls para borrar la terminal en windows o clear para linux
  os.system('cls' if os.name == 'nt' else 'clear')

  # Nos conectamos a la base de datos y creamos un cursor
  dbConection = sqlite3.connect('./_database_/db.sql')
  db = dbConection.cursor()


  '''
    Codigo del modulo
  '''
  panelDeVenta(dbConection, db)
  '''
    Codigo del modulo
  '''


  # Nos desconectamos de la base de datos
  dbConection.close()

  # REGRESAL AL MENU PRINCIPAL
  mainMenu()