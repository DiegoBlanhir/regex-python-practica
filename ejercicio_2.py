""" Extraer telefonos de un texto """
# En este ejercicio se extraen numeros de telefonos de 10 digitos de un texto, puede llevar solo los digitos, guiones u otros caracteres

import re # Extraemos la lbreria de las expresiones regulares

def extraer_telefonos(texto): # Definimos la variable
    patron = r'(\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4})' # Definimos el patron de la expresion
    return re.findall(patron, texto) # 

texto = """
Llámanos al (123) 456-7890 o al 123-456-7890.
También puedes marcar 9876543210 o (555)123-4567.
"""

telefonos = extraer_telefonos(texto)
print("Teléfonos encontrados:")
for t in telefonos:
    print(t)