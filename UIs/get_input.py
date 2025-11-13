# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'get_input.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QWidget)

class Ui_get_input(object):
    def setupUi(self, get_input):
        if not get_input.objectName():
            get_input.setObjectName(u"get_input")
        get_input.resize(210, 92)
        get_input.setMinimumSize(QSize(210, 92))
        get_input.setMaximumSize(QSize(16777215, 92))
        icon = QIcon()
        icon.addFile(u"../icons/active.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        get_input.setWindowIcon(icon)
        get_input.setStyleSheet(u"/* \u57fa\u7840\u8bbe\u7f6e */\n"
"* {\n"
"    font-family: 'Microsoft YaHei', 'Segoe UI', sans-serif;\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"/* \u4e3b\u7a97\u53e3 */\n"
"QWidget#get_input {\n"
"    background-color: rgba(20, 30, 20, 0.95);\n"
"    border: 1px solid rgba(60, 90, 60, 0.7);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* \u6846\u67b6\u6837\u5f0f */\n"
"QFrame#frame {\n"
"    background-color: rgba(35, 45, 35, 0.8);\n"
"    border: 1px solid rgba(70, 90, 70, 0.6);\n"
"    border-radius: 6px;\n"
"}\n"
"/* \u6807\u7b7e\u6837\u5f0f */\n"
"QLabel {\n"
"    background: transparent;\n"
"}")
        self.gridLayout = QGridLayout(get_input)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(get_input)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.get_exe_name = QLineEdit(self.frame)
        self.get_exe_name.setObjectName(u"get_exe_name")
        self.get_exe_name.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.get_exe_name, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(get_input)

        QMetaObject.connectSlotsByName(get_input)
    # setupUi

    def retranslateUi(self, get_input):
        get_input.setWindowTitle(QCoreApplication.translate("get_input", u"\u6dfb\u52a0\u5f85\u6740\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("get_input", u"\u65b0\u5efa\u9879", None))
        self.get_exe_name.setPlaceholderText(QCoreApplication.translate("get_input", u"\u8bf7\u8f93\u5165\u53ef\u6267\u884c\u6587\u4ef6\u540d(\u542b\u540e\u7f00)", None))
    # retranslateUi

