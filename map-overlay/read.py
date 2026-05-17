import easyocr
import unicodedata
import re

# Inicializa o leitor nos idiomas desejados (ex: português e inglês)
reader = easyocr.Reader(['pt', 'en'],gpu=True)

# Lê a imagem diretamente pelo caminho do arquivo

def ler_texto_da_imagem(caminho_imagem):
    resultado = reader.readtext(caminho_imagem, detail=0)

    texto_completo=''

    # O resultado vem como uma lista de strings
    for linha in resultado:
        print(linha)
        texto_completo+= linha
        

    texto_completo = texto_completo.lower()
    texto_completo = texto_completo.replace(" ", "")
    texto_normalizado = unicodedata.normalize('NFD', texto_completo)
    texto_sem_acentos = "".join(ch for ch in texto_normalizado if unicodedata.category(ch) != 'Mn')
    texto_limpo = re.sub(r'[^a-z]', '', texto_sem_acentos)

    return texto_limpo