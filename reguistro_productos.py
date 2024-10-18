
import json


def menu():
            print("""
        ===========================================
        ============ Menu inventario ==============
        =                                         =
        =   1. Registrar un producto              =
        =   2. ingresar producto al inventario    =
        =   3. Retirar producto del inventario    =
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

def ingreso():

  stock = None
  try:
    file = open('inventario.json', 'r')
    stock = json.load(file)
    file.close
  except Exception as error:
          stock = []
  cod = input("ingrese el codigo del producto = ")
  for producto in stock:
    if producto['cod'] == cod:
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
              bodega = "norte"
          elif ing == "2":
              bodega = "centro"
          elif ing == "3":
              bodega = "centro"
          try:
            producto["bodega"] = bodega
            print(f"El porducto al cual va a adicionar stock es {producto['name']} se van a agredar existencias a la {bodega}")
            agregar = int(input("indique la cantidad que desea agregar = "))
          except ValueError:print("Codido de producto errado")
          producto["cantidad"] += agregar
        for entrada in stock:
            if entrada["cantidad"] == producto["cantidad"]:
              movimiento ={
                "tipo": "Ingreso de mercansia",
                "descripccio": f"Se agregaron {producto['cantidad']} kg de {producto['name']}",
                "bodega":[bodega],
                # "fecha": f"{localtime()}",
              }
              print(movimiento)
  file = open('stock.json', 'w')
  json.dump(stock,file,indent=4)
  file.close

#==========================================================
#==========================================================
#|                RETIRO DE PRODUCTOS                     |
#==========================================================
# solicitar codigo de progusto y bodega donde se encuentra
# monto a retirar
# no se puede retirar si no cuenta con las exitencias
# descripccion de retiro

def retiro_productos():
  stock = None
  try:
    file = open('invetario.json', 'r')
    salida_productos = json.load(file)
    file.close
  except Exception as error:
          salida_productos = []

  print("ingrese el codigo del producto que desea retirar")
  cod = input("=>  ")
  bodega = print("ingrese la bodega en la cual se encuentra el producto")
  input("=>  "); 

  for producto in salida_productos:
    if producto["cod"] == cod or producto["bodega"] == bodega:
      print(f"El producto que va a retirara es {producto['name']}, el cual se encuentra en la bodega {producto['bodega']}")
      try:
          agregar = int(input("indique la cantidad que desea retirar = "))
      except ValueError:print("Codido de producto errado")
      producto["cantidad"] -= agregar
      for salida in salida_productos:
            if salida["cantidad"] == salida["cantidad"]:
              movimiento ={
                "tipo": "retiro de mercansia",
                "descripccio": f"Se retiro {agregar} kg de {producto['name']}",
                # "fecha": f"{localtime()}",
              }
              print(movimiento)
  salida_productos.append(producto)
  file = open('stock.json', 'w')
  json.dump(salida_productos,file,indent=4)
  file.close

#==========================================================
#|                 BUCAR DE PRODUCTOS                     |
#==========================================================

def buscar():
  # try:
    file = open('stock.json')
    busqueda = json.load(file)
    file.close
  # except Exception as error:
  #   buscar_productos = [] 
      
    cod = input("Ingrese el codigo del producto que desea consultar = ")
    for encontrado in busqueda:
      if encontrado["cod"] == cod:
        print(f"El codigo del producto es = {encontrado['cod']}")
        print(f"El producto consultado es = {encontrado['name']}")
        print(f"El proveedor es = {encontrado['proveedor']}")
        print(" ")
        print(f"{'CANTIDAD':<12}",f"{'BODEGA':<12}")
        print(f"{encontrado['cantidad']:<12}",f"{encontrado['bodega']:<12}")              
#==========================================================
#|                 BUCAR DE PRODUCTOS                     |
#==========================================================

print("""
  bodeda [1]
""")
# print(f"{producto[cod]: <12}**")