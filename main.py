import colores
import sys
import validacion
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def banner():
    clear()
    print(
        """
\033[1;33m
    \t\t ████████╗ █████╗ ███╗   ███╗██╗   ██╗
    \t\t ╚══██╔══╝██╔══██╗████╗ ████║██║   ██║
    \t\t    ██║   ███████║██╔████╔██║██║   ██║
    \t\t    ██║   ██╔══██║██║╚██╔╝██║██║   ██║
    \t\t    ██║   ██║  ██║██║ ╚═╝ ██║╚██████╔╝
    \t\t    ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝   \033[0;m \n

    Identifica la compañia de un número telefonico
    y si es posible realizar un ataque de diccionario
    
    Compañias soportadas : \033[1;33m ["Telcel","Att", "Movistar", "Unefon"] \033[0;m

    \033[1;33m @4nakata\033[0;m

============================================================================
    """)


def main(_numero):
    _celular = validacion.comprobarCompañia(_numero)

    colores.textBold(" Número : " + _celular.numero)
    colores.textBold(" Nombre de Compañia : " + _celular.compañia)
    colores.textBold(" ¿ Registado en la plataforma de la compañia ? : " + str(_celular.registradoWeb))
    colores.hr()

    if _celular.registradoWeb:

        colores.textPrimario(" >>> Confirmar ataque")
        _confirmarAtaque = colores.inputBold('  Se puede realizar un ataque de diccionario, ¿Quieres intentarlo? (s/n) : ')
        colores.hr()

        if _confirmarAtaque == 's' or _confirmarAtaque == 'S':
            _celular.ataqueDiccionario()

        else:
            colores.textError(" >>> Ataque no ejecutado \n")
            exit()

    else:
        colores.textError(' Con base en la "euristica" ( 3 ifs ) de este poderoso script')
        colores.textError(' Es imposible realizar un ataque de diccionario en su portal')
        colores.hr()
        exit()


if __name__ == "__main__":
    banner()

    if len(sys.argv) <= 1:
        colores.textError(" Debes de pasar como parametro el número celular con un formato de 10 digito")
        colores.textError("	Ejemplo : python3" + sys.argv[0] + " 5511223344")
        colores.hr()
        exit()

    else:
        _check = validacion.comprobarEstructuraNumero(sys.argv[1])

        if _check:
            main(sys.argv[1])

        else:
            colores.textError(" Debes de pasar como parametro el número celular con un formato de 10 digito")
            colores.textError("	Ejemplo : python3" + sys.argv[0] + " 5511223344")
            colores.hr()
            exit()
