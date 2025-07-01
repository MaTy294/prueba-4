ntrada = {}

def comprarEntrada():
    nombre = input("Ingrese su nombre: ")
    if nombre == "":
        print("El nombre no puede estar en blanco")
        return
    tipo = input("Ingrese el tipo de entrada (G/V): ").upper()
    if tipo not in ["G", "V"]:
        print("Tipo de entrada inválido")
        return
    codigo = input("Ingrese el código de confirmación: ")
    if len(codigo) < 6:
        print("El código debe tener mínimo 6 caracteres")
        return
    entrada[nombre] = {"tipo": tipo, "codigo": codigo}
    print("Entrada registrada con éxito")

def consultarComprador():
    nombre = input("Ingrese el nombre del comprador: ")
    if nombre in entrada:
        print("Tipo de entrada:", entrada[nombre]["tipoo"]) 
        print("Código de confirmación:", entrada[nombre]["codigo"])
    else:
        print("El comprador no se encuentra")

def cancelarCompra():
    nombre = input("Ingrese el nombre del comprador: ")
    if nombre in entrada:
        del entrada[nombre]
        print("Compra cancelada")
    else:
        print("No se pudo cancelar la compra")

def menu():
    while True:
        print("\nMENU PRINCIPAL")
        print("1.- Comprar entrada.")
        print("2.- Consultar comprador.")
        print("3.- Cancelar compra.")
        print("4.- Salir.")
        op = input("Escoja la opción que desea: ")
        if op == "1":
            comprarEntrada()
        elif op == "2":
            consultarComprador()
        elif op == "3":
            cancelarCompra()
        elif op == "4":
            print("Adiós!!")
            break
        else:
            print("Opción no válida")

menu()
