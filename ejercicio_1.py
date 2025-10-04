""" Validacion de correro """
# Este programa valida correos electronicos

import re # Importamos la libreria de expresiones regulares

def validar_correo(correo): # Definimos una variable
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # Esta es la expresion que utilizamos para validar el correo
    return re.match(patron, correo) is not None # Envia un return si el correo coincide con el patron y falso si no es asi

correos = [ # Hacemos pruebas de validacion
    "usuario@gmail.com",
    "nombre.apellido@yahoo.com",
    "correo123@dominio.mx",
    "correo-invalido@",
    "otro@dominio"]

for c in correos:
    print(f"{c}: {'Válido' if validar_correo(c) else 'Inválido'}") # Este es el print que marca si el correo es o no valido