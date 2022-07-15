"""
Negative Filter
"""


<<<<<<< HEAD
def apply_filter(parent, ui_function, pixels):
    """
    Transforma a imagem em negativa substituindo os valores RGB pela subtração deles no valor 255
    retorna a imagem modificada para a classe MainWindow
    :param ui_function:
=======
def apply_filter(parent, pixels):
    """
    Transforma a imagem em negativa substituindo os valores RGB pela subtração deles no valor 255
    retorna a imagem modificada para a classe MainWindow
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels = 255 - pixels[..., :3]

<<<<<<< HEAD
    ui_function.set_image(parent, pixels, False, True)
=======
    parent.set_image(pixels, has_filter=True)
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
