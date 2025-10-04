import re

def validar_contrasena(password):
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(patron, password) is not None

contrasenas = [
    "Hola123!",     
    "password",     
    "Segura@2025",  
    "12345678",     
    "Clave#Fuerte1" 
]

for c in contrasenas:
    print(f"{c}: {'Válida' if validar_contrasena(c) else 'Inválida'}")