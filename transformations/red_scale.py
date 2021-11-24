"""
Red Scale Filter
"""


def apply_filter(parent, pixels):
    """
    Transforma a imagem colorida em escala de vermelho, zerando os valores de verde e azul e deixando apenas o vermelho
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels[:, :, (1, 2)] = 0

    parent.set_image(pixels, has_filter=True)
