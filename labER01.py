""" Validacion de correos """
# En esta practica validamos correos de un archivo txt

import re # Imortamos la libreria de las expresiones regulares
import matplotlib.pyplot as plt # Importamos la libreria para las graficas

patron = r'^\d+\.\s*[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # Expresion regular

validos = 0 # Contador de validos
invalidos = 0 # Contador de invalidos

with open("correos.txt", "r") as f: # El archivo a leer
    for linea in f:
        correo = linea.strip()
        if correo:  # Ignorar líneas vacías
            if re.match(patron, correo):
                validos += 1
            else:
                invalidos += 1

print(f"Correos válidos: {validos}") # Imprime los correos validos
print(f"Correos inválidos: {invalidos}") # Imprime los correos invalidos

plt.bar(['Válidos', 'Inválidos'], [validos, invalidos]) # Generamos la grafica de validos e invalidos
plt.show() # Mostramos la grafica