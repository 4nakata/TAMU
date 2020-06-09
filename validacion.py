import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import re
import colores

from compañias import att
from compañias import desconocido
from compañias import movistar
from compañias import telcel
from compañias import unefon


def comprobarEstructuraNumero(numero):
	return re.match(r'[0-9]{10}$', numero)


def comprobarCompañia(numero):

	_telcel = telcel.telcel(numero)
	if _telcel.registrado:
		return _telcel

	_att = att.att(numero)
	if _att.registrado:
		return _att

	_movistar = movistar.movistar(numero)
	if _movistar.registrado:
		return _movistar

	_unefon = unefon.unefon(numero)
	if _unefon.registrado:
		return _unefon

	return desconocido.desconocido(numero)


def leerContraseñas(_msj=""):

	if _msj != "":
		colores.textError(_msj)
	
	_archivo = colores.inputBold(' ¿ Cual es el nombre del diccionario ? : ')
	
	if not os.path.exists(_archivo):
		leerContraseñas("El archivo no existe")

	_f = open(_archivo, "r")
	_contraseñas = _f.readlines()
	_f.close()
	
	return _contraseñas
