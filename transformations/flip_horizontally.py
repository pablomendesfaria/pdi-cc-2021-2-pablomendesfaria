"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
import numpy as np


def flip(parent, pixels):
    """
    Espalha a imagem horizontalmente e retorna os pixels da imagem para a classe MainWindow
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels = np.fliplr(pixels)

    parent.set_image(pixels, has_filter=True)
