"""
Transparency
"""


def apply_filter(parent, pixels, value):
    """
    Aplica transparencia a uma imagem de acordo com um valor de porcentagem recebido
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    :param value: valor obtido de uma determinada porcentagem sobre 255
    """

    pixels[..., 3] = value

    parent.set_image(pixels, has_filter=True)
