import re
from datetime import datetime

def extraer_fechas(texto):
    patron = r'(\d{2}[/-]\d{2}[/-]\d{4}|\d{4}[/-]\d{2}[/-]\d{2})'
    return re.findall(patron, texto)

def formatear_fecha(fecha):
    for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(fecha, fmt).strftime("%d-%m-%Y")
        except ValueError:
            pass
    return None

texto = """
Eventos importantes:
- Nacimiento: 25/12/2000
- Graduación: 2005-07-15
- Trabajo: 01-01-2015
"""

fechas = extraer_fechas(texto)
print("Fechas encontradas:", fechas)

print("\nFechas formateadas (DD-MM-YYYY):")
for f in fechas:
    print(f, "=>", formatear_fecha(f))