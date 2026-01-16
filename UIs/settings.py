# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QListView, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(850, 567)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"/* \u57fa\u7840\u8bbe\u7f6e */\n"
"* {\n"
"    font-family: 'Microsoft YaHei', 'Segoe UI', sans-serif;\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"/* \u4e3b\u7a97\u53e3 */\n"
"QWidget#Form {\n"
"    background-color: rgba(20, 30, 20, 0.95);\n"
"    border: 1px solid rgba(60, 90, 60, 0.7);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u9875\u5bb9\u5668 */\n"
"QTabWidget::pane {\n"
"    border: 1px solid rgba(50, 80, 50, 0.0);\n"
"    background: rgba(30, 50, 30, 0.0);\n"
"    border-radius: 6px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u9875\u6807\u7b7e */\n"
"QTabBar::tab {\n"
"    background: rgba(40, 60, 40, 0.8);\n"
"    border: 1px solid rgba(70, 100, 70, 0.6);\n"
"    border-bottom: none;\n"
"    color: #b0d0b0;\n"
"    padding: 6px 12px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgba(60, 90, 60, 0.9);\n"
"    color: white;\n"
"    border-bottom: 1px solid rgba(60, 90, "
                        "60, 0.9);\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: rgba(80, 110, 80, 0.8);\n"
"    color: white;\n"
"}\n"
"\n"
"/* \u6309\u94ae\u57fa\u7840\u6837\u5f0f */\n"
"QPushButton {\n"
"    background-color: rgba(50, 120, 60, 0.85);\n"
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
"QPushButton:disabled {\n"
"    background-color: rgba(46, 125, 50, 0.7);\n"
"    color: rgba(200, 230, 200, 0.7);\n"
"    border-color: rgba(46, 125, 50, 0.6);\n"
"}\n"
"\n"
"/* \u7279\u6b8a\u6309\u94ae\u6837\u5f0f */\n"
"QPushButton#all_disable, QPushButton#all_enable {\n"
"    padding: 6px -15px;;\n"
"}\n"
"QPushButton#is_active {\n"
"    background-color: rgba(80, 160, 90, 0.85);\n"
"    borde"
                        "r-color: rgba(110, 190, 120, 0.7);\n"
"}\n"
"\n"
"QPushButton#is_active:hover {\n"
"    background-color: rgba(100, 180, 110, 0.9);\n"
"}\n"
"\n"
"QPushButton#test_button {\n"
"    background-color: rgba(120, 60, 50, 0.85);\n"
"    border-color: rgba(150, 90, 80, 0.7);\n"
"}\n"
"\n"
"QPushButton#test_button:hover {\n"
"    background-color: rgba(140, 80, 70, 0.9);\n"
"}\n"
"\n"
"/* \u5217\u8868\u548c\u6587\u672c\u7f16\u8f91\u6846 */\n"
"QListWidget, QTextEdit {\n"
"    background-color: rgba(40, 50, 40, 0.0);\n"
"    border: 1px solid rgba(70, 90, 70, 0.7);\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #e0e0e0;\n"
"    selection-background-color: rgba(60, 120, 70, 0.7);\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* \u590d\u9009\u6846 */\n"
"QCheckBox {\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid rgba(90, 120, 90, 0.7);\n"
"    border-radius: 3px;\n"
""
                        "    background: rgba(50, 60, 50, 0.8);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(60, 130, 70, 0.9);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: rgba(70, 80, 70, 0.3);\n"
"}\n"
"\n"
"/* \u6570\u503c\u8f93\u5165\u6846 */\n"
"QSpinBox {\n"
"    background-color: rgba(40, 50, 40, 0.8);\n"
"    border: 1px solid rgba(70, 90, 70, 0.7);\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    width: 16px;\n"
"    border: none;\n"
"    background: rgba(60, 80, 60, 0.7);\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(80, 100, 80, 0.8);\n"
"}\n"
"\n"
"/* \u6846\u67b6\u6837\u5f0f */\n"
"QFrame#frame_2, #frame_4{\n"
"    background-color: rgba(35, 45, 35, 0.1);\n"
"    border: 1px solid rgba(70, 90, 70, 0.6);\n"
"    border-radius: 6px;\n"
"}\n"
"QFrame#frame {\n"
"    backgroud-color: rgba(35, 45, 35, 0.0);\n"
"    border: 1px solid rgba(70, 90,"
                        " 70, 0.6);\n"
"    border-radius: 6px;\n"
"}\n"
"QFrame#frame_3 {\n"
"    background-color: rgba(35, 45, 35, 0.8);\n"
"    border: 1px solid rgba(70, 90, 70, 0.6);\n"
"    border-radius: 6px;\n"
"}\n"
"QFrame#main_frame {\n"
"    background-color: rgb(35, 45, 35);\n"
"    border: 1px solid rgba(70, 90, 80 ,0.6);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u6837\u5f0f */\n"
"QLabel {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* \u5173\u4e8e\u9875\u5927\u6807\u9898 */\n"
"QLabel#label {\n"
"    color: rgba(100, 220, 120, 0.9);\n"
"}\n"
"\n"
"/* \u5206\u9694\u7ebf */\n"
"QFrame[frameShape=\"4\"], QFrame[frameShape=\"5\"] {\n"
"    background-color: rgba(70, 90, 70, 0.0);\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761 */\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    background: rgba(40, 50, 40, 0.5);\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical, QScrollBar:"
                        ":handle:horizontal {\n"
"    background: rgba(80, 120, 80, 0.6);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"/* \u5de5\u5177\u63d0\u793a */\n"
"QToolTip {\n"
"    background-color: rgba(40, 50, 40, 0.95);\n"
"    color: #e0e0e0;\n"
"    border: 1px solid rgba(70, 100, 70, 0.8);\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"/* \u6dfb\u52a0\u6309\u94ae(+) */\n"
"QPushButton[text=\"+\"], \n"
"QPushButton[text=\"\u6dfb\u52a0\"] {\n"
"    background-color: rgba(70, 150, 80, 0.9)"
                        ";\n"
"}\n"
"\n"
"/* \u5220\u9664\u6309\u94ae(-) */\n"
"QPushButton[text=\"-\"], \n"
"QPushButton[text=\"\u5220\u9664\"] {\n"
"    background-color: rgba(150, 70, 60, 0.9);\n"
"}\n"
"\n"
"/* \u5e94\u7528\u6309\u94ae\u7279\u6b8a\u6837\u5f0f */\n"
"QPushButton[text=\"\u5e94\u7528(Alt+A)\"] {\n"
"    background-color: rgba(80, 140, 90, 0.9);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* \u9000\u51fa\u6309\u94ae\u7279\u6b8a\u6837\u5f0f */\n"
"QPushButton[text=\"\u9000\u51fa(Ctrl+Q)\"] {\n"
"    background-color: rgba(120, 60, 50, 0.85);\n"
"}")
        self.gridLayout_10 = QGridLayout(Form)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setCursor(QCursor(Qt.CursorShape.SizeAllCursor))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.show_icon = QLabel(self.frame_4)
        self.show_icon.setObjectName(u"show_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_icon.sizePolicy().hasHeightForWidth())
        self.show_icon.setSizePolicy(sizePolicy)
        self.show_icon.setMaximumSize(QSize(30, 30))
        self.show_icon.setPixmap(QPixmap(u"C:/Users/Z_Oct/.designer/icons/active.png"))
        self.show_icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.show_icon)

        self.show_name = QLabel(self.frame_4)
        self.show_name.setObjectName(u"show_name")
        sizePolicy.setHeightForWidth(self.show_name.sizePolicy().hasHeightForWidth())
        self.show_name.setSizePolicy(sizePolicy)
        self.show_name.setScaledContents(True)

        self.horizontalLayout.addWidget(self.show_name)


        self.gridLayout_10.addWidget(self.frame_4, 1, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.minimize_button = QPushButton(self.frame_2)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.minimize_button.setStyleSheet(u"/* \u6700\u5c0f\u5316\u6309\u94ae\u6837\u5f0f - \u6697\u8272\u4e3b\u9898\u4e0e\u7eff\u8272\u8c03\u534f\u8c03 */\n"
"QPushButton#minimize_button {\n"
"    background-color: rgba(50, 60, 50, 0.85);  /* \u6df1\u7eff\u8272\u8c03\u80cc\u666f */\n"
"    border: 1px solid rgba(80, 100, 80, 0.7);  /* \u6d45\u7eff\u8272\u8fb9\u6846 */\n"
"    border-radius: 4px;\n"
"    color: #f0f0f0;\n"
"    padding: 4px;\n"
"    min-width: 20px;\n"
"    max-width: 20px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    font-weight: bold;\n"
"    qproperty-text: \"-\";  /* \u4f7f\u7528\u4e0b\u5212\u7ebf\u4f5c\u4e3a\u6700\u5c0f\u5316\u7b26\u53f7 */\n"
"}\n"
"\n"
"/* \u60ac\u505c\u72b6\u6001 - \u589e\u5f3a\u7eff\u8272\u8c03 */\n"
"QPushButton#minimize_button:hover {\n"
"    background-color: rgba(70, 90, 70, 0.9);\n"
"    border-color: rgba(100, 130, 100, 0.8);\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u72b6\u6001 */\n"
"QPushButton#minimize_button:pressed {\n"
"    background-color: rgba(90, 110, 90, 0.9);\n"
"    border-color: rgba(12"
                        "0, 150, 120, 0.8);\n"
"}\n"
"\n"
"/* \u7981\u7528\u72b6\u6001 */\n"
"QPushButton#minimize_button:disabled {\n"
"    background-color: rgba(50, 60, 50, 0.6);\n"
"    border-color: rgba(70, 80, 70, 0.5);\n"
"    color: rgba(180, 180, 180, 0.5);\n"
"}")

        self.gridLayout_11.addWidget(self.minimize_button, 0, 0, 1, 1)

        self.close_button = QPushButton(self.frame_2)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.close_button.setStyleSheet(u"QPushButton#close_button {\n"
"    background-color: rgba(80, 40, 40, 0.85);  /* \u6df1\u7ea2\u8910\u8272\u80cc\u666f */\n"
"    border: 1px solid rgba(120, 60, 60, 0.7);  /* \u7ea2\u8910\u8272\u8fb9\u6846 */\n"
"    border-radius: 4px;\n"
"    color: #f0f0f0;\n"
"    padding: 4px;\n"
"    min-width: 20px;\n"
"    max-width: 20px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    font-weight: bold;\n"
"    qproperty-text: \"\u00d7\";  /* \u4f7f\u7528\u4e58\u53f7\u4f5c\u4e3a\u5173\u95ed\u7b26\u53f7 */\n"
"}\n"
"\n"
"/* \u60ac\u505c\u72b6\u6001 - \u589e\u5f3a\u7ea2\u8272\u8c03\u4f46\u4ecd\u4fdd\u6301\u534f\u8c03 */\n"
"QPushButton#close_button:hover {\n"
"    background-color: rgba(120, 60, 60, 0.9);\n"
"    border-color: rgba(150, 80, 80, 0.8);\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u72b6\u6001 */\n"
"QPushButton#close_button:pressed {\n"
"    background-color: rgba(150, 70, 70, 0.9);\n"
"    border-color: rgba(180, 90, 90, 0.8);\n"
"}\n"
"\n"
"/* \u7981\u7528\u72b6\u6001 */\n"
"QPushButton#close_button:disab"
                        "led {\n"
"    background-color: rgba(60, 50, 50, 0.6);\n"
"    border-color: rgba(80, 70, 70, 0.5);\n"
"    color: rgba(180, 180, 180, 0.5);\n"
"}")

        self.gridLayout_11.addWidget(self.close_button, 0, 2, 1, 1)


        self.gridLayout_10.addWidget(self.frame_2, 1, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.resize_label = QLabel(self.frame_5)
        self.resize_label.setObjectName(u"resize_label")
        self.resize_label.setAutoFillBackground(False)

        self.gridLayout_14.addWidget(self.resize_label, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_5, 4, 2, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)

        self.main_frame = QFrame(Form)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.main_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.exit_button = QPushButton(self.main_frame)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.exit_button, 2, 0, 1, 1)

        self.apply_button = QPushButton(self.main_frame)
        self.apply_button.setObjectName(u"apply_button")
        self.apply_button.setEnabled(False)
        self.apply_button.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout.addWidget(self.apply_button, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.tabWidget = QTabWidget(self.main_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setBold(True)
        font.setKerning(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.times = QWidget()
        self.times.setObjectName(u"times")
        self.gridLayout_2 = QGridLayout(self.times)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.description_tip = QLabel(self.times)
        self.description_tip.setObjectName(u"description_tip")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.description_tip.sizePolicy().hasHeightForWidth())
        self.description_tip.setSizePolicy(sizePolicy1)
        self.description_tip.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.description_tip, 0, 2, 1, 1)

        self.all_enable = QPushButton(self.times)
        self.all_enable.setObjectName(u"all_enable")

        self.gridLayout_2.addWidget(self.all_enable, 2, 4, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.time_tip = QLabel(self.times)
        self.time_tip.setObjectName(u"time_tip")
        sizePolicy1.setHeightForWidth(self.time_tip.sizePolicy().hasHeightForWidth())
        self.time_tip.setSizePolicy(sizePolicy1)
        self.time_tip.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.time_tip, 0, 1, 1, 1)

        self.description = QTextEdit(self.times)
        self.description.setObjectName(u"description")

        self.gridLayout_2.addWidget(self.description, 1, 2, 5, 1)

        self.time_list = QListWidget(self.times)
        self.time_list.setObjectName(u"time_list")
        self.time_list.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.time_list.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.time_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.time_list.setMovement(QListView.Movement.Static)
        self.time_list.setFlow(QListView.Flow.TopToBottom)
        self.time_list.setResizeMode(QListView.ResizeMode.Fixed)
        self.time_list.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.time_list.setViewMode(QListView.ViewMode.ListMode)

        self.gridLayout_2.addWidget(self.time_list, 1, 1, 5, 1)

        self.all_disable = QPushButton(self.times)
        self.all_disable.setObjectName(u"all_disable")

        self.gridLayout_2.addWidget(self.all_disable, 2, 3, 1, 1)

        self.add_button = QPushButton(self.times)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.add_button, 3, 3, 1, 2)

        self.delete_button = QPushButton(self.times)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.delete_button, 4, 3, 1, 2)

        self.edit_button = QPushButton(self.times)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.edit_button.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.edit_button, 5, 3, 1, 2)

        self.tabWidget.addTab(self.times, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.gridLayout_5 = QGridLayout(self.settings)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.is_active = QPushButton(self.settings)
        self.is_active.setObjectName(u"is_active")
        self.is_active.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.is_active, 0, 2, 1, 1)

        self.frame = QFrame(self.settings)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 3, 0, 1, 1)

        self.if_tray_hide = QCheckBox(self.frame)
        self.if_tray_hide.setObjectName(u"if_tray_hide")
        self.if_tray_hide.setEnabled(True)
        self.if_tray_hide.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.if_tray_hide.setCheckable(True)
        self.if_tray_hide.setChecked(False)

        self.gridLayout_7.addWidget(self.if_tray_hide, 0, 0, 1, 4)

        self.b = QSpinBox(self.frame)
        self.b.setObjectName(u"b")
        self.b.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.b.setMaximum(999999999)

        self.gridLayout_7.addWidget(self.b, 2, 3, 1, 1)

        self.if_strong_hide = QCheckBox(self.frame)
        self.if_strong_hide.setObjectName(u"if_strong_hide")
        self.if_strong_hide.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_7.addWidget(self.if_strong_hide, 1, 0, 1, 4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 4, 0, 1, 4)

        self.hold_seconds = QSpinBox(self.frame)
        self.hold_seconds.setObjectName(u"hold_seconds")
        self.hold_seconds.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.hold_seconds.setMaximum(999999999)

        self.gridLayout_7.addWidget(self.hold_seconds, 3, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.label_4, 2, 2, 1, 1)

        self.a = QSpinBox(self.frame)
        self.a.setObjectName(u"a")
        self.a.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.a.setMaximum(999999999)

        self.gridLayout_7.addWidget(self.a, 2, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 3, 1)

        self.test_button = QPushButton(self.settings)
        self.test_button.setObjectName(u"test_button")
        self.test_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.test_button, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 1, 3, 1)

        self.tabWidget.addTab(self.settings, "")
        self.executables = QWidget()
        self.executables.setObjectName(u"executables")
        self.gridLayout_6 = QGridLayout(self.executables)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget_2 = QTabWidget(self.executables)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.exe = QWidget()
        self.exe.setObjectName(u"exe")
        self.gridLayout_8 = QGridLayout(self.exe)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.edit_exe_button = QPushButton(self.exe)
        self.edit_exe_button.setObjectName(u"edit_exe_button")
        self.edit_exe_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_8.addWidget(self.edit_exe_button, 2, 1, 1, 1)

        self.remove_exe = QPushButton(self.exe)
        self.remove_exe.setObjectName(u"remove_exe")
        self.remove_exe.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_8.addWidget(self.remove_exe, 4, 1, 1, 1)

        self.add_exe = QPushButton(self.exe)
        self.add_exe.setObjectName(u"add_exe")
        self.add_exe.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_8.addWidget(self.add_exe, 3, 1, 1, 1)

        self.choose_exe = QPushButton(self.exe)
        self.choose_exe.setObjectName(u"choose_exe")
        self.choose_exe.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_8.addWidget(self.choose_exe, 1, 1, 1, 1)

        self.for_kill_list = QListWidget(self.exe)
        self.for_kill_list.setObjectName(u"for_kill_list")

        self.gridLayout_8.addWidget(self.for_kill_list, 0, 0, 5, 1)

        self.tabWidget_2.addTab(self.exe, "")
        self.title = QWidget()
        self.title.setObjectName(u"title")
        self.gridLayout_9 = QGridLayout(self.title)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.remove_title = QPushButton(self.title)
        self.remove_title.setObjectName(u"remove_title")
        self.remove_title.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_9.addWidget(self.remove_title, 3, 1, 1, 1)

        self.add_title = QPushButton(self.title)
        self.add_title.setObjectName(u"add_title")
        self.add_title.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_9.addWidget(self.add_title, 2, 1, 1, 1)

        self.edit_title_button = QPushButton(self.title)
        self.edit_title_button.setObjectName(u"edit_title_button")
        self.edit_title_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_9.addWidget(self.edit_title_button, 1, 1, 1, 1)

        self.for_close_title = QListWidget(self.title)
        self.for_close_title.setObjectName(u"for_close_title")

        self.gridLayout_9.addWidget(self.for_close_title, 0, 0, 4, 1)

        self.tabWidget_2.addTab(self.title, "")

        self.gridLayout_6.addWidget(self.tabWidget_2, 2, 1, 1, 1)

        self.tabWidget.addTab(self.executables, "")
        self.weekdays = QWidget()
        self.weekdays.setObjectName(u"weekdays")
        self.gridLayout_13 = QGridLayout(self.weekdays)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.add_day = QPushButton(self.weekdays)
        self.add_day.setObjectName(u"add_day")
        self.add_day.setStyleSheet(u"/* \u6700\u5c0f\u5316\u6309\u94ae\u6837\u5f0f - \u6697\u8272\u4e3b\u9898\u4e0e\u7eff\u8272\u8c03\u534f\u8c03 */\n"
"QPushButton#add_day {\n"
"    background-color: rgba(80, 100, 80, 0.85);  /* \u6df1\u7eff\u8272\u8c03\u80cc\u666f */\n"
"    border: 1px solid rgba(80, 100, 80, 0.7);  /* \u6d45\u7eff\u8272\u8fb9\u6846 */\n"
"    border-radius: 4px;\n"
"    color: #f0f0f0;\n"
"    padding: 4px;\n"
"    min-width: 20px;\n"
"    max-width: 20px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    font-weight: bold;\n"
"    qproperty-text: \"+\";  /* \u4f7f\u7528\u4e0b\u5212\u7ebf\u4f5c\u4e3a\u6700\u5c0f\u5316\u7b26\u53f7 */\n"
"}\n"
"\n"
"/* \u60ac\u505c\u72b6\u6001 - \u589e\u5f3a\u7eff\u8272\u8c03 */\n"
"QPushButton#minimize_button:hover {\n"
"    background-color: rgba(70, 90, 70, 0.9);\n"
"    border-color: rgba(100, 130, 100, 0.8);\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u72b6\u6001 */\n"
"QPushButton#minimize_button:pressed {\n"
"    background-color: rgba(90, 110, 90, 0.9);\n"
"    border-color: rgba(120, 150,"
                        " 120, 0.8);\n"
"}\n"
"\n"
"/* \u7981\u7528\u72b6\u6001 */\n"
"QPushButton#minimize_button:disabled {\n"
"    background-color: rgba(50, 60, 50, 0.6);\n"
"    border-color: rgba(70, 80, 70, 0.5);\n"
"    color: rgba(180, 180, 180, 0.5);\n"
"}")

        self.gridLayout_13.addWidget(self.add_day, 0, 7, 1, 1)

        self.del_day = QPushButton(self.weekdays)
        self.del_day.setObjectName(u"del_day")
        self.del_day.setStyleSheet(u"/* \u6700\u5c0f\u5316\u6309\u94ae\u6837\u5f0f - \u6697\u8272\u4e3b\u9898\u4e0e\u7eff\u8272\u8c03\u534f\u8c03 */\n"
"QPushButton#del_day {\n"
"    background-color: rgba(80, 100, 80, 0.85);  /* \u6df1\u7eff\u8272\u8c03\u80cc\u666f */\n"
"    border: 1px solid rgba(80, 100, 80, 0.7);  /* \u6d45\u7eff\u8272\u8fb9\u6846 */\n"
"    border-radius: 4px;\n"
"    color: #f0f0f0;\n"
"    padding: 4px;\n"
"    min-width: 20px;\n"
"    max-width: 20px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    font-weight: bold;\n"
"    qproperty-text: \"-\";  /* \u4f7f\u7528\u4e0b\u5212\u7ebf\u4f5c\u4e3a\u6700\u5c0f\u5316\u7b26\u53f7 */\n"
"}\n"
"\n"
"/* \u60ac\u505c\u72b6\u6001 - \u589e\u5f3a\u7eff\u8272\u8c03 */\n"
"QPushButton#minimize_button:hover {\n"
"    background-color: rgba(70, 90, 70, 0.9);\n"
"    border-color: rgba(100, 130, 100, 0.8);\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u72b6\u6001 */\n"
"QPushButton#minimize_button:pressed {\n"
"    background-color: rgba(90, 110, 90, 0.9);\n"
"    border-color: rgba(120, 150,"
                        " 120, 0.8);\n"
"}\n"
"\n"
"/* \u7981\u7528\u72b6\u6001 */\n"
"QPushButton#minimize_button:disabled {\n"
"    background-color: rgba(50, 60, 50, 0.6);\n"
"    border-color: rgba(70, 80, 70, 0.5);\n"
"    color: rgba(180, 180, 180, 0.5);\n"
"}")

        self.gridLayout_13.addWidget(self.del_day, 1, 7, 1, 1)

        self.del_lesson = QPushButton(self.weekdays)
        self.del_lesson.setObjectName(u"del_lesson")
        self.del_lesson.setStyleSheet(u"/* \u6700\u5c0f\u5316\u6309\u94ae\u6837\u5f0f - \u6697\u8272\u4e3b\u9898\u4e0e\u7eff\u8272\u8c03\u534f\u8c03 */\n"
"QPushButton#del_lesson {\n"
"    background-color: rgba(80, 100, 80, 0.85);  /* \u6df1\u7eff\u8272\u8c03\u80cc\u666f */\n"
"    border: 1px solid rgba(80, 100, 80, 0.7);  /* \u6d45\u7eff\u8272\u8fb9\u6846 */\n"
"    border-radius: 4px;\n"
"    color: #f0f0f0;\n"
"    padding: 4px;\n"
"    min-width: 20px;\n"
"    max-width: 20px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    font-weight: bold;\n"
"    qproperty-text: \"-\";  /* \u4f7f\u7528\u4e0b\u5212\u7ebf\u4f5c\u4e3a\u6700\u5c0f\u5316\u7b26\u53f7 */\n"
"}\n"
"\n"
"/* \u60ac\u505c\u72b6\u6001 - \u589e\u5f3a\u7eff\u8272\u8c03 */\n"
"QPushButton#minimize_button:hover {\n"
"    background-color: rgba(70, 90, 70, 0.9);\n"
"    border-color: rgba(100, 130, 100, 0.8);\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u72b6\u6001 */\n"
"QPushButton#minimize_button:pressed {\n"
"    background-color: rgba(90, 110, 90, 0.9);\n"
"    border-color: rgba(120, 1"
                        "50, 120, 0.8);\n"
"}\n"
"\n"
"/* \u7981\u7528\u72b6\u6001 */\n"
"QPushButton#minimize_button:disabled {\n"
"    background-color: rgba(50, 60, 50, 0.6);\n"
"    border-color: rgba(70, 80, 70, 0.5);\n"
"    color: rgba(180, 180, 180, 0.5);\n"
"}")

        self.gridLayout_13.addWidget(self.del_lesson, 7, 1, 1, 1)

        self.add_lesson = QPushButton(self.weekdays)
        self.add_lesson.setObjectName(u"add_lesson")
        self.add_lesson.setStyleSheet(u"/* \u6700\u5c0f\u5316\u6309\u94ae\u6837\u5f0f - \u6697\u8272\u4e3b\u9898\u4e0e\u7eff\u8272\u8c03\u534f\u8c03 */\n"
"QPushButton#add_lesson {\n"
"    background-color: rgba(80, 100, 80, 0.85);  /* \u6df1\u7eff\u8272\u8c03\u80cc\u666f */\n"
"    border: 1px solid rgba(80, 100, 80, 0.7);  /* \u6d45\u7eff\u8272\u8fb9\u6846 */\n"
"    border-radius: 4px;\n"
"    color: #f0f0f0;\n"
"    padding: 4px;\n"
"    min-width: 20px;\n"
"    max-width: 20px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    font-weight: bold;\n"
"    qproperty-text: \"+\";  /* \u4f7f\u7528\u4e0b\u5212\u7ebf\u4f5c\u4e3a\u6700\u5c0f\u5316\u7b26\u53f7 */\n"
"}\n"
"\n"
"/* \u60ac\u505c\u72b6\u6001 - \u589e\u5f3a\u7eff\u8272\u8c03 */\n"
"QPushButton#minimize_button:hover {\n"
"    background-color: rgba(70, 90, 70, 0.9);\n"
"    border-color: rgba(100, 130, 100, 0.8);\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u72b6\u6001 */\n"
"QPushButton#minimize_button:pressed {\n"
"    background-color: rgba(90, 110, 90, 0.9);\n"
"    border-color: rgba(120, 1"
                        "50, 120, 0.8);\n"
"}\n"
"\n"
"/* \u7981\u7528\u72b6\u6001 */\n"
"QPushButton#minimize_button:disabled {\n"
"    background-color: rgba(50, 60, 50, 0.6);\n"
"    border-color: rgba(70, 80, 70, 0.5);\n"
"    color: rgba(180, 180, 180, 0.5);\n"
"}")

        self.gridLayout_13.addWidget(self.add_lesson, 7, 0, 1, 1)

        self.time_table = QTableWidget(self.weekdays)
        if (self.time_table.columnCount() < 5):
            self.time_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.time_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.time_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.time_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.time_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.time_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.time_table.rowCount() < 8):
            self.time_table.setRowCount(8)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.time_table.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.time_table.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.time_table.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.time_table.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.time_table.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.time_table.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.time_table.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.time_table.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.time_table.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.time_table.setItem(0, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.time_table.setItem(0, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.time_table.setItem(0, 3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.time_table.setItem(0, 4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.time_table.setItem(1, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.time_table.setItem(1, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.time_table.setItem(1, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.time_table.setItem(1, 3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.time_table.setItem(1, 4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.time_table.setItem(2, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.time_table.setItem(2, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.time_table.setItem(2, 2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.time_table.setItem(2, 3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.time_table.setItem(2, 4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.time_table.setItem(3, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.time_table.setItem(3, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.time_table.setItem(3, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.time_table.setItem(3, 3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.time_table.setItem(3, 4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.time_table.setItem(4, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.time_table.setItem(4, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.time_table.setItem(4, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.time_table.setItem(4, 3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.time_table.setItem(4, 4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.time_table.setItem(5, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.time_table.setItem(5, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.time_table.setItem(5, 2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.time_table.setItem(5, 3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.time_table.setItem(5, 4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.time_table.setItem(6, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.time_table.setItem(6, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.time_table.setItem(6, 2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.time_table.setItem(6, 3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.time_table.setItem(6, 4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.time_table.setItem(7, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.time_table.setItem(7, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.time_table.setItem(7, 2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.time_table.setItem(7, 3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.time_table.setItem(7, 4, __qtablewidgetitem52)
        self.time_table.setObjectName(u"time_table")
        sizePolicy.setHeightForWidth(self.time_table.sizePolicy().hasHeightForWidth())
        self.time_table.setSizePolicy(sizePolicy)
        self.time_table.setStyleSheet(u"/* QTableWidget \u4e3b\u6837\u5f0f */\n"
"QTableWidget {\n"
"    background-color: rgba(40, 50, 40, 0.0);  /* \u5b8c\u5168\u900f\u660e\u80cc\u666f */\n"
"    border: 1px solid rgba(70, 90, 70, 0.7);\n"
"    border-radius: 4px;\n"
"    gridline-color: rgba(70, 90, 70, 0.4);\n"
"    color: #e0e0e0;\n"
"    selection-background-color: rgba(60, 120, 70, 0.7);\n"
"    selection-color: white;\n"
"    outline: 0;  /* \u79fb\u9664\u9009\u4e2d\u65f6\u7684\u865a\u7ebf\u6846 */\n"
"}\n"
"\n"
"/* \u8868\u5934\u6837\u5f0f */\n"
"QHeaderView {\n"
"    background-color: rgba(40, 60, 40, 0.8);\n"
"    border: none;\n"
"    border-radius: 0;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(50, 70, 50, 0.9);\n"
"    color: #b0d0b0;\n"
"    padding: 6px;\n"
"    border: 1px solid rgba(70, 100, 70, 0.6);\n"
"    border-left: none;\n"
"    border-top: none;\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"    border-left: 1px solid rgba(70, 100, 70, 0.6);\n"
"}\n"
"\n"
"QHeaderView::"
                        "section:checked {\n"
"    background-color: rgba(60, 90, 60, 0.9);\n"
"    color: white;\n"
"}\n"
"\n"
"/* \u8868\u9879\u6837\u5f0f */\n"
"QTableWidget::item {\n"
"    padding: 4px 8px;\n"
"    border-bottom: 1px solid rgba(70, 90, 70, 0.3);\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: rgba(60, 80, 60, 0.4);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(60, 120, 70, 0.7);\n"
"    color: white;\n"
"}\n"
"\n"
"/* \u4ea4\u66ff\u884c\u989c\u8272 */\n"
"QTableWidget::item:alternate {\n"
"    background-color: rgba(45, 55, 45, 0.2);\n"
"}\n"
"\n"
"/* \u89d2\u90e8\u6309\u94ae\u6837\u5f0f */\n"
"QTableCornerButton::section {\n"
"    background-color: rgba(50, 70, 50, 0.9);\n"
"    border: 1px solid rgba(70, 100, 70, 0.6);\n"
"    border-left: none;\n"
"    border-top: none;\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761\u6837\u5f0f\uff08\u4e0e\u4e3b\u6837\u5f0f\u4e00\u81f4\uff09 */\n"
"QTableWidget QScrollBar:vertical {\n"
"    background: rgba(40, 50, 40, 0.5);\n"
"    width"
                        ": 10px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::handle:vertical {\n"
"    background: rgba(80, 120, 80, 0.6);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTableWidget QScrollBar::add-line:vertical, \n"
"QTableWidget QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* \u7f16\u8f91\u72b6\u6001\u4e0b\u7684\u6837\u5f0f */\n"
"QTableWidget::item:editing {\n"
"    background-color: rgba(60, 80, 60, 0.6);\n"
"}")
        self.time_table.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.time_table.setGridStyle(Qt.PenStyle.DashDotLine)
        self.time_table.setSortingEnabled(False)
        self.time_table.horizontalHeader().setVisible(True)
        self.time_table.horizontalHeader().setCascadingSectionResizes(False)

        self.gridLayout_13.addWidget(self.time_table, 0, 0, 3, 6)

        self.tabWidget.addTab(self.weekdays, "")
        self.log = QWidget()
        self.log.setObjectName(u"log")
        self.gridLayout_12 = QGridLayout(self.log)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.logger = QTextBrowser(self.log)
        self.logger.setObjectName(u"logger")
        self.logger.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.logger.setStyleSheet(u"gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.logger.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.logger.setOpenExternalLinks(True)

        self.gridLayout_12.addWidget(self.logger, 0, 0, 1, 1)

        self.tabWidget.addTab(self.log, "")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.gridLayout_4 = QGridLayout(self.about)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.about)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(69)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.about)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.about, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 3)

        self.tabWidget.raise_()
        self.exit_button.raise_()
        self.apply_button.raise_()

        self.gridLayout_10.addWidget(self.main_frame, 3, 1, 1, 2)

        QWidget.setTabOrder(self.time_list, self.add_button)
        QWidget.setTabOrder(self.add_button, self.delete_button)
        QWidget.setTabOrder(self.delete_button, self.edit_button)
        QWidget.setTabOrder(self.edit_button, self.if_tray_hide)
        QWidget.setTabOrder(self.if_tray_hide, self.if_strong_hide)
        QWidget.setTabOrder(self.if_strong_hide, self.a)
        QWidget.setTabOrder(self.a, self.b)
        QWidget.setTabOrder(self.b, self.hold_seconds)
        QWidget.setTabOrder(self.hold_seconds, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.for_kill_list)
        QWidget.setTabOrder(self.for_kill_list, self.choose_exe)
        QWidget.setTabOrder(self.choose_exe, self.edit_exe_button)
        QWidget.setTabOrder(self.edit_exe_button, self.add_exe)
        QWidget.setTabOrder(self.add_exe, self.remove_exe)
        QWidget.setTabOrder(self.remove_exe, self.for_close_title)
        QWidget.setTabOrder(self.for_close_title, self.edit_title_button)
        QWidget.setTabOrder(self.edit_title_button, self.add_title)
        QWidget.setTabOrder(self.add_title, self.remove_title)
        QWidget.setTabOrder(self.remove_title, self.description)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u90a3\u523b\u590f", None))
        self.show_icon.setText("")
        self.show_name.setText(QCoreApplication.translate("Form", u"\u90a3\u523b\u590f", None))
        self.minimize_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.close_button.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.resize_label.setText(QCoreApplication.translate("Form", u"\u21f2\u25e2", None))
        self.exit_button.setText(QCoreApplication.translate("Form", u"\u9000\u51fa(Ctrl+Q)", None))
#if QT_CONFIG(tooltip)
        self.apply_button.setToolTip(QCoreApplication.translate("Form", u"\u4e00\u4e9b\u8bbe\u7f6e\u66f4\u6539\u540e\u8981\u5e94\u7528\u624d\u4f1a\u4fdd\u5b58", None))
#endif // QT_CONFIG(tooltip)
        self.apply_button.setText(QCoreApplication.translate("Form", u"\u5e94\u7528(Alt+A)", None))
#if QT_CONFIG(accessibility)
        self.times.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.description_tip.setText(QCoreApplication.translate("Form", u"\u63cf\u8ff0", None))
        self.all_enable.setText(QCoreApplication.translate("Form", u"\u5168\u90e8\u542f\u7528", None))
        self.time_tip.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4", None))
        self.all_disable.setText(QCoreApplication.translate("Form", u"\u5168\u90e8\u7981\u7528", None))
        self.add_button.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.edit_button.setText(QCoreApplication.translate("Form", u"\u4fee\u6539", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.times), QCoreApplication.translate("Form", u"\u65f6\u95f4", None))
#if QT_CONFIG(tooltip)
        self.is_active.setToolTip(QCoreApplication.translate("Form", u"\u70b9\u51fb\u5207\u6362\u6fc0\u6d3b\u72b6\u6001", None))
#endif // QT_CONFIG(tooltip)
        self.is_active.setText(QCoreApplication.translate("Form", u"\u5de5\u4f5c\u4e2d", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Form", u"\u4e0b\u8bfe\u540e\u591a\u957f\u65f6\u95f4\u5185\u4e0d\u53ef\u4ee5\u518d\u6b21\u6253\u5f00\u6559\u5b66\u8f6f\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6301\u7eed\u65f6\u95f4(\u79d2)", None))
#if QT_CONFIG(tooltip)
        self.if_tray_hide.setToolTip(QCoreApplication.translate("Form", u"\u5c06\u6258\u76d8\u56fe\u6807\u8bbe\u7f6e\u4e3a\u900f\u660e\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.if_tray_hide.setText(QCoreApplication.translate("Form", u"\u9690\u85cf\u6258\u76d8                                                                                      ", None))
#if QT_CONFIG(tooltip)
        self.b.setToolTip(QCoreApplication.translate("Form", u"\u5ef6\u8fdf\u6700\u5927\u503c", None))
#endif // QT_CONFIG(tooltip)
        self.if_strong_hide.setText(QCoreApplication.translate("Form", u"\u5f3a\u529b\u9690\u85cf\u6a21\u5f0f(\u8bf7\u4f7f\u7528ctrl+win+alt+shift+f6\u6253\u5f00\u8bbe\u7f6e, \u6258\u76d8\u56fe\u6807\u5c06\u6d88\u5931)", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form", u"\u5f53\u4e0b\u8bfe\u540e\u4f1a\u968f\u673a\u5728\u8fd9\u4e2a\u8303\u56f4\u5185\u53d6\u503c\u4f5c\u4e3a\u5ef6\u8fdf, \u7136\u540e\u7b49\u5f85\u5ef6\u8fdf\u540e\u518d\u6740\u7a0b\u5e8f", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"\u968f\u673a\u7b49\u5f85\u65f6\u95f4(\u79d2)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"~", None))
#if QT_CONFIG(tooltip)
        self.a.setToolTip(QCoreApplication.translate("Form", u"\u5ef6\u8fdf\u6700\u5c0f\u503c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.test_button.setToolTip(QCoreApplication.translate("Form", u"\u6a21\u62df\u4e00\u6b21\u4e0b\u8bfe", None))
#endif // QT_CONFIG(tooltip)
        self.test_button.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.edit_exe_button.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91", None))
        self.remove_exe.setText(QCoreApplication.translate("Form", u"-", None))
        self.add_exe.setText(QCoreApplication.translate("Form", u"+", None))
        self.choose_exe.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.exe), QCoreApplication.translate("Form", u"\u5e94\u7528\u7a0b\u5e8fexe", None))
        self.remove_title.setText(QCoreApplication.translate("Form", u"-", None))
        self.add_title.setText(QCoreApplication.translate("Form", u"+", None))
        self.edit_title_button.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.title), QCoreApplication.translate("Form", u"\u7a97\u53e3\u6807\u9898", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.executables), QCoreApplication.translate("Form", u"\u7a0b\u5e8f", None))
        self.add_day.setText(QCoreApplication.translate("Form", u"+", None))
        self.del_day.setText(QCoreApplication.translate("Form", u"-", None))
        self.del_lesson.setText(QCoreApplication.translate("Form", u"-", None))
        self.add_lesson.setText(QCoreApplication.translate("Form", u"+", None))
        ___qtablewidgetitem = self.time_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u5468\u4e00", None));
        ___qtablewidgetitem1 = self.time_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u5468\u4e8c", None));
        ___qtablewidgetitem2 = self.time_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u5468\u4e09", None));
        ___qtablewidgetitem3 = self.time_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u5468\u56db", None));
        ___qtablewidgetitem4 = self.time_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u5468\u4e94", None));
        ___qtablewidgetitem5 = self.time_table.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u7b2c\u4e00\u8282", None));
        ___qtablewidgetitem6 = self.time_table.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u7b2c\u4e8c\u8282", None));
        ___qtablewidgetitem7 = self.time_table.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u7b2c\u4e09\u8282", None));
        ___qtablewidgetitem8 = self.time_table.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"\u7b2c\u56db\u8282", None));
        ___qtablewidgetitem9 = self.time_table.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"\u7b2c\u4e94\u8282", None));
        ___qtablewidgetitem10 = self.time_table.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"\u7b2c\u516d\u8282", None));
        ___qtablewidgetitem11 = self.time_table.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"\u7b2c\u4e03\u8282", None));
        ___qtablewidgetitem12 = self.time_table.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"\u7b2c\u516b\u8282", None));

        __sortingEnabled = self.time_table.isSortingEnabled()
        self.time_table.setSortingEnabled(False)
        ___qtablewidgetitem13 = self.time_table.item(0, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"\u7269\u7406", None));
        ___qtablewidgetitem14 = self.time_table.item(0, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"\u5316\u5b66", None));
        ___qtablewidgetitem15 = self.time_table.item(0, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"\u8bed\u6587", None));
        ___qtablewidgetitem16 = self.time_table.item(0, 3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"\u7269\u7406", None));
        ___qtablewidgetitem17 = self.time_table.item(0, 4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"\u5316\u5b66", None));
        ___qtablewidgetitem18 = self.time_table.item(1, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None));
        ___qtablewidgetitem19 = self.time_table.item(1, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"\u7269\u7406", None));
        ___qtablewidgetitem20 = self.time_table.item(1, 2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"\u8bed\u6587", None));
        ___qtablewidgetitem21 = self.time_table.item(1, 3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"\u8bed\u6587", None));
        ___qtablewidgetitem22 = self.time_table.item(1, 4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"\u6570\u5b66", None));
        ___qtablewidgetitem23 = self.time_table.item(2, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"\u6570\u5b66", None));
        ___qtablewidgetitem24 = self.time_table.item(2, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"\u4f53\u80b2", None));
        ___qtablewidgetitem25 = self.time_table.item(2, 2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"\u653f\u6cbb", None));
        ___qtablewidgetitem26 = self.time_table.item(2, 3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form", u"\u6570\u5b66", None));
        ___qtablewidgetitem27 = self.time_table.item(2, 4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Form", u"\u5386\u53f2", None));
        ___qtablewidgetitem28 = self.time_table.item(3, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Form", u"\u8bed\u6587", None));
        ___qtablewidgetitem29 = self.time_table.item(3, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Form", u"\u653f\u6cbb", None));
        ___qtablewidgetitem30 = self.time_table.item(3, 2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None));
        ___qtablewidgetitem31 = self.time_table.item(3, 3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Form", u"\u4f53\u80b2", None));
        ___qtablewidgetitem32 = self.time_table.item(3, 4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Form", u"\u8bed\u6587", None));
        ___qtablewidgetitem33 = self.time_table.item(4, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Form", u"\u5316\u5b66", None));
        ___qtablewidgetitem34 = self.time_table.item(4, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Form", u"\u6570\u5b66", None));
        ___qtablewidgetitem35 = self.time_table.item(4, 2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Form", u"\u6570\u5b66", None));
        ___qtablewidgetitem36 = self.time_table.item(4, 3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Form", u"\u653f\u6cbb", None));
        ___qtablewidgetitem37 = self.time_table.item(4, 4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Form", u"\u7269\u7406", None));
        ___qtablewidgetitem38 = self.time_table.item(5, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None));
        ___qtablewidgetitem39 = self.time_table.item(5, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None));
        ___qtablewidgetitem40 = self.time_table.item(5, 2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Form", u"\u5316\u5b66", None));
        ___qtablewidgetitem41 = self.time_table.item(5, 3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Form", u"\u5316\u5b66", None));
        ___qtablewidgetitem42 = self.time_table.item(5, 4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None));
        ___qtablewidgetitem43 = self.time_table.item(6, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Form", u"\u5386\u53f2", None));
        ___qtablewidgetitem44 = self.time_table.item(6, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Form", u"\u8bed\u6587", None));
        ___qtablewidgetitem45 = self.time_table.item(6, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Form", u"\u4f53\u80b2", None));
        ___qtablewidgetitem46 = self.time_table.item(6, 3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None));
        ___qtablewidgetitem47 = self.time_table.item(6, 4)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Form", u"\u73ed\u4f1a", None));
        ___qtablewidgetitem48 = self.time_table.item(7, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Form", u"\u6570\u5b66", None));
        ___qtablewidgetitem49 = self.time_table.item(7, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Form", u"\u8bed\u6587", None));
        ___qtablewidgetitem50 = self.time_table.item(7, 2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Form", u"\u7269\u7406", None));
        ___qtablewidgetitem51 = self.time_table.item(7, 3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Form", u"\u6570\u5b66", None));
        ___qtablewidgetitem52 = self.time_table.item(7, 4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Form", u"\u653e\u5b66", None));
        self.time_table.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.weekdays), QCoreApplication.translate("Form", u"\u8bfe\u7a0b\u8868", None))
        self.logger.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei','Segoe UI','sans-serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), QCoreApplication.translate("Form", u"\u65e5\u5fd7", None))
        self.label.setText(QCoreApplication.translate("Form", u"   \u90a3\u523b\u590f\uff01", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4e00\u4f4d\u95f2\u7740\u6ca1\u4e8b\u7684\u521d\u4e09\u751f\u5199\u7684\u5c0f\u7a0b\u5e8f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
    # retranslateUi

