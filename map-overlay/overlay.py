import sys
import os
from PySide6.QtCore import Qt, QTimer, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QRegion, QPixmap
import keyboard

class MeuOverlay(QWidget):
    sinal_fechar = Signal()

    # Adicionamos 'nome_da_imagem' como parâmetro do __init__
    def __init__(self, nome_da_imagem=None):
        super().__init__()

        pasta_do_script = os.path.dirname(os.path.abspath(__file__))

        # Se o OCR encontrar um texto, usamos ele + .png, senão usamos uma imagem padrão

        caminho_absoluto_imagem = os.path.join(pasta_do_script, "maps", nome_da_imagem + ".png")
        print(f"[Overlay] Tentando carregar: {caminho_absoluto_imagem}")
        
        pixmap = QPixmap(caminho_absoluto_imagem)

        # Flags da Janela
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        
        # REMOVIDO: self.setMask(QRegion(0, 0, 0, 0)) -> Isso torna a janela 100% invisível/clicável.
        # Deixamos apenas o TranslucentBackground para que a imagem apareça com fundo transparente.

        self.setGeometry(100, 100, 500, 400)

        # Layout e Elementos Visuais
        layout = QVBoxLayout()
        self.label_imagem = QLabel(self)
       
        if not pixmap.isNull():
            pixmap_redimensionado = pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.label_imagem.setPixmap(pixmap_redimensionado)
        else:
            # Caso a imagem não exista na pasta maps, avisa na tela
            self.label_imagem.setText(f"Imagem não encontrada:\n{nome_da_imagem}")
            self.label_imagem.setStyleSheet("color: red; font-size: 16px; font-weight: bold;")

        self.label_imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_imagem)
        self.setLayout(layout)

        # Atalho com Sinais
        self.sinal_fechar.connect(self.fechar_overlay_seguro)
        keyboard.add_hotkey('f9', lambda: self.sinal_fechar.emit())

        # Mantém o Ctrl+C ativo no prompt
        self.timer_terminal = QTimer()
        self.timer_terminal.timeout.connect(lambda: None)
        self.timer_terminal.start(100)

    @Slot()
    def fechar_overlay_seguro(self):
        print("\nFechando o overlay com segurança...")
        keyboard.unhook_all()
        self.close()
        QApplication.quit()

# Este bloco só roda se você executar o overlay.py sozinho para testar
if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = MeuOverlay()
    overlay.show()
    sys.exit(app.exec())