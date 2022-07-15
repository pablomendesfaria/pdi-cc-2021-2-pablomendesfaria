# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainnlFGSN.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QCursor, QFont, QIcon)
from PySide6.QtWidgets import (QAbstractSpinBox, QDoubleSpinBox, QFrame,
                               QHBoxLayout, QLabel, QLayout, QMenu, QMenuBar, QPushButton, QSlider, QSpinBox, QStatusBar, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(990, 475)
        MainWindow.setMinimumSize(QSize(990, 475))
        icon = QIcon()
        icon.addFile(u"resources/window_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
                                 "	background-color: rgb(25, 26, 43);\n"
                                 "}\n"
                                 "QMenuBar{\n"
                                 "	background-color: rgb(234, 237, 244);\n"
                                 "	color: rgb(25, 26, 43);\n"
                                 "}\n"
                                 "QMenuBar::item:selected{\n"
                                 "	background-color: rgb(231, 34, 88);\n"
                                 "	color: rgb(234, 237, 244);\n"
                                 "}\n"
                                 "QMenu{\n"
                                 "	background-color: rgb(231, 34, 88);\n"
                                 "	color: rgb(234, 237, 244);\n"
                                 "}\n"
                                 "QMenu::item:enabled:selected{\n"
                                 "	background-color: rgb(234, 237, 244);\n"
                                 "	color: rgb(25, 26, 43);\n"
                                 "}\n"
                                 "QMenu#menuEdge_Enhance, #menuFind_Edge, #menuSmooth, #menuAbout{\n"
                                 "	background-color: rgb(234, 237, 244);\n"
                                 "	color: rgb(25, 26, 43);\n"
                                 "}\n"
                                 "QMenu::item:enabled:selected#menuEdge_Enhance{\n"
                                 "	background-color: rgb(231, 34, 88);\n"
                                 "	color: rgb(234, 237, 244);\n"
                                 "}\n"
                                 "QMenu::item:enabled:selected#menuFind_Edge{\n"
                                 "	background-color: rgb(231, 34, 88);\n"
                                 "	color: rgb(234, 237, 244);\n"
                                 "}\n"
                                 "QMenu::item:enabled:selected#menuSmooth{\n"
                                 "	background-color: rgb(231, 34, 88);\n"
                                 "	color: rgb(234, 237, 244);\n"
                                 "}\n"
                                 "QMenu::item:enabled:selected#menuAb"
                                 "out{\n"
                                 "	background-color: rgb(231, 34, 88);\n"
                                 "	color: rgb(234, 237, 244);\n"
                                 "}\n"
                                 "QMenu::item:disabled{\n"
                                 "	color: gray;\n"
                                 "}\n"
                                 "QStatusBar{\n"
                                 "	color: white;\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "	color: rgb(25, 26, 43);\n"
                                 "	 border-style: none;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "	border: 1px solid #191a2b;\n"
                                 "	border-radius: 10px;\n"
                                 "}\n"
                                 "QPushButton:pressed{\n"
                                 "	border: 2px solid #e72258;\n"
                                 "	border-radius: 10px;\n"
                                 "}\n"
                                 "QPushButton:hover#btnOpen{\n"
                                 "	border-style: none;\n"
                                 "}\n"
                                 "QPushButton:pressed#Open{\n"
                                 "	border-style: none;\n"
                                 "}\n"
                                 "QSlider::handle:horizontaly{\n"
                                 "	background-color:  rgb(25, 26, 43);\n"
                                 "	border: 1px solid #191a2b;\n"
                                 "	width: 9px;\n"
                                 "	margin: -6px 0;\n"
                                 "	border-radius: 5px;\n"
                                 "}\n"
                                 "QSlider::groove:horizontaly#gammaSlider{\n"
                                 "	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(27, 27, 27, 255), stop:1 rgba(207, 207, 207, 255));\n"
                                 "	height: 10px;\n"
                                 "	border-radius: 5px;\n"
                                 "}\n"
                                 "QSlider::groove:horizontaly#transpaSlider{\n"
                                 "	height: 10px"
                                 ";\n"
                                 "	border-radius: 5px;\n"
                                 "}\n"
                                 "QSlider::sub-page:horizontaly#transpaSlider{\n"
                                 "	background: rgb(231, 34, 88);\n"
                                 "	border-radius: 5px;\n"
                                 "}\n"
                                 "QSlider::add-page:horizontaly#transpaSlider{\n"
                                 "	background: rgba(214, 214, 214);\n"
                                 "	border-radius: 5px;\n"
                                 "}\n"
                                 "QSpinBox{\n"
                                 "	color: rgb(25, 26, 43);\n"
                                 "}\n"
                                 "QDoubleSpinBox{\n"
                                 "	color: rgb(25, 26, 43);\n"
                                 "}")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save_as = QAction(MainWindow)
        self.action_save_as.setObjectName(u"action_save_as")
        self.action_save_as.setEnabled(False)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_black_and_white = QAction(MainWindow)
        self.action_black_and_white.setObjectName(u"action_black_and_white")
        self.action_black_and_white.setEnabled(False)
        self.action_gray_scale = QAction(MainWindow)
        self.action_gray_scale.setObjectName(u"action_gray_scale")
        self.action_gray_scale.setEnabled(False)
        self.action_blur = QAction(MainWindow)
        self.action_blur.setObjectName(u"action_blur")
        self.action_blur.setEnabled(False)
        self.action_countor = QAction(MainWindow)
        self.action_countor.setObjectName(u"action_countor")
        self.action_countor.setEnabled(False)
        self.action_detail = QAction(MainWindow)
        self.action_detail.setObjectName(u"action_detail")
        self.action_detail.setEnabled(False)
        self.action_e_e_normal = QAction(MainWindow)
        self.action_e_e_normal.setObjectName(u"action_e_e_normal")
        self.action_e_e_normal.setEnabled(False)
        self.action_e_e_more = QAction(MainWindow)
        self.action_e_e_more.setObjectName(u"action_e_e_more")
        self.action_e_e_more.setEnabled(False)
        self.action_emboss = QAction(MainWindow)
        self.action_emboss.setObjectName(u"action_emboss")
        self.action_emboss.setEnabled(False)
        self.action_negative = QAction(MainWindow)
        self.action_negative.setObjectName(u"action_negative")
        self.action_negative.setEnabled(False)
        self.action_sharpen = QAction(MainWindow)
        self.action_sharpen.setObjectName(u"action_sharpen")
        self.action_sharpen.setEnabled(False)
        self.action_s_normal = QAction(MainWindow)
        self.action_s_normal.setObjectName(u"action_s_normal")
        self.action_s_normal.setEnabled(False)
        self.action_s_more = QAction(MainWindow)
        self.action_s_more.setObjectName(u"action_s_more")
        self.action_s_more.setEnabled(False)
        self.action_f_e_weak_detection = QAction(MainWindow)
        self.action_f_e_weak_detection.setObjectName(u"action_f_e_weak_detection")
        self.action_f_e_weak_detection.setEnabled(False)
        self.action_f_e_medium_detection = QAction(MainWindow)
        self.action_f_e_medium_detection.setObjectName(u"action_f_e_medium_detection")
        self.action_f_e_medium_detection.setEnabled(False)
        self.action_f_e_strong_detection = QAction(MainWindow)
        self.action_f_e_strong_detection.setObjectName(u"action_f_e_strong_detection")
        self.action_f_e_strong_detection.setEnabled(False)
        self.action_about_app = QAction(MainWindow)
        self.action_about_app.setObjectName(u"action_about_app")
        self.action_about_app.setEnabled(True)
        self.action_about_img = QAction(MainWindow)
        self.action_about_img.setObjectName(u"action_about_img")
        self.action_about_img.setEnabled(False)
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_save.setEnabled(False)
        self.action_red_scale = QAction(MainWindow)
        self.action_red_scale.setObjectName(u"action_red_scale")
        self.action_red_scale.setEnabled(False)
        self.action_green_scale = QAction(MainWindow)
        self.action_green_scale.setObjectName(u"action_green_scale")
        self.action_green_scale.setEnabled(False)
        self.action_blue_scale = QAction(MainWindow)
        self.action_blue_scale.setObjectName(u"action_blue_scale")
        self.action_blue_scale.setEnabled(False)
        self.action_logarithmic = QAction(MainWindow)
        self.action_logarithmic.setObjectName(u"action_logarithmic")
        self.action_logarithmic.setEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(780, 0, 211, 461))
        self.verticalWidget.setStyleSheet(u"background-color: rgb(234, 237, 244);")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(10, -1, 10, 30)
        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(500, 15))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.line = QFrame(self.verticalWidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(190, 0))
        self.line.setMaximumSize(QSize(190, 16777215))
        self.line.setLayoutDirection(Qt.LeftToRight)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.horizontalWidget = QWidget(self.verticalWidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMaximumSize(QSize(16777215, 250))
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_rotate = QPushButton(self.horizontalWidget)
        self.btn_rotate.setObjectName(u"btn_rotate")
        self.btn_rotate.setEnabled(False)
        self.btn_rotate.setMinimumSize(QSize(40, 40))
        self.btn_rotate.setMaximumSize(QSize(40, 40))
        self.btn_rotate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_rotate.setToolTipDuration(-1)
        icon1 = QIcon()
        icon1.addFile(u"resources/rotate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rotate.setIcon(icon1)
        self.btn_rotate.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.btn_rotate)

        self.btn_flip_h = QPushButton(self.horizontalWidget)
        self.btn_flip_h.setObjectName(u"btn_flip_h")
        self.btn_flip_h.setEnabled(False)
        self.btn_flip_h.setMinimumSize(QSize(40, 40))
        self.btn_flip_h.setMaximumSize(QSize(40, 40))
        self.btn_flip_h.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"resources/flip_h.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_flip_h.setIcon(icon2)
        self.btn_flip_h.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.btn_flip_h)

        self.btn_flip_v = QPushButton(self.horizontalWidget)
        self.btn_flip_v.setObjectName(u"btn_flip_v")
        self.btn_flip_v.setEnabled(False)
        self.btn_flip_v.setMinimumSize(QSize(40, 40))
        self.btn_flip_v.setMaximumSize(QSize(40, 40))
        self.btn_flip_v.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"resources/flip_v.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_flip_v.setIcon(icon3)
        self.btn_flip_v.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.btn_flip_v)

        self.verticalLayout.addWidget(self.horizontalWidget)

        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(105, 15))
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gamma_slider = QSlider(self.verticalWidget)
        self.gamma_slider.setObjectName(u"gamma_slider")
        self.gamma_slider.setEnabled(False)
        self.gamma_slider.setMinimumSize(QSize(140, 22))
        self.gamma_slider.setMaximumSize(QSize(191, 22))
        self.gamma_slider.setMinimum(25)
        self.gamma_slider.setMaximum(200)
        self.gamma_slider.setValue(100)
        self.gamma_slider.setSliderPosition(100)
        self.gamma_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.gamma_slider)

        self.gamma_spin = QDoubleSpinBox(self.verticalWidget)
        self.gamma_spin.setObjectName(u"gamma_spin")
        self.gamma_spin.setEnabled(False)
        self.gamma_spin.setMinimumSize(QSize(35, 25))
        self.gamma_spin.setAlignment(Qt.AlignCenter)
        self.gamma_spin.setReadOnly(True)
        self.gamma_spin.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.gamma_spin.setDecimals(2)
        self.gamma_spin.setMaximum(2.000000000000000)
        self.gamma_spin.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.gamma_spin)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(self.verticalWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(105, 15))
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.transpa_slider = QSlider(self.verticalWidget)
        self.transpa_slider.setObjectName(u"transpa_slider")
        self.transpa_slider.setEnabled(False)
        self.transpa_slider.setMinimumSize(QSize(140, 22))
        self.transpa_slider.setMaximumSize(QSize(191, 22))
        self.transpa_slider.setMinimum(0)
        self.transpa_slider.setMaximum(100)
        self.transpa_slider.setValue(0)
        self.transpa_slider.setSliderPosition(0)
        self.transpa_slider.setOrientation(Qt.Horizontal)
        self.transpa_slider.setInvertedAppearance(False)
        self.transpa_slider.setInvertedControls(True)

        self.horizontalLayout_3.addWidget(self.transpa_slider)

        self.transpa_spin = QSpinBox(self.verticalWidget)
        self.transpa_spin.setObjectName(u"transpa_spin")
        self.transpa_spin.setEnabled(False)
        self.transpa_spin.setMinimumSize(QSize(35, 25))
        self.transpa_spin.setAlignment(Qt.AlignCenter)
        self.transpa_spin.setReadOnly(True)
        self.transpa_spin.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.transpa_spin.setMaximum(100)
        self.transpa_spin.setValue(0)

        self.horizontalLayout_3.addWidget(self.transpa_spin)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btn_reset = QPushButton(self.verticalWidget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setEnabled(False)
        self.btn_reset.setMaximumSize(QSize(191, 60))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.btn_reset.setFont(font2)
        self.btn_reset.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"resources/reset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reset.setIcon(icon4)
        self.btn_reset.setIconSize(QSize(40, 40))
        self.btn_reset.setChecked(False)

        self.verticalLayout.addWidget(self.btn_reset)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(7, 1)
        self.btn_open = QPushButton(self.centralwidget)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setGeometry(QRect(210, 60, 331, 311))
        self.btn_open.setMinimumSize(QSize(331, 311))
        self.btn_open.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"resources/open_image_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open.setIcon(icon5)
        self.btn_open.setIconSize(QSize(331, 311))
        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(10, 10, 761, 421))
        self.image_label.setMaximumSize(QSize(761, 421))
        self.image_label.setLayoutDirection(Qt.LeftToRight)
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.image_label.raise_()
        self.verticalWidget.raise_()
        self.btn_open.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 990, 22))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_filters = QMenu(self.menubar)
        self.menu_filters.setObjectName(u"menu_filters")
        self.menu_edge_enhance = QMenu(self.menu_filters)
        self.menu_edge_enhance.setObjectName(u"menu_edge_enhance")
        self.menu_smooth = QMenu(self.menu_filters)
        self.menu_smooth.setObjectName(u"menu_smooth")
        self.menu_find_edge = QMenu(self.menu_filters)
        self.menu_find_edge.setObjectName(u"menu_find_edge")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_about = QMenu(self.menu_help)
        self.menu_about.setObjectName(u"menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_filters.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_save_as)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_filters.addAction(self.action_black_and_white)
        self.menu_filters.addAction(self.action_gray_scale)
        self.menu_filters.addAction(self.action_negative)
        self.menu_filters.addSeparator()
        self.menu_filters.addAction(self.action_blur)
        self.menu_filters.addAction(self.action_countor)
        self.menu_filters.addAction(self.action_detail)
        self.menu_filters.addAction(self.menu_edge_enhance.menuAction())
        self.menu_filters.addAction(self.action_emboss)
        self.menu_filters.addAction(self.menu_find_edge.menuAction())
        self.menu_filters.addAction(self.action_sharpen)
        self.menu_filters.addAction(self.menu_smooth.menuAction())
        self.menu_filters.addSeparator()
        self.menu_filters.addAction(self.action_red_scale)
        self.menu_filters.addAction(self.action_green_scale)
        self.menu_filters.addAction(self.action_blue_scale)
        self.menu_filters.addSeparator()
        self.menu_filters.addAction(self.action_logarithmic)
        self.menu_edge_enhance.addAction(self.action_e_e_normal)
        self.menu_edge_enhance.addAction(self.action_e_e_more)
        self.menu_smooth.addAction(self.action_s_normal)
        self.menu_smooth.addAction(self.action_s_more)
        self.menu_find_edge.addAction(self.action_f_e_weak_detection)
        self.menu_find_edge.addAction(self.action_f_e_medium_detection)
        self.menu_find_edge.addAction(self.action_f_e_strong_detection)
        self.menu_help.addAction(self.menu_about.menuAction())
        self.menu_about.addAction(self.action_about_app)
        self.menu_about.addAction(self.action_about_img)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple Editor", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
        # if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
        # endif // QT_CONFIG(shortcut)
        self.action_save_as.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        # if QT_CONFIG(shortcut)
        self.action_save_as.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+S", None))
        # endif // QT_CONFIG(shortcut)
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.action_black_and_white.setText(QCoreApplication.translate("MainWindow", u"Black and White", None))
        self.action_gray_scale.setText(QCoreApplication.translate("MainWindow", u"Gray Scale", None))
        self.action_blur.setText(QCoreApplication.translate("MainWindow", u"Blur", None))
        self.action_countor.setText(QCoreApplication.translate("MainWindow", u"Countor", None))
        self.action_detail.setText(QCoreApplication.translate("MainWindow", u"Detail", None))
        self.action_e_e_normal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.action_e_e_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.action_emboss.setText(QCoreApplication.translate("MainWindow", u"Emboss", None))
        self.action_negative.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.action_sharpen.setText(QCoreApplication.translate("MainWindow", u"Sharpen", None))
        self.action_s_normal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.action_s_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.action_f_e_weak_detection.setText(QCoreApplication.translate("MainWindow", u"Weak Detection", None))
        self.action_f_e_medium_detection.setText(QCoreApplication.translate("MainWindow", u"Medium Detection", None))
        self.action_f_e_strong_detection.setText(QCoreApplication.translate("MainWindow", u"Strong Detection", None))
        self.action_about_app.setText(QCoreApplication.translate("MainWindow", u"App", None))
        self.action_about_img.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        # if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
        # endif // QT_CONFIG(shortcut)
        self.action_red_scale.setText(QCoreApplication.translate("MainWindow", u"Red Scale", None))
        self.action_green_scale.setText(QCoreApplication.translate("MainWindow", u"Green Scale", None))
        self.action_blue_scale.setText(QCoreApplication.translate("MainWindow", u"Blue Scale", None))
        self.action_logarithmic.setText(QCoreApplication.translate("MainWindow", u"Logarithmic", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p><span style=\" color:#e72258;\">Rotate &amp; Adjustments</span></p></body></html>",
                                                      None))
        # if QT_CONFIG(tooltip)
        self.btn_rotate.setToolTip(QCoreApplication.translate("MainWindow", u"Rotate 90\u00b0 Left", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_rotate.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_flip_h.setToolTip(QCoreApplication.translate("MainWindow", u"Flip Horizontaly", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_flip_h.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_flip_v.setToolTip(QCoreApplication.translate("MainWindow", u"Flip Verticaly", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_flip_v.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" color:#191a2b;\">Gamma Correction</span></p></body></html>",
                                                        None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" color:#191a2b;\">Transparency (%)</span></p></body></html>",
                                                        None))
        # if QT_CONFIG(tooltip)
        self.transpa_slider.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.btn_reset.setToolTip(QCoreApplication.translate("MainWindow", u"Revert You Image to the Original", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"  Reset", None))
        # if QT_CONFIG(tooltip)
        self.btn_open.setToolTip(QCoreApplication.translate("MainWindow", u"Open an Image...", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_open.setText("")
        self.image_label.setText("")
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_filters.setTitle(QCoreApplication.translate("MainWindow", u"Fil&ters", None))
        self.menu_edge_enhance.setTitle(QCoreApplication.translate("MainWindow", u"Edge Enhance", None))
        self.menu_smooth.setTitle(QCoreApplication.translate("MainWindow", u"Smooth", None))
        self.menu_find_edge.setTitle(QCoreApplication.translate("MainWindow", u"Find Edge", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.menu_about.setTitle(QCoreApplication.translate("MainWindow", u"&About", None))
    # retranslateUi
