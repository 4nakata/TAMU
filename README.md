# TAMU

Script que identifica la compañia de un número telefonico (México) y si es posible realizar un ataque de diccionario contra el portal de la compañia. Útil para un ataque de ingenieria social dirigido o solo para recolectar más información del target.

Compañias soportadas:
  - Telcel
  - ATT
  - Movistar
  - Unefon

Requistos:
  - Python 3.X
  - Requests

Uso:
  - python3 main.py 5511223344

Notas:
  * ATT y Unefon son extremedamente inestables por lo que no fue viable utilizar multi-threads.
  ** Python 2 NO es funcional
