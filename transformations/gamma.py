"""
Gamma Correction
"""
import numpy as np
import cv2


def correction(parent, pixels, gam):
    """
    Faz a correção gama da imagem de acordo com o valor recebido
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    :param gam: o valor gamma a ser aplicado nos pixels
    """

    table = np.array([((i / 255) ** gam) * 255 for i in np.arange(0, 256)]).astype("uint8")
    pixels = cv2.LUT(pixels, table)

    parent.set_image(pixels)
