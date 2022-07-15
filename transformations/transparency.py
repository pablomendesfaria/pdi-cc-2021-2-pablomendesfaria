"""
Transparency
"""


<<<<<<< HEAD
def apply_filter(parent, ui_function, pixels, value):
    """
    Aplica transparencia a uma imagem de acordo com um valor de porcentagem recebido
    :param ui_function:
=======
def apply_filter(parent, pixels, value):
    """
    Aplica transparencia a uma imagem de acordo com um valor de porcentagem recebido
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    :param value: valor obtido de uma determinada porcentagem sobre 255
    """

    pixels[..., 3] = value

<<<<<<< HEAD
    ui_function.set_image(parent, pixels, False, True)
=======
    parent.set_image(pixels, has_filter=True)
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
