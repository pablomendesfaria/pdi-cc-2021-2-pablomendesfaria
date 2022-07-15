"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
from PIL import (Image, ImageFilter)


def apply_filter(parent, ui_function, pixels):
    """
    Aplica o filtro Find Edge Weak a partir de um kernel pre estabelecido e retorna os pixels da imagem para a classe
    MainWindow
    :param ui_function:
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """
    kernel = ImageFilter.Kernel((3, 3), (1, 0, -1, 0, 0, 0, -1, 0, 1), 1)
    img = Image.fromarray(pixels)
    img2 = img.filter(kernel)
    ui_function.set_image(parent, img2, True, True)
