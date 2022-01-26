class Menu:
    def __init__(self):
        pass

    def menu_principal(self,opciones_edd,titulo_edd):
        print("*"*10,titulo_edd,"*"*10)
        for opcion_edd in opciones_edd:
            print(opcion_edd)
        print("*"*10,"*"*(len(titulo_edd)),"*"*10)
        opc_edd = input("Elija una de las opciones[1 - {}]: ".format(len(opciones_edd)))
        return opc_edd
