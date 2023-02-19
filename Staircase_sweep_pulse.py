# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_Staircase_sweep_pulse(object):
    def setupUi(self, Staircase_sweep_pulse):
        if not Staircase_sweep_pulse.objectName():
            Staircase_sweep_pulse.setObjectName(u"Staircase_sweep_pulse")
        Staircase_sweep_pulse.resize(710, 600)
        Staircase_sweep_pulse.setMinimumSize(QSize(626, 286))
        Staircase_sweep_pulse.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 10pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(Staircase_sweep_pulse)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_14 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_13)

        self.lineEdit_13 = QLineEdit(self.centralwidget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)
        self.lineEdit_13.setStyleSheet(u"font-size: 14pt;\n"
"")
        self.lineEdit_13.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.lineEdit_13.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.lineEdit_13)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lineEdit_7)


        self.gridLayout.addLayout(self.verticalLayout_7, 0, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lineEdit_6)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 2, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lineEdit_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lineEdit_5)


        self.gridLayout.addLayout(self.verticalLayout_5, 1, 2, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lineEdit_8)


        self.gridLayout.addLayout(self.verticalLayout_8, 2, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_9)

        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.lineEdit_9)


        self.gridLayout.addLayout(self.verticalLayout_9, 2, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_10)

        self.lineEdit_10 = QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.lineEdit_10)


        self.gridLayout.addLayout(self.verticalLayout_10, 3, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_11)

        self.lineEdit_11 = QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lineEdit_11)


        self.gridLayout.addLayout(self.verticalLayout_11, 3, 1, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_12)

        self.lineEdit_12 = QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lineEdit_12)


        self.gridLayout.addLayout(self.verticalLayout_12, 3, 2, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_14.addWidget(self.pushButton)

        Staircase_sweep_pulse.setCentralWidget(self.centralwidget)

        self.retranslateUi(Staircase_sweep_pulse)

        QMetaObject.connectSlotsByName(Staircase_sweep_pulse)
    # setupUi

    def retranslateUi(self, Staircase_sweep_pulse):
        Staircase_sweep_pulse.setWindowTitle(QCoreApplication.translate("Staircase_sweep_pulse", u"MainWindow", None))
        self.label_13.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u0414\u0438\u0430\u043b\u043e\u0433\u043e\u0432\u043e\u0435 \u043e\u043a\u043d\u043e", None))
        self.lineEdit_13.setText("")
        self.label_2.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u043e\u043a (\u0410)", None))
        self.lineEdit_2.setText("")
        self.label_7.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u041a\u043e\u043d\u0435\u0447\u043d\u044b\u0439 \u0442\u043e\u043a (\u0410)", None))
        self.lineEdit_7.setText("")
        self.label_6.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u0428\u0430\u0433 \u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u044f \u0442\u043e\u043a\u0430 (\u0410)", None))
        self.lineEdit_6.setText("")
        self.label_4.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 (V)", None))
        self.lineEdit_4.setText("")
        self.label.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u041d\u043e\u043c\u0435\u0440 \u0432\u044b\u0431\u043e\u0440\u0430 \u043f\u0440\u0438\u0431\u043e\u0440\u0430", None))
        self.lineEdit.setText("")
        self.label_5.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u0438\u043c\u043f\u0443\u043b\u044c\u0441\u0430 (PLC)", None))
        self.lineEdit_5.setText("")
        self.label_8.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u0438\u043c\u043f\u0443\u043b\u044c\u0441\u0430 (s)", None))
        self.lineEdit_8.setText("")
        self.label_3.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438 \u0440\u0430\u0437\u0432\u0435\u0440\u0442\u043a\u0438 (s)", None))
        self.lineEdit_3.setText("")
        self.label_9.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u0412\u0440\u0435\u043c\u044f \u0446\u0438\u043a\u043b\u0430 \u0434\u0435\u043b\u044c\u0442\u0430-\u0442\u0435\u0441\u0442\u0430 (s)", None))
        self.lineEdit_9.setText("")
        self.label_10.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u0427\u0438\u0441\u043b\u043e \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u043e\u0432 \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.lineEdit_10.setText("")
        self.label_11.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u0412\u044b\u0432\u043e\u0434 \u0432 \u0437\u0435\u043c\u043b\u044e (ON/OFF)", None))
        self.lineEdit_11.setText("")
        self.label_12.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430", None))
        self.lineEdit_12.setText("")
        self.pushButton.setText(QCoreApplication.translate("Staircase_sweep_pulse", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("Staircase_sweep_pulse", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

