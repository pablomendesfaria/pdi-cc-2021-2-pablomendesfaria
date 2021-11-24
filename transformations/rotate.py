"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
import numpy as np


def rotate(parent, pixels):
    """
    Rotaciona a imagem em 270º (90° pra direita) e retorna os pixels da imagem para a classe MainWindow
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels = np.rot90(pixels)

    parent.set_image(pixels, has_filter=True)
