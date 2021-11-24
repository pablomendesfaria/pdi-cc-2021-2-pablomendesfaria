"""
Gray Scale Filter
"""
import numpy as np


def apply_filter(parent, pixels):
    """
    Transforma uma imagem coloria em tons de cinza usando média ponderada, onde o vermelho tem um peso
    de 30%, o verde 59% e o azul 11%, o valor obtido da média bonderada é utilizado no lugar dos valores
    RGB, os pixels modificados são retornados para a classe MainWindow
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels = np.average(pixels[..., :3], axis=2, weights=[0.2989, 0.5870, 0.1140]) / 3

    parent.set_image(pixels, has_filter=True)
