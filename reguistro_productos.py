
import json


def menu(localtime):
            print("""
        ===========================================
        ============= Menu Bancario ===============
        =                                         =
        =   1. Registrar un producto             =
        =   2. ingresar producto al inventadio    =
        =   3. Retirar producto del inventadio    =
        =   4. Bucar un producto                  =
        =   5. Historial de productos             =
        =   6. Informe                            =
        =   6. Salir                              =
        =                                         =
        ===========================================
             """)

#==========================================================
#==========================================================
#|                REGISTRO DE PRODUCTOS                   |
#==========================================================

def creacion():
  
  # try:
    producto ={
      "cod": input("cod = " ),
      "name": input("nombre = "),
      "proveedor": input("proveedor = "),
      "cantidad": 0,
        }

    inventario = None
    try:
      file = open('inventario.json', 'r')
      inventario = json.load(file)
      file.close
    except Exception as error:
         inventario = []
    inventario.append(producto)
    file = open('inventario.json', 'w')
    json.dump(inventario,file,indent=4)
    file.close

#==========================================================

#==========================================================
#|                INGRESO DE PRODUCTOS                    |
#==========================================================

def ingreso(productos,localtime):

  stock = None
  try:
    file = open('inventario.json', 'r')
    inventario = json.load(file)
    file.close
  except Exception as error:
          stock = []
  print("ingrese el cod")
  cod = int(input("ingrese el codigo del producto = "))

  for producto in inventario:
      if producto["cod"] == cod:
        print("indique la bodega a la cual desea ingresar nuevas existencias")
        ing = input("""
          ____________________
        |                    |
        | (1) Bodega Norte   |
        | (2) Bodega Centro  |
        | (3) Bodega Centro  |
        |____________________|

        """)

        if ing == "1" or ing == "2" or ing == "3":
          if ing == "1":
              bodega = "Bodega Norte"
          elif ing == "2":
              bodega = "Bodega Centro"
          elif ing == "3":
              bodega = "Bodega Centro"
          try:
            producto["bodega"] = bodega
            print(f"El porducto al cual va a adicionar stock es {producto['name']} se van a agredar existencias a la {bodega}")
            cantidad = int(input("indique la cantidad que desea agregar = "))
          except ValueError:print("Codido de producto errado")
  #====================================================================================

        elif productos["cantidad"] <= 0:
          print("no se puede ingresar cantidades negativas")
          break

  #====================================================================================

      producto["cantidad"] += cantidad
      for producto in inventario:
          if 


#==========================================================
#==========================================================
#|                RETIRO DE PRODUCTOS                     |
#==========================================================
# solicitar codigo de progusto y bodega donde se encuentra
# monto a retirar
# no se puede retirar si no cuenta con las exitencias
# descripccion de retiro

def retiro_productos(productos, producto):
  print("ingrese el codigo del producto que desea retirar")
  cod = input("=>  ")
  bodega = print("ingrese la bodega en la cual se encuentra el producto")
  input("=>  ")

  for producto in productos:
    if producto["cod"] == cod and producto["bodega"] == bodega:
      print(f"El producto que va a retirara es {producto['name']}, el cual se encuentra en la {producto['bodega']}")