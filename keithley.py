import matplotlib.pyplot as plt
import pyvisa
import random as random
import time

fileCreationCounter = 0


class Keythley6221(object):
    """Класс прибора Keithley 6221 для работы с ним."""

    def __init__(self) -> None:
        self.rm = pyvisa.ResourceManager()
        self.connection = False
        self.delay = None
        self.start = 0
        self.stop = 0
        self.step = 0
        self.U = []
        self.I = []

    def connect(self) -> None:
        """Подключение к выбранному прибору по его адресу."""
        instruments = self.rm.list_resources()
        for address in instruments:
            print(f'[{instruments.index(address) + 1}] -- '
                  f'инструмент использует {address} адрес')
        choice = int(input('Выберите нужный номер прибора: '))
        self.connection = self.rm.open_resource(instruments[choice - 1])
        print(f'Подключение произошло успешно!')

    def getStatus(self) -> None:
        """Получение общей информации о приборе."""
        print(f'Информация о данном приборе: '
              f'{self.connection.query("*IDN?")}')

    def reset(self) -> None:
        """Восстановление настроек по умолчанию."""
        self.connection.write('*RST')
        print(f'Настройки восстановлены по умолчанию!')

    def setLinearStaircase(self) -> None:
        """Установка линейной развёртки."""
        self.connection.write(f'SOUR:SWE:SPAC LIN')

    def setStartCurrent(self) -> None:
        """Установка начального значения тока."""
        startCurrent = input('Установите начальный ток: ')
        self.connection.write(f'SOUR:CURR:STAR ' + startCurrent)
        self.start = float(startCurrent)

    def setStopCurrent(self) -> None:
        """Установка конечного значения тока = максимальная амплитуда тока."""
        stopCurrent = input('Установите конечный ток: ')
        self.connection.write(f'SOUR:CURR:STOP ' + stopCurrent)
        self.stop = float(stopCurrent)

    def setStep(self) -> None:
        """Установка шага увеличения амплитуды тока."""
        step = input('Установите шаг увеличения тока: ')
        self.connection.write(f'SOUR:CURR:STEP ' + step)
        self.step = float(step)

    def calcDataDelay(self) -> int:
        """Подсчёт времени генерации тока перед отключением."""
        timeDelay = ((self.stop - self.start) / self.step) * self.delay
        return round(timeDelay)

    def setDelay(self) -> None:
        """Установка ожидания между импульсами."""
        delay = input('Установите задержку импульсов: ')
        self.connection.write(f'SOUR:DEL ' + delay)
        self.delay = float(delay)

    def setSpan(self) -> None:
        """
        Установка диапазона источника.

        [BEST] -- Использовать наилучший диапазон для максимального шага развертки
        """
        self.connection.write(f'SOUR:PDEL:RANG BEST')

    def setCurrentCompliance(self) -> None:
        """Ограничение выходного напряжения."""
        currentCompliance = input('Установите предел напряжения: ')
        self.connection.write(f'SOUR:CURR:COMP ' + currentCompliance)

    def setTriaxOutputLow(self) -> None:
        """Установка вывода в землю.

            [ON] -- Включить вывод
            [OFF] -- Выключить вывод
            """
        triaxOutputLow = input('Вывод в землю: ')
        self.connection.write(f'OUTP:LTE ' + triaxOutputLow)

    def setLowSignal(self) -> None:
        """Установка низкого уровня сигнала."""
        self.connection.write(f'SOUR:PDEL:LOW 0')

    def setHighSignal(self) -> None:
        """Установка высокого уровня сигнала (не обязательно)."""
        highSignal = input('Установите высокий уровень сигнала: ')
        self.connection.write(f'SOUR:PDEL:HIGH ' + highSignal)

    def setImpulseInterval(self) -> None:
        """Установка интервала импульса."""
        impulseInterval = input('Установите интервал импульса: ')
        self.connection.write(f'SOUR:PDEL:INT ' + impulseInterval)

    def setWidth(self) -> None:
        """Установка ширины импульса."""
        width = input('Установите ширину импульса: ')
        self.connection.write(f'SOUR:PDEL:WIDT ' + width)

    def setSweepMode(self) -> None:
        """Инициализация функции развёртки."""
        self.connection.write(f'SOUR:PDEL:SWE ON')

    def setDelayOfMode(self) -> None:
        """Установка времени задержки развёртки."""
        delayOfMode = input('Установите задержку у режима: ')
        self.connection.write(f'SOUR:PDEL:SDEL ' + delayOfMode)

    def setPulseCount(self) -> None:
        """Установка счётчика. Задаёт размер буфера."""
        pulseCount = input('Установите количество импульсов: ')
        self.connection.write('SOUR:PDEL:COUN ' + pulseCount)

    def setBufSize(self) -> None:
        """Установка размера буфера."""
        self.connection.write('TRAC:POIN 5000')

    def cleanBuffer(self) -> None:
        """Очистка буфера"""
        self.connection.write('TRAC:CLE')

    def setInterruption(self) -> None:
        """
        Прекращение работы при выходе параметров за допустимые пределы.

        [ON] -- Функция включена
        [OFF] -- Функция выключена
        """
        turnInterruption = input('Прекращение: ')
        self.connection.write('TRAC:DCON:CAB ' + turnInterruption)

    def initialise(self) -> None:
        """Инициализация импульсного дельта-теста."""
        self.connection.write('SOUR:PDEL:ARM')

    def run(self) -> None:
        """Запуск импульсного дельта-теста."""
        print('Процесс запущен...')
        self.connection.write('INIT:IMM')

        # Ожидание, пока процесс завершится и чтобы не прерывать его
        time.sleep(self.calcDataDelay() + 1)
        print("Процесс завершен!")

    def complete(self) -> None:
        """Прекращение импульсного дельта-теста."""
        self.connection.write('SOUR:SWE:ABOR')

    def dataProcessing(self) -> None:
        """Считывание показаний измерений из буфера Keithley6221."""
        time.sleep(5)
        data = str(self.connection.query('TRAC:DATA?'))
        dataList = data.split(",")[::2]

        for number in dataList:
            self.U.append(float(number))

        self.I = [self.start + i * self.step for i in range(len(self.U))]

        # Для обработки больших данных нужно больше времени
        time.sleep(5)

    def configureSweep(self) -> None:
        """Установка значений в режиме линейно-ступенчатой развертки."""
        self.setLinearStaircase()
        self.setStartCurrent()
        self.setStopCurrent()
        self.setStep()
        self.setSpan()
        self.setCurrentCompliance()
        self.setDelay()
        self.setTriaxOutputLow()

    def pulseSweep(self) -> None:
        """Установка значений в режиме импульсного дельта-теста."""
        self.setLowSignal()
        self.setWidth()
        self.setDelayOfMode()
        self.setSweepMode()
        self.setPulseCount()


def saveToFile(U, I, fileNumber) -> None:
    """Сохранение показаний с прибора в файл."""
    name = input('Введите название файла: ')
    fileNumber += 1
    with open(f'{name}{fileNumber}.txt', "a", encoding="utf-8") as f:
        # Левая колонка -- напряжение, правая -- ток.
        # f.write("{:^15}{:^35}\n".format("U", "I"))
        for u, i in zip(U, I):
            f.write("{:<25.13f}{:<25.13f}\n".format(u, i))
        f.close()


def draw(U, I) -> None:
    """
    Построение графика по измеренным данным.

    С графиком можно будет делать следующее (при просмотре):
        Перемещаться с помощью курсора по графику
        Приближать изображение
        Менять настройки просмотра (например, смещать в сторону)
        Сохранять
        Сбрасывать описанные выше настройки
    """
    # Задание случайного цвета графика
    r = random.random()
    g = random.random()
    b = random.random()

    color = (r, g, b)

    plt.title('Вольт-амперная характеристика')
    plt.xlabel('Сила тока')
    plt.ylabel('Напряжение')
    plt.plot(I, U, c=color)


def showAllGraphs() -> None:
    """Показывает все графики ВАХ на одной плоскости (для наглядности)."""
    plt.show()
