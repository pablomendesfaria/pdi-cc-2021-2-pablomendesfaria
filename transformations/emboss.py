"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
from PIL import (Image, ImageFilter)


<<<<<<< HEAD
def apply_filter(parent, ui_function, pixels):
    """
    Aplica o filtro Emboss na imagem usando a biblioteca PIL e retorna os pixels da imagem para a classe MainWindow
    :param ui_function:
=======
def apply_filter(parent, pixels, size):
    """
    Aplica o filtro Emboss na imagem usando a biblioteca PIL e retorna os pixels da imagem para a classe MainWindow
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    :param size: tamanho da imagem que recebera o filtro
    """
<<<<<<< HEAD
    img = Image.fromarray(pixels)
    img2 = img.filter(ImageFilter.EMBOSS)
    ui_function.set_image(parent, img2, True, True)
=======
    img = Image.new('RGBA', size, (255, 255, 255))
    img.putdata(pixels)
    img2 = img.filter(ImageFilter.EMBOSS)
    parent.set_image(list(img2.getdata()), has_filter=True)
>>>>>>> 2c6988e60113dcb07bc3a10106dbf06a93b5ccad
