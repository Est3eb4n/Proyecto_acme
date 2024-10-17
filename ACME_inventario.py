from menu import*
from reguistro_productos import productos
from reguistro_productos import ingreso


from time import asctime
producto = []
cantidad = []
cod = []


while True:
    
    print("""
        Bienvenido a ACME SAS
          
        Porfavor escoja una de la siguientes opcciones
        """)
    menu(asctime)
    opc = input("opc")

    if opc == "1":
         productos
    elif opc == "2":
        ingreso(productos, cantidad, cod, asctime)