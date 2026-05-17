import mss

def capturar_tela(caminho_saida='temp.png'):
    with mss.mss() as sct:
        # Capture the first monitor
        
        small_region = {'left': 700, 'top': 850, 'width': 520, 'height': 48}
        screenshot = sct.grab(small_region)

        # Save to file
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=caminho_saida)

    print(f"[Print] Screen Saved at: {caminho_saida}")
    return caminho_saida


