from ahorcado import Ahorcado


class Menu:
    def menu(self):

        while True:

            print('BIENVENIDO A AHORCADO')

            print('Elija una opción:')

            print('1: Un jugador')

            print('2: Dos jugador')

            try:
                opcion = int(input('>'))

            except ValueError:
                print("No se aceptan letras")

            if opcion > 0 and opcion < 3:

                if opcion == 1:
                    print('Juega uno')
                    Ahorcado.un_jugador_nuevo(self)

                if opcion == 2:
                    print('Juegan dos')
                    Ahorcado.dos_jugadores_nuevos(self)


if __name__ == '__main__':
    a = Menu()
    a.menu()
