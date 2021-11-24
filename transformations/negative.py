"""
Negative Filter
"""


def apply_filter(parent, pixels):
    """
    Transforma a imagem em negativa substituindo os valores RGB pela subtração deles no valor 255
    retorna a imagem modificada para a classe MainWindow
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels = 255 - pixels[..., :3]

    parent.set_image(pixels, has_filter=True)
