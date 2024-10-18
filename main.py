from reguistro_productos import menu
from reguistro_productos import creacion
from reguistro_productos import ingreso
from reguistro_productos import retiro_productos
from reguistro_productos import buscar
from time import asctime



while True:

    print("""
        Bienvenido a ACME SAS

        Porfavor escoja una de la siguientes opcciones
        """)
    menu()
    opc = input(" => ")

    if opc == "1":
        creacion()
    elif opc == "2":
        ingreso()
    elif opc == "3":
        retiro_productos()
    elif opc == "4":
        buscar()