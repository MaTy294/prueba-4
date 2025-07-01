entrada = {}

def comprarEntrada():
    nombre = input("ingrese su nombre")
    if nombre == "":
        print("el nombre no puede estar en blanco")
        return
    tipoEntrada = input("ingrese el tipo de entrada (G/V)").upper()
    if tipoEntrada not in ["G", "V"]:
        print("tipo de entrada invalido")
        return
    codigo = input("ingrese el codigo de confirmacion")
    if len(codigo) < 6:
        print("el codigo debe tener minimo 6 caracteres")
        return
    entrada[nombre] = {"tipo": tipoEntrada, "codigo": codigo}
    print("Entrada registrada con exito")

def consultarComprador():
    nombre = input("ingrese el nombre del comprador")
    if nombre in entrada:
        datos = entrada[nombre]
        print("Tipo de entrada:", datos["tipo"])
        print("Código de confirmación:", datos["codigo"])
    else:
        print("El comprador no se encuentra")

def cancelarCompra():
    nombre = input("ingrese el nombre del comprador")
    if nombre in entrada:
        del entrada[nombre]
        print("compra cancelada")
    else:
        print("no se pudo cancelar la compra")

def menu():
    while True:
        print("MENU PRINCIPAL")
        print("1.- Comprar entrada.")
        print("2.- Consultar comprador.")
        print("3.- Cancelar compra.")
        print("4.- Salir.")
        op = input("escoja la opcion que desea")
        if op == "1":
            comprarEntrada()
        elif op == "2":
            consultarComprador()
        elif op == "3":
            cancelarCompra()
        elif op == "4":
            print("Adios!!")
            break
        else:
            print("opcion no valida")

menu()
