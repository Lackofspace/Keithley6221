import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from Staircase_sweep_pulse import Ui_Staircase_sweep_pulse

import matplotlib.pyplot as plt
import pyvisa
import random as random
import time


class StaircaseSweep(QMainWindow):
    def __init__(self):
        super(StaircaseSweep, self).__init__()

        self.ui = Ui_Staircase_sweep_pulse()
        self.ui.setupUi(self)

        self.ui.pushButton.setCheckable(True)
        self.ui.pushButton.clicked.connect(self.run)

        self.rm = pyvisa.ResourceManager()
        self.connection = False
        self.delay = None
        self.fileNumber = 0
        self.start = 0
        self.stop = 0
        self.step = 0
        self.U = []
        self.I = []

    def calcDataDelay(self) -> int:

        timeDelay = ((self.stop - self.start) / self.step) * self.delay
        return round(timeDelay)

    def run(self) -> None:

        instruments = self.rm.list_resources()
        for address in instruments:
            self.ui.lineEdit_13.setText(f'[{instruments.index(address) + 1}] -- '
                                        f'инструмент использует {address} адрес')
        choice = int(self.ui.lineEdit.text())
        self.connection = self.rm.open_resource(instruments[choice - 1])
        self.ui.lineEdit_13.setText(self.ui.lineEdit_13.text() +
                                    f'\nПодключение произошло успешно!'
                                    f'\nТекущий статус о приборе:\n'
                                    f'{self.connection.query("*IDN?")}')

        self.connection.write('*RST')

        self.connection.write(f'SOUR:PDEL:LOW 0')

        self.connection.write(f'SOUR:PDEL:WIDT ' + self.ui.lineEdit_8.text())

        self.connection.write(f'SOUR:PDEL:SDEL ' + self.ui.lineEdit_3.text())

        self.connection.write(f'SOUR:PDEL:SWE ON')

        self.connection.write('SOUR:PDEL:COUN ' + self.ui.lineEdit_10.text())

        self.connection.write(f'SOUR:SWE:SPAC LIN')

        self.connection.write(f'SOUR:CURR:STAR ' + self.ui.lineEdit_2.text())
        self.start = float(self.ui.lineEdit_2.text())

        self.connection.write(f'SOUR:CURR:STOP ' + self.ui.lineEdit_7.text())
        self.stop = float(self.ui.lineEdit_7.text())

        self.connection.write(f'SOUR:CURR:STEP ' + self.ui.lineEdit_6.text())
        self.step = float(self.ui.lineEdit_6.text())

        self.connection.write(f'SOUR:PDEL:RANG BEST')

        self.connection.write(f'SOUR:CURR:COMP ' + self.ui.lineEdit_4.text())

        self.connection.write(f'SOUR:DEL ' + self.ui.lineEdit_9.text())
        self.delay = float(self.ui.lineEdit_9.text())

        self.connection.write(f'OUTP:LTE ' + self.ui.lineEdit_11.text())

        self.connection.write('TRAC:CLE')

        self.connection.write('TRAC:POIN 5000')

        self.connection.write('SOUR:PDEL:ARM')

        self.ui.lineEdit_13.setText('Процесс запущен...')
        self.connection.write('INIT:IMM')

        time.sleep(self.calcDataDelay() + 1)
        self.ui.lineEdit_13.setText("\nПроцесс завершен!")

        self.connection.write('SOUR:SWE:ABOR')

        time.sleep(5)
        data = str(self.connection.query('TRAC:DATA?'))
        dataList = data.split(",")[::2]

        for number in dataList:
            self.U.append(float(number))

        self.I = [self.start + i * self.step for i in range(len(self.U))]

        # Для обработки больших данных нужно больше времени
        time.sleep(5)

        self.fileNumber += 1
        with open(f'{self.ui.lineEdit_12.text()}{self.fileNumber}.txt', "a", encoding="utf-8") as f:
            for u, i in zip(self.U, self.I):
                f.write("{:<25.13f}{:<25.13f}\n".format(u, i))
            f.close()

        r = random.random()
        g = random.random()
        b = random.random()

        color = (r, g, b)

        plt.title('Вольт-амперная характеристика')
        plt.xlabel('Сила тока (A)')
        plt.ylabel('Напряжение (V)')
        plt.plot(self.I, self.U, c=color)

        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = StaircaseSweep()
    window.show()

    sys.exit(app.exec())
