from Menu import Menu
if __name__ == "__main__":
    menu= Menu()
    ban = True
    user = (input("Ingrese el usuario (Director/Tesorero) - (FIN para terminar): ")).lower()
    while ban is True:
        c = input("Ingrese la contraseña: ")
        if user== "tesorero" and c == "uTesoreso/ag@74ck":
            menu.MenuTesorero(user)
        elif user == "director" and c== "uDirector/ufC77#!1":
            menu.MenuDirector(user)
        else:
            print("Contraseña y/o Usuario incorrecto")
        usuario = input("Ingrese el usuario (Director/Tesorero) - (FIN para terminar): ")
        if usuario.lower() == "fin":
            ban = False