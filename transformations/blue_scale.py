"""
Blue Scale Filter
"""


<<<<<<< HEAD
def apply_filter(parent, ui_function, pixels):
    """
    Transforma a imagem colorida em escala de azul, zerando os valores de vermelho e verde e deixando apenas o azul
    :param ui_function:
=======
def apply_filter(parent, pixels):
    """
    Transforma a imagem colorida em escala de azul, zerando os valores de vermelho e verde e deixando apenas o azul
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels[:, :, (0, 1)] = 0

<<<<<<< HEAD
    ui_function.set_image(parent, pixels, False, True)
=======
    parent.set_image(pixels, has_filter=True)
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
