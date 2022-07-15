import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QDialog, QLabel)

from ui_about_app_dialog import Ui_App_Dialog
from ui_about_image_dialog import Ui_Image_Dialog
from ui_functions import *
from ui_main import Ui_MainWindow
from transformations import (black_and_white, blur, countor, detail, edge_enhance_normal, edge_enhance_more, emboss,
                             find_edge_weak, find_edge_medium, find_edge_strong, flip_horizontally, flip_vertically,
                             gray_scale, negative, rotate, red_scale, green_scale, blue_scale, sharpen,
                             smooth_normal, smooth_more, logarithmic)


class AppDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_App_Dialog()
        self.ui.setupUi(self)
        self.show()


class ImageDialog(QDialog):
    def __init__(self, name, img_type, width, height):
        QDialog.__init__(self)
        self.ui = Ui_Image_Dialog()
        self.ui.setupUi(self)
        self.ui.nameLabel.setText(name)
        self.ui.typeLabel.setText(img_type)
        self.ui.widthLabel.setText(width)
        self.ui.heightLabel.setText(height)
        self.show()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.img_path = ' '
        self.image = None
        self.original_format = None
        self.pixels_bkup = []
        self.transform_bkup = []
        self.pixels = []
        self.has_filter = False
        self.has_saved = False

        self.file_name = QLabel('Name: No file open   ')
        self.file_name.setStyleSheet('color: rgb(231, 34, 88)')
        self.file_path = QLabel('   Path: No file open   ')
        self.file_path.setStyleSheet('color: rgb(231, 34, 88)')
        self.save_status = QLabel('   Save Status: No file open   ')
        self.save_status.setStyleSheet('color: rgb(231, 34, 88)')

        self.ui.setupUi(self)
        self.setup_status_bar()
        self.setup_triggers()
        self.show()

    def setup_status_bar(self):
        """
        Adiciona os label que contem o nome, local do arquivo e status de salvamento na barra de status
        """
        self.ui.status_bar.addPermanentWidget(self.file_name, 0)
        self.ui.status_bar.addPermanentWidget(self.file_path, 0)
        self.ui.status_bar.addPermanentWidget(self.save_status, 1)

    def setup_triggers(self):
        """
        Define as interações da aplicação, o que cada botão faz ao ser clicado e etc.
        """
        self.ui.action_open.triggered.connect(lambda: Ui_Functions.open_file(self))
        self.ui.action_save.triggered.connect(lambda: Ui_Functions.save(self))
        self.ui.action_save_as.triggered.connect(lambda: Ui_Functions.save_as(self))
        self.ui.action_exit.triggered.connect(sys.exit)

        self.ui.action_about_app.triggered.connect(lambda: about_app_dialog())
        self.ui.action_about_img.triggered.connect(lambda: Ui_Functions.about_image_dialog(self))

        self.ui.action_black_and_white.triggered.connect(lambda: black_and_white.apply_filter(self, Ui_Functions,
                                                                                              self.pixels))
        self.ui.action_gray_scale.triggered.connect(lambda: gray_scale.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_negative.triggered.connect(lambda: negative.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_blur.triggered.connect(lambda: blur.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_countor.triggered.connect(lambda: countor.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_detail.triggered.connect(lambda: detail.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_e_e_normal.triggered.connect(lambda: edge_enhance_normal.apply_filter(self, Ui_Functions,
                                                                                             self.pixels))
        self.ui.action_e_e_more.triggered.connect(lambda: edge_enhance_more.apply_filter(self, Ui_Functions,
                                                                                         self.pixels))
        self.ui.action_emboss.triggered.connect(lambda: emboss.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_f_e_weak_detection.triggered.connect(lambda: find_edge_weak.apply_filter(self, Ui_Functions,
                                                                                                self.pixels))
        self.ui.action_f_e_medium_detection.triggered.connect(lambda: find_edge_medium.apply_filter(self, Ui_Functions,
                                                                                                    self.pixels))
        self.ui.action_f_e_strong_detection.triggered.connect(lambda: find_edge_strong.apply_filter(self, Ui_Functions,
                                                                                                    self.pixels))
        self.ui.action_sharpen.triggered.connect(lambda: sharpen.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_s_normal.triggered.connect(
            lambda: smooth_normal.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_s_more.triggered.connect(lambda: smooth_more.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_red_scale.triggered.connect(lambda: red_scale.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_green_scale.triggered.connect(lambda: green_scale.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_blue_scale.triggered.connect(lambda: blue_scale.apply_filter(self, Ui_Functions, self.pixels))
        self.ui.action_logarithmic.triggered.connect(lambda: logarithmic.log_transform(self, Ui_Functions, self.pixels))

        self.ui.btn_open.clicked.connect(lambda: Ui_Functions.open_file(self))
        self.ui.btn_rotate.clicked.connect(lambda: rotate.rotate(self, Ui_Functions, self.pixels))
        self.ui.btn_flip_h.clicked.connect(lambda: flip_horizontally.flip(self, Ui_Functions, self.pixels))
        self.ui.btn_flip_v.clicked.connect(lambda: flip_vertically.flip(self, Ui_Functions, self.pixels))
        self.ui.btn_reset.clicked.connect(lambda: Ui_Functions.reset(self))

        self.ui.gamma_slider.valueChanged.connect(lambda: Ui_Functions.gamma_correction(self))
        self.ui.transpa_slider.valueChanged.connect(lambda: Ui_Functions.change_transparency(self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
