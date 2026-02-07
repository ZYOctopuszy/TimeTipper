# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_time.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    Qt,
)
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTimeEdit,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(168, 136)
        Form.setStyleSheet(
            "/* \u57fa\u7840\u8bbe\u7f6e */\n"
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
            "\n"
            "/* \u6309\u94ae\u6837\u5f0f */\n"
            "QPushButton {\n"
            "    background-color: rgba(70, 150, 80, 0.9);\n"
            "    color: white;\n"
            "    border: 1px solid rgba(80, 150, 90, 0.7);\n"
            "    border-radius: 4px;\n"
            "    padding: 6px 12px;\n"
            "    min-width: 80px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(70, 140, 80, 0.9);\n"
            "    border-color: rgba(100, 170, 110, 0.8);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(30, 100, 40, 0.9);\n"
            "}\n"
            "\n"
            "/* \u65f6\u95f4"
            "\u8f93\u5165\u6846 */\n"
            "QTimeEdit {\n"
            "    background-color: rgba(40, 50, 40, 0.8);\n"
            "    border: 1px solid rgba(70, 90, 70, 0.7);\n"
            "    border-radius: 4px;\n"
            "    padding: 3px;\n"
            "    color: #e0e0e0;\n"
            "}\n"
            "\n"
            "QTimeEdit::up-button, QTimeEdit::down-button {\n"
            "    width: 16px;\n"
            "    border: none;\n"
            "    background: rgba(60, 80, 60, 0.7);\n"
            "}\n"
            "\n"
            "QTimeEdit::up-button:hover, QTimeEdit::down-button:hover {\n"
            "    background: rgba(80, 100, 80, 0.8);\n"
            "}"
        )
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.timeEdit = QTimeEdit(self.frame)
        self.timeEdit.setObjectName("timeEdit")

        self.gridLayout_2.addWidget(self.timeEdit, 2, 0, 1, 1)

        self.sure = QPushButton(self.frame)
        self.sure.setObjectName("sure")

        self.gridLayout_2.addWidget(self.sure, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(
            20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.sure.setText(QCoreApplication.translate("Form", "\u786e\u8ba4", None))
        self.label.setText(
            QCoreApplication.translate("Form", "\u6dfb\u52a0\u65f6\u95f4\u70b9", None)
        )

    # retranslateUi
