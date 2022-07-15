"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
import numpy as np


<<<<<<< HEAD
def rotate(parent, ui_function, pixels):
    """
    Rotaciona a imagem em 270º (90° pra direita) e retorna os pixels da imagem para a classe MainWindow
    :param ui_function: classe que contem as funções do app
=======
def rotate(parent, pixels):
    """
    Rotaciona a imagem em 270º (90° pra direita) e retorna os pixels da imagem para a classe MainWindow
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels = np.rot90(pixels)

<<<<<<< HEAD
    ui_function.set_image(parent, pixels, False, True)
=======
    parent.set_image(pixels, has_filter=True)
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
