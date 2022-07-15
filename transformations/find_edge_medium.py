"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
from PIL import (Image, ImageFilter)


<<<<<<< HEAD
def apply_filter(parent, ui_function, pixels):
    """
    Aplica o filtro Find Edge Medium a partir de um kernel pre estabelecido e retorna os pixels da imagem para a classe
    MainWindow
    :param ui_function:
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """
    kernel = ImageFilter.Kernel((3, 3), (0, 1, 0, 1, -4, 1, 0, 1, 0), 1)
    img = Image.fromarray(pixels)
    img2 = img.filter(kernel)
    ui_function.set_image(parent, img2, True, True)
=======
def apply_filter(parent, pixels, size):
    """
    Aplica o filtro Find Edge Medium a partir de um kernel pre estabelecido e retorna os pixels da imagem para a classe
    MainWindow
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    :param size: tamanho da imagem que recebera o filtro
    """
    kernel = ImageFilter.Kernel((3, 3), (0, 1, 0, 1, -4, 1, 0, 1, 0), 1)
    img = Image.new('RGB', size, (255, 255, 255))
    img.putdata(pixels)
    img2 = img.filter(kernel)
    parent.set_image(list(img2.getdata()), has_filter=True)
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
