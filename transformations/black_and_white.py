"""
Black and White Filter
"""
import numpy as np


def apply_filter(parent, ui_function, pixels):

    """
    Transforma a imagem colorida em preto e branco, ela percorre cada pixel da imagem e verifica se
    a media média dos valores RGB do pixel é menor ou maior do que 128, caso seja menor o pixel RGB
    em questão recebe 0, caso seja maior recebe 255, caso o pixel seja 128 continua 128, depois o
    metodo retorna os pixels modificados para a classe MainWindow
    :param ui_function:
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    mean = np.mean(pixels, axis=2)
    pixels = (mean > 128) * 255

    ui_function.set_image(parent, pixels, False, True)
