"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
from PIL import (Image, ImageFilter)


def apply_filter(parent, ui_function, pixels):
    """
    Aplica o filtro Edge Enhance More na imagem usando a biblioteca PIL e retorna os pixels da imagem para a classe
    MainWindow
    :param ui_function:
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """
    img = Image.fromarray(pixels)
    img2 = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    ui_function.set_image(parent, img2, True, True)
