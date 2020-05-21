# Importamos las librerias necesarias para el modulo
import os
import sqlite3

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
  input('Modulo del cliente, precione enter para continuar...')
  '''
    Codigo del modulo
  '''


  # Nos desconectamos de la base de datos
  dbConection.close()

  # REGRESAL AL MENU PRINCIPAL
  mainMenu()