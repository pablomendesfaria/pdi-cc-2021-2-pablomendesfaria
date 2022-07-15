"""
Green Scale Filter
"""


def apply_filter(parent, ui_function, pixels):
    """
    Transforma a imagem colorida em escala de verde, zerando os valores de vermelho e azul e deixando apenas o verde
    :param ui_function:
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    pixels[:, :, (0, 2)] = 0

    ui_function.set_image(parent, pixels, False, True)

