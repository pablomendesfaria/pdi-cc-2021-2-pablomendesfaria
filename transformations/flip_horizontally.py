"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
import numpy as np


<<<<<<< HEAD
def flip(parent, ui_function, pixels):
    """
    Espalha a imagem horizontalmente e retorna os pixels da imagem para a classe MainWindow
    :param ui_function:
=======
def flip(parent, pixels):
    """
    Espalha a imagem horizontalmente e retorna os pixels da imagem para a classe MainWindow
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels = np.fliplr(pixels)

<<<<<<< HEAD
    ui_function.set_image(parent, pixels, False, True)
=======
    parent.set_image(pixels, has_filter=True)
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
