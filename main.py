from ClaseGestorConjunto import GestorConjunto

def test(gestor):
    c1 = input("Ingrese su conjunto separado por ; Para salir, ingrese FIN\n").upper()
    while c1 != "FIN":
        c2 = input("Ingrese el otro conjunto separado por ;\n")
        if gestor.crearConjuntos(c1, c2):
            gestor.operaciones()
        c1 = input("Ingrese su conjunto separado por ; Para salir, ingrese FIN\n").upper()



if __name__ == '__main__':
    gestor = GestorConjunto()
    test(gestor)
