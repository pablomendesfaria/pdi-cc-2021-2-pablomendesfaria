"""
Transparency
"""


def apply_filter(parent, ui_function, pixels, value):
    """
    Aplica transparencia a uma imagem de acordo com um valor de porcentagem recebido
    :param ui_function:
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    :param value: valor obtido de uma determinada porcentagem sobre 255
    """

    pixels[..., 3] = value

    ui_function.set_image(parent, pixels, False, True)
