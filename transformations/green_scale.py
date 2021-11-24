"""
Green Scale Filter
"""


def apply_filter(parent, pixels):
    """
    Transforma a imagem colorida em escala de verde, zerando os valores de vermelho e azul e deixando apenas o verde
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels[:, :, (0, 2)] = 0

    parent.set_image(pixels, has_filter=True)
