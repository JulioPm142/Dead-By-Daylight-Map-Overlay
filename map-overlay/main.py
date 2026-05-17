import sys
from PySide6.QtWidgets import QApplication
from printar import capturar_tela
from read import ler_texto_da_imagem
from overlay import MeuOverlay

def main():
    print("=== Iniciando Aplicação Principal ===")
    
    # 1. Tira o print da tela
    caminho_da_foto = 'maps/temp1.png'
    imagem_gerada = capturar_tela(caminho_da_foto)
    
    # 2. Lê o texto da imagem (OCR)
    texto_detectado = ler_texto_da_imagem(imagem_gerada)
    print(f"\n[OCR] Texto detectado: '{texto_detectado}'")
    
    # 3. Inicializa o ambiente gráfico do PySide6
    # O Qt exige que o QApplication seja criado antes de qualquer janela
    app = QApplication(sys.argv)
    
    # Se o OCR detectou algo, passamos o texto como nome da imagem.
    # Caso contrário, ele vai abrir vazio ou com a imagem padrão.
    if texto_detectado:
        print(f"[Main] Abrindo overlay para o mapa: {texto_detectado}")
        overlay = MeuOverlay(nome_da_imagem=texto_detectado)
    else:
        print("[Main] Nenhum texto detectado. Abrindo overlay padrão.")
        overlay = MeuOverlay() # Abre o padrão definido no código anterior
        
    overlay.show()
    
    # Inicia o loop do PySide6 (trava o script aqui até você apertar F9)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()