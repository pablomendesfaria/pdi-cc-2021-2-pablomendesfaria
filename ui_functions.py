import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtCore import QDir, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog

from main import MainWindow, AppDialog, ImageDialog
from transformations import (transparency, gamma)


class Ui_Functions(MainWindow):
    def open_file(self):
        """
        Abre uma imagem escolhida pelo usuario e define o label image como sendo essa imagem mantendo as proporções
        da imagem, tambem define a variavel image que sera a imagem usada para as transformações como sendo a imagem
        aberta, assim como tambem o seu back up caso o usuario queira resetar.
        """
        path, _ = QFileDialog.getOpenFileName(self, 'Open File', QDir.currentPath(), 'All Files (*.*);;'
                                                                                     'Images (*.png; *.jpg; *.jpeg)',
                                              'Images (*.png; *.jpg; *.jpeg)')
        if path:
            self.img_path = path
            Ui_Functions.set_enable_disable(self)
        else:
            pass

    def save(self):
        """
        Salva a imagem no caminho de destino com o mesmo nome, assim sobreescrevendo a antiga
        """
        self.image.save(self.img_path)
        self.has_saved = True
        Ui_Functions.init_image(self)
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
            self.has_saved = True
            Ui_Functions.init_image(self)
            self.file_name.setText(f'   Name: {self.get_image_name()}   ')
            self.file_path.setText(f'   Path: {self.img_path}   ')
            self.save_status.setText('   Save Status: Saved   ')
            self.ui.action_save.setEnabled(True)
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
        self.pixels = np.asarray(img)
        self.image = img
        if not self.has_saved:
            self.pixels_bkup = self.pixels.copy()
        Ui_Functions.set_img_on_label(self)

    def set_image(self, pixels, has_data=False, has_filter=False):
        """
        Atualiza a imagem e o label que mostra a imagem toda vez que ela for modificada
        :param has_data:
        :param has_filter: serve unicamente para a aplicação de correção gamma, pois apos aplicar a correção gamma
        em cima de outro o filtro anteriormente aplicado é removido, para evitar isso foi criado essa variavel de
        controle
        :param pixels: é a imagem modificada recebida de alguma classe que aplica alguma transformação
        """
        if has_filter:
            self.has_filter = has_filter
            self.transform_bkup = np.asarray(pixels)
        if has_data:
            img = pixels
        else:
            img = Image.fromarray(pixels)
        img = img.convert('RGBA')
        self.pixels = np.asarray(img)
        self.image = img.copy()
        self.image.format = self.original_format

        Ui_Functions.set_img_on_label(self)

        self.save_status.setText('   Save Status: Not Saved*   ')

        self.ui.action_save_as.setEnabled(True)
        self.ui.btn_reset.setEnabled(True)

    def set_img_on_label(self):
        """
        Verifica se a imagem esta rotacionada em 90 ou 270 graus e entaõ define o label de acordo
        """
        q_image = ImageQt(self.image)
        img_size = self.image.size
        label_size = self.ui.image_label.size()
        label_width = int((img_size[0] * label_size.height()) / img_size[1])

        if img_size[1] > img_size[0]:
            self.ui.image_label.setGeometry(QRect(250, 10, label_width, label_size.height()))
            self.ui.image_label.setPixmap(QPixmap.fromImage(q_image))
        else:
            self.ui.image_label.setGeometry(QRect(int((779 - label_width) / 2), 10, label_width, label_size.height()))
            self.ui.image_label.setPixmap(QPixmap.fromImage(q_image))

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

        Ui_Functions.set_img_on_label(self)

        self.has_filter = False
        self.has_saved = False
        self.ui.gamma_slider.setValue(100)
        self.ui.gamma_spin.setValue(1)
        self.ui.transpa_slider.setValue(0)
        self.ui.transpa_spin.setValue(0)
        self.ui.btn_reset.setDisabled(True)
        self.save_status.setText('   Save Status: Not Saved*   ')

    def set_enable_disable(self):
        """
        Apos uma imagem ser aberta os componentes que estavam desabilitados seram ativados e outros que estavam ativados
        desabilitados
        """
        self.ui.action_black_and_white.setEnabled(True)
        self.ui.action_gray_scale.setEnabled(True)
        self.ui.action_negative.setEnabled(True)
        self.ui.action_blur.setEnabled(True)
        self.ui.action_countor.setEnabled(True)
        self.ui.action_detail.setEnabled(True)
        self.ui.action_e_e_normal.setEnabled(True)
        self.ui.action_e_e_more.setEnabled(True)
        self.ui.action_emboss.setEnabled(True)
        self.ui.action_f_e_weak_detection.setEnabled(True)
        self.ui.action_f_e_medium_detection.setEnabled(True)
        self.ui.action_f_e_strong_detection.setEnabled(True)
        self.ui.action_sharpen.setEnabled(True)
        self.ui.action_s_normal.setEnabled(True)
        self.ui.action_s_more.setEnabled(True)
        self.ui.action_red_scale.setEnabled(True)
        self.ui.action_green_scale.setEnabled(True)
        self.ui.action_blue_scale.setEnabled(True)
        self.ui.action_logarithmic.setEnabled(True)

        self.ui.action_about_img.setEnabled(True)

        self.ui.gamma_slider.setEnabled(True)
        self.ui.transpa_slider.setEnabled(True)

        self.ui.gamma_spin.setEnabled(True)
        self.ui.transpa_spin.setEnabled(True)

        self.ui.btn_open.setDisabled(True)
        self.ui.btn_open.setVisible(False)
        self.ui.btn_rotate.setEnabled(True)
        self.ui.btn_flip_h.setEnabled(True)
        self.ui.btn_flip_v.setEnabled(True)

        Ui_Functions.init_image(self)

        self.file_name.setText(f'   Name: {Ui_Functions.get_image_name(self)}   ')
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
        image_dialog = ImageDialog(Ui_Functions.get_image_name(self), img_format, str(width), str(height))
        image_dialog.exec_()

    def gamma_correction(self):
        """
        Atualiza o valor do spinBox quando o slider for movido
        :param value: valor atual do slider
        """
        self.ui.gamma_spin.setValue(((self.ui.gamma_slider.value() / 10) / 10))
        val = self.ui.gamma_slider.sliderPosition()
        pixel = self.transform_bkup.copy() if self.has_filter else self.pixels_bkup.copy()
        gamma.correction(self, Ui_Functions, pixel, ((val / 10) / 10))

    def change_transparency(self):
        """
        Atualiza o valor do spinBox quando o slider for movido
        Pega o valor do slider e transforma em um inteiro corresponde a porcentagem escolhida, chama o arquivo que faz a
        transformação
        :param value: valor atual do slider
        """
        self.ui.transpa_spin.setValue(self.ui.transpa_slider.value())
        val = self.ui.transpa_slider.sliderPosition()
        transparency.apply_filter(self, Ui_Functions, self.pixels, int(255 - ((255 * val) / 100)))


def about_app_dialog():
    """
    Inicia o dialogo que contem as informações do app
    """
    app_dialog = AppDialog()
    app_dialog.exec_()
