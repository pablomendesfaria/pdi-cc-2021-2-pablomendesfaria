"""
Blue Scale Filter
"""


def apply_filter(parent, ui_function, pixels):
    """
    Transforma a imagem colorida em escala de azul, zerando os valores de vermelho e verde e deixando apenas o azul
    :param ui_function:
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels[:, :, (0, 1)] = 0

    ui_function.set_image(parent, pixels, False, True)
