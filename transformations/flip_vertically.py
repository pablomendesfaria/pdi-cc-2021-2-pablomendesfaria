"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
import numpy as np


def flip(parent, ui_function, pixels):
    """
    Espalha a imagem verticalmente e retorna os pixels da imagem para a classe MainWindow
    :param ui_function:
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels = np.flipud(pixels)

    ui_function.set_image(parent, pixels, False, True)
