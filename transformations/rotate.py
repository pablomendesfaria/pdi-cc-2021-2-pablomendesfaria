"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
import numpy as np


def rotate(parent, ui_function, pixels):
    """
    Rotaciona a imagem em 270º (90° pra direita) e retorna os pixels da imagem para a classe MainWindow
    :param ui_function: classe que contem as funções do app
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels = np.rot90(pixels)

    ui_function.set_image(parent, pixels, False, True)
