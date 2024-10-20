# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTextEdit, QTreeView, QVBoxLayout,
    QWidget)

class Ui_UI(object):
    def setupUi(self, UI):
        if not UI.objectName():
            UI.setObjectName(u"UI")
        UI.resize(1020, 570)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UI.sizePolicy().hasHeightForWidth())
        UI.setSizePolicy(sizePolicy)
        UI.setMinimumSize(QSize(1020, 570))
        UI.setMaximumSize(QSize(1020, 570))
        self.horizontalLayoutWidget = QWidget(UI)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 1001, 551))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.open = QPushButton(self.horizontalLayoutWidget)
        self.open.setObjectName(u"open")

        self.horizontalLayout_2.addWidget(self.open)

        self.save = QPushButton(self.horizontalLayoutWidget)
        self.save.setObjectName(u"save")

        self.horizontalLayout_2.addWidget(self.save)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.treeView = QTreeView(self.horizontalLayoutWidget)
        self.treeView.setObjectName(u"treeView")

        self.horizontalLayout.addWidget(self.treeView)


        self.retranslateUi(UI)

        QMetaObject.connectSlotsByName(UI)
    # setupUi

    def retranslateUi(self, UI):
        UI.setWindowTitle(QCoreApplication.translate("UI", u"FowlEditor", None))
        self.open.setText(QCoreApplication.translate("UI", u"Open Folder", None))
        self.save.setText(QCoreApplication.translate("UI", u"Save main.py", None))
    # retranslateUi

