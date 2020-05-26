# Importamos las librerias necesarias para el modulo
import os
import sqlite3
import importlib.machinery


loader = importlib.machinery.SourceFileLoader('inputU', './modules/utilities/input.utilities.py')
inputU = loader.load_module('inputU')


# Funcion que es llamada al seleccionar el modulo de inventario en el menu principal
def mainFunction(mainMenu):
  # Usamos cls para borrar la terminal en windows o clear para linux
  os.system('cls' if os.name == 'nt' else 'clear')

  # Nos conectamos a la base de datos y creamos un cursor
  dbConection = sqlite3.connect('./_database_/db.sql')
  db = dbConection.cursor()

  
  db.execute("INSERT INTO inventario VALUES(1,'Gambas','Son gambas amigo', 20, 80)")

  print('INVENTARIO\n')
  print('1. Mostrar Prouctos')
  print('2. Modificar Proucto')
  print('3. Consultar productos')
  opcion = inputU.inputNumber("\n ➤ ")

#MOSTRAMOS LOS PRODUCTOS
  if opcion == 1:
    print('MOSTRAR PRODUCTOS\n')
    os.system('cls' if os.name == 'nt' else 'clear') #Limpio la pantalla
    exic_show = db.execute('SELECT * FROM inventario').rowcount
    
    if exic_show <= 0:
      print('Error! No tiene productos')
      input('\nIngrese enter para continuar...')
      mainMenu()
    else:
      db.execute('SELECT * FROM inventario') #Se hace llaman los datos dentro de la tabla y su contenido con sentencia SQL
      rows = db.fetchall() #Se cuentan la cantidad de filas que tenga la tabla
      for row in rows: #Se hace un contador que mostrara los datos desde 0 hasta llegar a la cantidad de datos total
        print(row) #Imprime los datos dentro de la db
      input('\nIngrese enter para continuar...')
      mainMenu()

#MODIFICAMOS LOS PRODUCTOS
  elif opcion == 2:
    print('MODIFICAR PRODUCTOS\n')
    os.system('cls' if os.name == 'nt' else 'clear') #Limpio la pantalla
    mod = input ('Ingrese el nombre del producto: ') #Ingresamos el nombre el producto al que queremos hacerle una modificacion dentro de las exitencias
    exist = db.execute('SELECT nombre_prod,desc_prod,precio_prod,stock FROM inventario WHERE nombre_prod = ' + mod).rowcount #Hacemos un conteo si este existe dentro de la base de datos debolvera un numero y si no devolvera un cero
    #Verificamos si existe la fila, si esta no existe mostrata error
    if exist <= 0:
      print('ERROR! Este producto no existe!')
      input('\nIngrese enter para continuar...')
      mainMenu()
    else:
      x = db.execute('SELECT nombre_prod,desc_prod,precio_prod,stock From inventario Where nombre_prod = ' + mod) #Hacemos un Select de nombre dentro de la tabla inventario
      i = db.execute('SELECT id From inventario Where nombre_prod = ' + mod) #Selecionamos el ID por aparte del mismo producto
      print(x) #Imprimo los datos que tenga en esta tabla
    
      #SUB MENU DE ACTUALIZACION
      print('QUE DECEA ACTUALIZAR')
      print('1. Descuento del producto')
      print('2. Precio del producto')
      print('3. Nombre del producto')
      print('4. Existencias de producto')
      op2 = inputU.inputNumber("\n ➤ ")

      if op2 == 1: #ACTUALIZAR DESCUENTO
        print('ACTUALIZACION DE DESCUENTO\n')
        d = db.execute('SELECT desc_prod From inventario Where nombre_prod = ' + mod) #Buscamos el campo en la tabla usando el nombre ya buscado
        print('El descuento actual es de: ' + d) #Le mencionamos el descuento actual que tiene el producto para que tenga conocimiento de este
        descuento = inputU.inputPositiveNumber #Solicitamos el nuevo descuento que sea un numero positivo
        db.execute('UPDATE inventario SET desc_prod =' + descuento + 'WHERE id = '+ i) #Realizamos la sentencia de actualizacion para este campo con el ID obtenido antes
        print('Cambio realizado con excito!') #Mensaje de confirmacion de cambio
        input('Presione una enter para continuar...') #Le damos una pausa al usuario y volvemos al menu principal
        mainMenu()

      elif op2 == 2: #ACTUALIZAR PRECIO DEL PRODUCTO
        print('ACTUALIZACION DE PRECIO\n')
        p = db.execute('SELECT precio_prod From inventario Where nombre_prod = ' + mod)
        print('El precio actual es de: ' + p) #Le mencionamos el precio actual que tiene el producto para que tenga conocimiento de este
        precio = inputU.inputPositiveNumber #Solicitamos el nuevo precio que sea un numero positivo
        db.execute('UPDATE inventario SET precio_prod =' + precio + 'WHERE id = '+ i) #Realizamos la sentencia de actualizacion para este campo con el ID obtenido antes
        print('Cambio realizado con excito!') #Mensaje de confirmacion de cambio
        input('Presione una enter para continuar...') #Le damos una pausa al usuario y volvemos al menu principal
        mainMenu()

      elif op2 == 3: #ACTUALIZAR NOMBRE DEL PRODUCTO
        print('ACTUALIZACION DE NOMBRE\n')
        n = db.execute('SELECT nombre_prod From inventario Where nombre_prod = ' + mod)
        print('El nombre actual es de: ' + n) #Le mencionamos el nombre actual que tiene el producto para que tenga conocimiento de este
        nombre = inputU.inputRequired #Solicitamos el nuevo nombre
        db.execute('UPDATE inventario SET nombre_prod =' + nombre + 'WHERE id = '+ i) #Realizamos la sentencia de actualizacion para este campo con el ID obtenido antes
        print('Cambio realizado con excito!') #Mensaje de confirmacion de cambio
        input('Presione una enter para continuar...') #Le damos una pausa al usuario y volvemos al menu principal
        mainMenu()

      elif op2 == 4: #ACTUALIZAR EXISTENCIAS
        print('ACTUALIZACION DE EXISTENCIAS\n')
        s = db.execute('SELECT stock From inventario Where nombre_prod = ' + mod)
        print('La existencia actual es de: ' + s) #Le mencionamos la existencia actual que tiene el producto para que tenga conocimiento de este
        existencia = inputU.inputPositiveNumber #Solicitamos la cantidad de existencias nuevas
        db.execute('UPDATE inventario SET stock =' + existencia + 'WHERE id = '+ i) #Realizamos la sentencia de actualizacion para este campo con el ID obtenido antes
        print('Cambio realizado con excito!') #Mensaje de confirmacion de cambio
        input('Presione una enter para continuar...') #Le damos una pausa al usuario y volvemos al menu principal
        mainMenu()

  #CONSULTA DE PRODUCTO
  elif opcion == 3:
    print('CONSULTA DE PODUCTOS\n')
    os.system('cls' if os.name == 'nt' else 'clear') #Limpio la pantalla
    query = input ('Ingrese el nombre del producto: ') #Ingresamos el nombre el producto al que queremos consultar
    #Hacemos un conteo de las filas con ese mismo nombre y si no existe respondera con cero
    exist_c = db.execute('SELECT nombre_prod From inventario Where nombre_prod = '+ query).rowcount
    if exist_c == 0:
      print('ERROR! Este producto no exite!')
      mainMenu()
    else:
      db.execute('SELECT nombre_prod,desc_prod,precio_prod,stock From inventario Where nombre_prod = ' + query)
      rows = db.fetchall() #Se cuentan la cantidad de filas que tenga la tabla
      print('EN EL INVENTARIO ESTA: \n')
      for row in rows: #Se hace un contador que mostrara los datos desde 0 hasta llegar a la cantidad de datos total
        print(row) #Imprime los datos dentro de la db
      input('Presione enter para continuar ...')
    

  # Nos desconectamos de la base de datos
  dbConection.close()

  # REGRESAL AL MENU PRINCIPAL
  mainMenu()