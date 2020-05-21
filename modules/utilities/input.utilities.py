# Funcion que solo permite ingresar numeros
def inputNumber(mensaje = 'Ingresa un número:', error = 'Error: Tienes que ingresar un numero entero'):
  while True:
    try:
      x = int(input(mensaje))
    except ValueError:
      print("\n" + error + "\n")
      continue
    else:
      return x

# Funcion que verifica si se ingreso almenos 1 caracter por teclado
def inputRequired(mensaje = 'Ingresa almenos 1 caracter:', error = 'Error: Tienes que ingresar almenos 1 carácter'):
  while True:
    x = input(mensaje)
    if len(x) < 1:
        print("\n" + error + "\n")
    else:
        break
  return x

# Funcion que solo permite el ingreso de numeros positivos
def inputPositiveNumber(mensaje = 'Ingresa un número positivo:', error = 'Error: El número ingresado tiene que ser positivo'):
  while True:
    x = inputNumber(mensaje)
    if x < 0:
        print("\n" + error + "\n")
    else:
        break
  return x

# Funcion que solo permite el ingreso de numeros mayores a x numero
def inputHigherOrEqualNumber(higherOrEqualThan, mensaje = 'default', error = 'default'):

  if mensaje == 'default':
    mensaje = 'Ingresa un numero mayor a' + higherOrEqualThan + ':'

  if error == 'default':
    error = 'Error: El número ingresado debe ser mayor o igual a ' + higherOrEqualThan

  while True:
    x = inputNumber(mensaje)
    if x < higherOrEqualThan:
        print('\n',error,'\n')
    else:
        break
  return x
