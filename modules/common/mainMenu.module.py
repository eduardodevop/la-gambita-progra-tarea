# Importamos las librerias necesarias para el archivo main.py
import os
import importlib.machinery

# Importamos las utilidades necesarias para el archivo main.py
loader = importlib.machinery.SourceFileLoader('inputU', './modules/utilities/input.utilities.py')
inputU = loader.load_module('inputU')

# Importamos los modulos del programa
loader = importlib.machinery.SourceFileLoader('facturacion', './modules/core/facturacion/facturacion.module.py')
facturacion = loader.load_module('facturacion')
loader = importlib.machinery.SourceFileLoader('inventario', './modules/core/inventario/inventario.module.py')
inventario = loader.load_module('inventario')
loader = importlib.machinery.SourceFileLoader('cliente', './modules/core/cliente/cliente.module.py')
cliente = loader.load_module('cliente')
loader = importlib.machinery.SourceFileLoader('compra', './modules/core/compra/compra.module.py')
compra = loader.load_module('compra')
loader = importlib.machinery.SourceFileLoader('venta', './modules/core/venta/venta.module.py')
venta = loader.load_module('venta')

# Definicion del menu principal
def drawMenu(titulo = '+++ Seleccione una opción del menú +++'):
  # Usamos cls para borrar la terminal en windows o clear para linux
  os.system('cls' if os.name == 'nt' else 'clear')

  print('Marisqueria "La Gambita" (*^_^*)', '\n')
  print(titulo, '\n')
  print('1. Modulo de clientes')
  print('2. Modulo de ventas')
  print('3. Modulo de facturacion')
  print('4. Modulo de compras')
  print('5. Modulo de inventario')
  print('6. Salir')

  opcion = inputU.inputNumber("\n-> ")

  # Llamamos a la funcion correcta para cada opcion del menu
  if opcion == 1:
    cliente.mainFunction(drawMenu)
  elif opcion == 2:
    venta.mainFunction(drawMenu)
  elif opcion == 3:
    facturacion.mainFunction(drawMenu)
  elif opcion == 4:
    compra.mainFunction(drawMenu)
  elif opcion == 5:
    inventario.mainFunction(drawMenu)

  elif opcion == 6:
    # Usamos cls para borrar la terminal en windows o clear para linux
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-> Saliendo del programa <-")

  else:
    # Si no se ingreso un valor valido entonces regresamos al usuario al menu con un mensaje de error
    drawMenu(titulo = '+++ Error: Opción no valida\t\t+++\n+++ Seleccione una opción del menú\t+++')

