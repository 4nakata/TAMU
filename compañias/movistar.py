import colores
import requests
import json


class movistar:
    
    def __init__(self, numero):
        self.numero = numero
        self.compañia = "Movistar"
        self.registrado = False
        self.registradoWeb = False
        self.comprobarNumero()
          

    def comprobarNumero(self):
        
        _response = requests.get('https://mi.movistar.com.mx/registro?p_p_id=mx_movistar_ecare_register_web_portlet_RegisterPortlet_INSTANCE_YVQUt4lb7C9W&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=%2Fuser%2Fregister&p_p_cacheability=cacheLevelPage&_mx_movistar_ecare_register_web_portlet_RegisterPortlet_INSTANCE_YVQUt4lb7C9W_msisdn='+self.numero)
        self.validaResponse(_response.text)

    def validaResponse(self, data): 

        try:
            data = json.loads(data)
            
        except Exception as e:
            self.registradoWeb = False
            self.registrado = False    

        else:
            
            if '404' in data["code"]:
                self.registradoWeb = True
                self.registrado = True
                
            elif '200' in data["code"]:
                self.registradoWeb = False
                self.registrado = True
            
            elif '422' in data["code"]:
                self.registradoWeb = False
                self.registrado = False

            else:
                self.registradoWeb = False
                self.registrado = False

    def ataqueDiccionario(self):

        colores.textPrimario(" >>> Tranquilo vaquero  ")
        colores.textError(" Movistar tiene una extraña y/o segura forma de validar el inicio de sesión ")
        colores.textError(" [ cookies, parametros, sesiones, valores aleatorios ] ")
        colores.textPrimario("     Es mucho más fácil utilizar burpsuit para el ataque ;)")
        colores.hr()
        exit()
