"""
Faz a importação das classes necessarias da biblioteca PyQt5
"""
import sys

from PIL import Image
import numpy as np
from PIL.ImageQt import ImageQt
from PyQt5 import uic
from PyQt5.QtCore import (QObject, QDir, QRect)
from PyQt5.QtGui import (QPixmap)
from PyQt5.QtWidgets import (QDialog, QLabel, QMainWindow, QAction, QSlider, QDoubleSpinBox, QSpinBox, QPushButton,
                             QFileDialog, QApplication)
from transformations import (black_and_white, blur, countor, detail, edge_enhance_normal, edge_enhance_more, emboss,
                             find_edge_weak, find_edge_medium, find_edge_strong, flip_horizontally, flip_vertically,
                             gray_scale, negative, rotate, red_scale, green_scale, blue_scale, sharpen,
                             smooth_normal, smooth_more, transparency, gamma, logarithmic)


class AboutAppDialog(QDialog):
    """
    Classe que representa o dialogo para mostrar as informações sobre o app
    Carrega o arquivo .ui que contem a interface grafica
    """
    def __init__(self):
        super(AboutAppDialog, self).__init__()
        uic.loadUi('about_app_dialog.ui', self)


class AboutImageDialog(QDialog):
    """
    Classe que representa o dialogo para mostrar as informações sobre a imagem
    Carrega o arquivo .ui que contem a interface grafica e em seguida atualiza os labels name, type, comment
    width e height com os devidos parametros recebidos da classe MainWindow
    :param name: é o nome do arquivo da imagem
    :param img_type: é o o tipo de arquivo (extensão) da imagem
    :param width: é a largura da imagem
    :param height: é a altura da imagem
    """
    def __init__(self, name, img_type, width, height):
        super(AboutImageDialog, self).__init__()
        uic.loadUi('about_image_dialog.ui', self)
        self.name = self.findChild(QLabel, 'nameLabel')
        self.type = self.findChild(QLabel, 'typeLabel')
        self.width = self.findChild(QLabel, 'widthLabel')
        self.height = self.findChild(QLabel, 'heightLabel')
        self.name.setText(name)
        self.type.setText(img_type)
        self.width.setText(width)
        self.height.setText(height)


class MainWindow(QMainWindow):
    """
    Classe que representa a janela principal da aplicação
    Carrega um arquivo .ui que contem toda a interface principal
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_window.ui', self)
        self.status_bar = self.findChild(QObject, 'statusBar')

        self.action_open = self.findChild(QAction, 'actionOpen')
        self.action_save = self.findChild(QAction, 'actionSave')
        self.action_save_as = self.findChild(QAction, 'actionSave_As')
        self.action_exit = self.findChild(QAction, 'actionExit')

        self.action_black_and_white = self.findChild(QAction, 'actionBlack_and_White')
        self.action_gray_scale = self.findChild(QAction, 'actionGray_Scale')
        self.action_negative = self.findChild(QAction, 'actionNegative')
        self.action_blur = self.findChild(QAction, 'actionBlur')
        self.action_countor = self.findChild(QAction, 'actionCountor')
        self.action_detail = self.findChild(QAction, 'actionDetail')
        self.action_e_e_normal = self.findChild(QAction, 'actionE_E_Normal')
        self.action_e_e_more = self.findChild(QAction, 'actionE_E_More')
        self.action_emboss = self.findChild(QAction, 'actionEmboss')
        self.action_f_e_weak_detection = self.findChild(QAction, 'actionF_E_Weak_Detection')
        self.action_f_e_medium_detection = self.findChild(QAction, 'actionF_E_Medium_Detection')
        self.action_f_e_strong_detection = self.findChild(QAction, 'actionF_E_Strong_Detection')
        self.action_sharpen = self.findChild(QAction, 'actionSharpen')
        self.action_s_normal = self.findChild(QAction, 'actionS_Normal')
        self.action_s_more = self.findChild(QAction, 'actionS_More')
        self.action_red_scale = self.findChild(QAction, 'actionRed_Scale')
        self.action_green_scale = self.findChild(QAction, 'actionGreen_Scale')
        self.action_blue_scale = self.findChild(QAction, 'actionBlue_Scale')
        self.action_logarithmic = self.findChild(QAction, 'actionLogarithmic')

        self.action_about_app = self.findChild(QAction, 'actionAbout_App')
        self.action_about_image = self.findChild(QAction, 'actionAbout_Img')

        self.image_label = self.findChild(QLabel, 'imageLabel')

        self.gamma_slider = self.findChild(QSlider, 'gammaSlider')
        self.transparency_slider = self.findChild(QSlider, 'transpaSlider')

        self.gamma_spin = self.findChild(QDoubleSpinBox, 'gammaSpin')
        self.transparency_spin = self.findChild(QSpinBox, 'transpaSpin')

        self.btn_open = self.findChild(QPushButton, 'btnOpen')
        self.btn_rotate = self.findChild(QPushButton, 'btnRotate')
        self.btn_flip_h = self.findChild(QPushButton, 'btnFlipH')
        self.btn_flip_v = self.findChild(QPushButton, 'btnFlipV')
        self.btn_reset = self.findChild(QPushButton, 'btnReset')

        self.file_name = QLabel('Name: No file open   ')
        self.file_name.setStyleSheet('color: rgb(231, 34, 88)')
        self.file_path = QLabel('   Path: No file open   ')
        self.file_path.setStyleSheet('color: rgb(231, 34, 88)')
        self.save_status = QLabel('   Save Status: No file open   ')
        self.save_status.setStyleSheet('color: rgb(231, 34, 88)')

        self.img_path = ' '
        self.image = None
        self.original_format = None
        self.pixels_bkup = []
        self.transform_bkup = []
        self.pixels = []
        self.has_filter = False
        self.setup_status_bar()
        self.setup_ui()

    def setup_status_bar(self):
        """
        Adiciona os label que contem o nome, local do arquivo e status de salvamento na barra de status
        """
        self.status_bar.addPermanentWidget(self.file_name, 0)
        self.status_bar.addPermanentWidget(self.file_path, 0)
        self.status_bar.addPermanentWidget(self.save_status, 1)

    def setup_ui(self):
        """
        Define as interações da aplicação, o que cada botão faz ao ser clicado e etc.
        """
        self.action_open.triggered.connect(self.open_file)
        self.action_save.triggered.connect(self.save)
        self.action_save_as.triggered.connect(self.save_as)
        self.action_exit.triggered.connect(sys.exit)

        self.action_about_app.triggered.connect(about_app_dialog)
        self.action_about_image.triggered.connect(self.about_image_dialog)

        self.action_black_and_white.triggered.connect(lambda: black_and_white.apply_filter(self, self.pixels))
        self.action_gray_scale.triggered.connect(lambda: gray_scale.apply_filter(self, self.pixels))
        self.action_negative.triggered.connect(lambda: negative.apply_filter(self, self.pixels))
        self.action_blur.triggered.connect(lambda: blur.apply_filter(self, self.pixels, self.image.size))
        self.action_countor.triggered.connect(lambda: countor.apply_filter(self, self.pixels, self.image.size))
        self.action_detail.triggered.connect(lambda: detail.apply_filter(self, self.pixels, self.image.size))
        self.action_e_e_normal.triggered.connect(lambda: edge_enhance_normal.apply_filter(self, self.pixels,
                                                                                          self.image.size))
        self.action_e_e_more.triggered.connect(lambda: edge_enhance_more.apply_filter(self, self.pixels,
                                                                                      self.image.size))
        self.action_emboss.triggered.connect(lambda: emboss.apply_filter(self, self.pixels, self.image.size))
        self.action_f_e_weak_detection.triggered.connect(lambda: find_edge_weak.apply_filter(self, self.pixels,
                                                                                             self.image.size))
        self.action_f_e_medium_detection.triggered.connect(lambda: find_edge_medium.apply_filter(self, self.pixels,
                                                                                                 self.image.size))
        self.action_f_e_strong_detection.triggered.connect(lambda: find_edge_strong.apply_filter(self, self.pixels,
                                                                                                 self.image.size))
        self.action_sharpen.triggered.connect(lambda: sharpen.apply_filter(self, self.pixels, self.image.size))
        self.action_s_normal.triggered.connect(lambda: smooth_normal.apply_filter(self, self.pixels, self.image.size))
        self.action_s_more.triggered.connect(lambda: smooth_more.apply_filter(self, self.pixels, self.image.size))
        self.action_red_scale.triggered.connect(lambda: red_scale.apply_filter(self, self.pixels))
        self.action_green_scale.triggered.connect(lambda: green_scale.apply_filter(self, self.pixels))
        self.action_blue_scale.triggered.connect(lambda: blue_scale.apply_filter(self, self.pixels))
        self.action_logarithmic.triggered.connect(lambda: logarithmic.log_transform(self, self.pixels))

        self.btn_open.clicked.connect(self.open_file)
        self.btn_rotate.clicked.connect(lambda: rotate.rotate(self, self.pixels))
        self.btn_flip_h.clicked.connect(lambda: flip_horizontally.flip(self, self.pixels))
        self.btn_flip_v.clicked.connect(lambda: flip_vertically.flip(self, self.pixels))
        self.btn_reset.clicked.connect(self.reset)

        self.gamma_slider.valueChanged[int].connect(self.gamma_correction)
        self.transparency_slider.valueChanged[int].connect(self.change_transparency)

    def open_file(self):
        """
        Abre uma imagem escolhida pelo usuario e define o label image como sendo essa imagem mantendo as proporções
        da imagem, tambem define a variavel image que sera a imagem usada para as transformações como sendo a imagem
        aberta, assim como tambem o seu back up caso o usuario queira resetar.
        """
        path, _ = QFileDialog.getOpenFileName(self, 'Open File', QDir.currentPath(), 'All Files (*.*);;'
                                                                                     'Images (*.png; *.jpg)', 'Images '
                                                                                                              '(*.png'
                                                                                                              '; '
                                                                                                              '*.jpg)')
        if path:
            self.img_path = path
            self.set_enable_disable()
        else:
            pass

    def save(self):
        """
        Salva a imagem no caminho de destino com o mesmo nome, assim sobreescrevendo a antiga
        """
        self.image.save(self.img_path)
        self.init_image()
        self.save_status.setText('   Save Status: Saved   ')

    def save_as(self):
        """
        Salva a imagem com o nome e local definido pelo usuario
        """
        path, _ = QFileDialog.getSaveFileName(self, 'Save File', QDir.currentPath(), 'All Files (*.*);;'
                                                                                     'Images (*.png)', 'Images '
                                                                                                       '(*.png')
        if path:
            self.img_path = path
            self.image.save(self.img_path)
            self.init_image()
            self.file_name.setText(f'   Name: {self.get_image_name()}   ')
            self.file_path.setText(f'   Path: {self.img_path}   ')
            self.save_status.setText('   Save Status: Saved   ')
            self.action_save.setEnabled(True)
        else:
            pass

    def init_image(self):
        """
        Configura a imagem a ser trabalhada e o label que ira exibir a imagem, assim como os devidos backups dos pixels
        e do formato original da imagem
        Sera usado apos abrir ou salvar uma imagem
        """
        img = Image.open(self.img_path)
        self.original_format = img.format
        img = img.convert('RGBA')
        img.format = self.original_format
        self.pixels = np.array(img)
        self.image = img
        self.pixels_bkup = self.pixels.copy()

        self.set_img_on_label()

    def set_image(self, pixels, has_filter=False):
        """
        Atualiza a imagem e o label que mostra a imagem toda vez que ela for modificada
        :param has_filter: serve unicamente para a aplicação de correção gamma, pois apos aplicar a correção gamma
        em cima de outro o filtro anteriormente aplicado é removido, para evitar isso foi criado essa variavel de
        controle
        :param pixels: é a imagem modificada recebida de alguma classe que aplica alguma transformação
        """
        if has_filter:
            self.has_filter = has_filter
            self.transform_bkup = pixels.copy()

        img = Image.fromarray(np.uint8(pixels))
        img = img.convert('RGBA')
        self.pixels = np.array(img)
        self.image = img.copy()
        self.image.format = self.original_format

        self.set_img_on_label()

        self.save_status.setText('   Save Status: Not Saved*   ')

        self.action_save_as.setEnabled(True)
        self.btn_reset.setEnabled(True)

    def set_img_on_label(self):
        """
        Verifica se a imagem esta rotacionada em 90 ou 270 graus e entaõ define o label de acordo
        """
        q_image = ImageQt(self.image)
        img_size = self.image.size
        label_size = self.image_label.size()
        label_width = int((img_size[0] * label_size.height()) / img_size[1])

        if img_size[1] > img_size[0]:
            self.image_label.setGeometry(QRect(250, 10, label_width, label_size.height()))
            self.image_label.setPixmap(QPixmap.fromImage(q_image))
        else:
            self.image_label.setGeometry(QRect(int((779 - label_width) / 2), 10, label_width, label_size.height()))
            self.image_label.setPixmap(QPixmap.fromImage(q_image))

    def reset(self):
        """
        Reseta a imagem para o status original e desativa o botão de reset que so sera ativado quando a imagem for
        modificada
        """
        self.pixels = self.pixels_bkup.copy()
        self.transform_bkup = self.pixels_bkup.copy()

        img = Image.fromarray(self.pixels)
        self.image = img.copy()
        self.image.format = self.original_format

        self.set_img_on_label()

        self.has_filter = False
        self.gamma_slider.setValue(100)
        self.gamma_spin.setValue(1)
        self.transparency_slider.setValue(0)
        self.transparency_spin.setValue(0)
        self.action_save_as.setDisabled(True)
        self.btn_reset.setDisabled(True)

    def set_enable_disable(self):
        """
        Apos uma imagem ser aberta os componentes que estavam desabilitados seram ativados e outros que estavam ativados
        desabilitados
        """
        self.action_black_and_white.setEnabled(True)
        self.action_gray_scale.setEnabled(True)
        self.action_negative.setEnabled(True)
        self.action_blur.setEnabled(True)
        self.action_countor.setEnabled(True)
        self.action_detail.setEnabled(True)
        self.action_e_e_normal.setEnabled(True)
        self.action_e_e_more.setEnabled(True)
        self.action_emboss.setEnabled(True)
        self.action_f_e_weak_detection.setEnabled(True)
        self.action_f_e_medium_detection.setEnabled(True)
        self.action_f_e_strong_detection.setEnabled(True)
        self.action_sharpen.setEnabled(True)
        self.action_s_normal.setEnabled(True)
        self.action_s_more.setEnabled(True)
        self.action_red_scale.setEnabled(True)
        self.action_green_scale.setEnabled(True)
        self.action_blue_scale.setEnabled(True)
        self.action_logarithmic.setEnabled(True)

        self.action_about_image.setEnabled(True)

        self.gamma_slider.setEnabled(True)
        self.transparency_slider.setEnabled(True)

        self.gamma_spin.setEnabled(True)
        self.transparency_spin.setEnabled(True)

        self.btn_open.setDisabled(True)
        self.btn_open.setVisible(False)
        self.btn_rotate.setEnabled(True)
        self.btn_flip_h.setEnabled(True)
        self.btn_flip_v.setEnabled(True)

        self.init_image()

        self.file_name.setText(f'   Name: {self.get_image_name()}   ')
        self.file_path.setText(f'   Path: {self.img_path}   ')
        self.save_status.setText('   Save Status: Without Changes   ')

    def get_image_name(self):
        """
        Pega o nome da imagem na string que contrem o caminho completa e o retorna
        :return: retorna o nome da imagem
        """
        name = self.img_path.split('/')[-1]
        name = name.split('.')
        return name[0]

    def about_image_dialog(self):
        """
        Inicia o dialogo que contem as informações da imagem
        """
        img_format = self.image.format
        width, height = self.image.size
        image_dialog = AboutImageDialog(self.get_image_name(), img_format, str(width), str(height))
        image_dialog.exec_()

    def gamma_correction(self, value):
        """
        Atualiza o valor do spinBox quando o slider for movido
        :param value: valor atual do slider
        """
        self.gamma_spin.setValue(((value / 10) / 10))
        val = self.gamma_slider.sliderPosition()
        pixel = self.transform_bkup.copy() if self.has_filter else self.pixels_bkup.copy()
        gamma.correction(self, pixel, ((val / 10) / 10))

    def change_transparency(self, value):
        """
        Atualiza o valor do spinBox quando o slider for movido
        Pega o valor do slider e transforma em um inteiro corresponde a porcentagem escolhida, chama o arquivo que faz a
        transformação
        :param value: valor atual do slider
        """
        self.transparency_spin.setValue(value)
        val = self.transparency_slider.sliderPosition()
        transparency.apply_filter(self, self.pixels, int(255 - ((255 * val) / 100)))


def about_app_dialog():
    """
    Inicia o dialogo que contem as informações do app
    """
    app_dialog = AboutAppDialog()
    app_dialog.exec_()


def start():
    """
        Inicia a aplicação
    """
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
