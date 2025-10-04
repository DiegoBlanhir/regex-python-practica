import re

def extraer_urls(texto):
    patron = r'(https?://[^\s]+)'
    return re.findall(patron, texto)

def extraer_dominios(urls):
    patron = r'https?://([^/]+)'
    return [re.match(patron, url).group(1) for url in urls]

texto = """
Visita https://www.google.com para buscar,
o entra a http://example.org/test. 
También https://openai.com/research es útil.
"""

urls = extraer_urls(texto)
dominios = extraer_dominios(urls)

print("URLs encontradas:", urls)
print("Dominios encontrados:", dominios)