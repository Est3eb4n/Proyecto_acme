
import json

#==========================================================
#==========================================================
#==========================================================

new_stock = open('inventario.json', 'a')

productos = {
    "cod": input("cod = " ),
    "name": input("nombre = "),
    "bodega": input("proveedor = "),
    "cantidad":[],
  }

  
things = json.dumps(productos)
new_stock.write('\n')
new_stock.write(things) 
 
#==========================================================

#==========================================================
#==========================================================

def ingreso(productos, cantidad, cod, localtime):
  print("Desea agregar mas productos?")
  rta = input("s/n")
  for agregar in productos:
    if rta == "s":
      cod = input("ingres el codgo del producto")
      if productos["cod"] == cod:
         print(f"El porducto al cual va a adicionar stock es {productos['name']} y se encuentra ubicado en la bodega {productos['bodega']}")
         cantidad = int(input("indique la cantidad que desea agregar "))
#====================================================================================
      # if productos["cantidad"] < cantidad:
      #   print("no posee las existencias necesarias para retidar")
      #   break
      elif productos["cantidad"] <= 0:
        print("no se puede ingresar cantidades negativas")
        break
#====================================================================================
    productos["cantidad"] += cantidad
    for cantidades in cantidad:
      if productos["cod"] == cantidades["cod"]:
        cantidades["cantidad"].append({
          "tipo": "adicion",
          "proveedor": f"la bodega a la que entro el producto es {'proveedor'}",
          "descripccion": f"se han agregado {'cantidad'} al producto {'name'}",
          # "cantidad": "",
          "fecha": f"{localtime()}",
        })
    print(cantidades)
#==========================================================