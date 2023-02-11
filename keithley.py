import matplotlib.pyplot as plt
import pyvisa
import random as random
import time


class Keythley6221(object):
    """Класс прибора Keithley 6221 для работы с прибором."""
    def __init__(self) -> None:
        self.rm = pyvisa.ResourceManager()
        self.connection = False
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
        print(f'Настройки восстановлены по умолчанию.')

    def setLinearStaircase(self) -> None:
        """
        Выбор вида развертки:

            [STAIR] -- Указать START, STOP, STEP, DELAY
            (начало, конец, шаг, задержка)

            [LOG] -- Указать START, STOP, NO OF POINTS, DELAY
            (начало, конец, число точек, задержка)

            [CUSTOM] -- Указать #-POINTS, ADJUST POINTS, AUTO COPY*
            (число точек, ввод точек, авто-копирование)
        """

        linearStaircase = input('Установите линейно-ступенчатую развёртку: ')
        self.connection.write(f'SOUR:SWE:SPAC ' + linearStaircase)

    def setStartCurrent(self) -> None:
        """Установка начального значения тока."""
        startCurrent = input('Set start current: ')
        self.connection.write(f'SOUR:CURR:STAR ' + startCurrent)
        self.start = float(startCurrent)

    def setStopCurrent(self) -> None:
        """Установка конечного значения тока = максимальная амплитуда тока."""
        stopCurrent = input('Set stop current: ')
        self.connection.write(f'SOUR:CURR:STOP ' + stopCurrent)
        self.stop = float(stopCurrent)

    def setStep(self) -> None:
        """Установка шага увеличения амплитуды тока."""
        step = input('Set step: ')
        self.connection.write(f'SOUR:CURR:STEP ' + step)
        self.step = float(step)

    def calcDataDelay(self) -> int:
        """Подсчёт времени генерации тока перед отключением."""
        timeDelay = (self.stop - self.start) / self.step
        return round(timeDelay)

    def setDelay(self) -> None:
        """Установка ожидания между импульсами."""
        delay = input('Set delay: ')
        self.connection.write(f'SOUR:DEL ' + delay)

    def setSpan(self) -> None:
        """
        Установка диапазона источника.

        Выбор диапазона источника:
            [BEST] -- Использовать наилучший диапазон для максимального шага развертки
            [AUTO] -- Индивидуально автоматически устанавливать диапазон для каждого шага
            [FIXED] -- Оставаться в заданном диапазоне
        """
        span = input('Set range: ')
        self.connection.write(f'SOUR:PDEL:RANG ' + span)

    def setCurrentCompliance(self) -> None:
        """Ограничение выходного напряжения."""
        currentCompliance = input('Set curr comp: ')
        self.connection.write(f'SOUR:CURR:COMP ' + currentCompliance)

    def setTriaxOutputLow(self) -> None:
        """Установка вывода в землю."""
        triaxOutputLow = input('Set triax out: ')
        self.connection.write(f'OUTP:LTE ' + triaxOutputLow)

    def setLowSignal(self) -> None:
        """Установка низкого уровня сигнала."""
        lowSignal = input('Set low sig: ')
        self.connection.write(f'SOUR:PDEL:LOW ' + lowSignal)

    def setHighSignal(self) -> None:
        """Установка высокого уровня сигнала (не обязательно)."""
        highSignal = input('Set high sig: ')
        self.connection.write(f'SOUR:PDEL:HIGH ' + highSignal)

    def setImpulseInterval(self) -> None:
        """Установка интервала импульса."""
        impulseInterval = input('Set imp int: ')
        self.connection.write(f'SOUR:PDEL:INT ' + impulseInterval)

    def setWidth(self) -> None:
        """Установка ширины импульса."""
        width = input('Set width: ')
        self.connection.write(f'SOUR:PDEL:WIDT ' + width)

    def setSweepMode(self) -> None:
        """
        Инициализация функции развертки.

        [ON] -- Включить функцию развертки
        [OFF] -- Выключить функцию развертки
        """
        sweepMode = input('Set sweep mode: ')
        self.connection.write(f'SOUR:PDEL:SWE ' + sweepMode)

    def setDelayOfMode(self) -> None:
        """Установка времени задержки развертки."""
        delayOfMode = input('Set delay of mode: ')
        self.connection.write(f'SOUR:PDEL:SDEL ' + delayOfMode)

    def setPulseCount(self) -> None:
        """
        Установка счётчика = количество точек кривой.

        Задаёт размер буфера
        """
        pulseCount = input('Set pulse count: ')
        self.connection.write('SOUR:PDEL:COUN ' + pulseCount)

    def setBufSize(self) -> None:
        """Установка размера буфера."""
        bufSize = input('Set buf size: ')
        self.connection.write('TRAC:POIN ' + bufSize)

    def cleanBuffer(self) -> None:
        """Очистка буфера"""
        self.connection.write('TRAC:CLE')

    def setInterruption(self) -> None:
        """
        Прекращение работы при выходе параметров за допустимые пределы.

        [ON] -- Функция включена
        [OFF] -- Функция выключена
        """
        turnInterruption = input('Set inter: ')
        self.connection.write('TRAC:DCON:CAB ' + turnInterruption)

    def initialise(self) -> None:
        """Инициализация импульсного дельта-теста."""
        self.connection.write('SOUR:PDEL:ARM')

    def run(self) -> None:
        """Запуск импульсного дельта-теста."""
        self.connection.write('INIT:IMM')

    def complete(self) -> None:
        """Прекращение импульсного дельта-теста."""
        self.connection.write('SOUR:SWE:ABOR')

    def dataProcessing(self) -> None:
        """Считывание показаний измерений из буфера Keithley6221."""
        data = str(self.connection.query('TRAC:DATA?'))
        dataList = data.split(",")[::2]

        for number in dataList:
            self.U.append(float(number))

        self.I = [self.start + i * self.step for i in range(self.calcDataDelay())]

    def saveToFile(self) -> None:
        """Сохранение показаний с прибора в файл."""
        name = input('Введите название файла: ')
        with open(f'{name}.txt', 'w', encoding="utf-8") as f:
            f.write("{:^15}{:^35}\n".format("U", "I"))
            for u, i in zip(self.U, self.I):
                f.write("{:<25.13f}{:<25.13f}\n".format(u, i))
            f.close()

    def configureSweep(self) -> None:
        """Установка значений в режиме линейно-ступенчатой развертки."""
        self.setLinearStaircase()
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

    plt.title('Volt-ampere characteristic')
    plt.xlabel('Amperage')
    plt.ylabel('Voltage')
    plt.plot(I, U, c=color)


def showAllGraphs() -> None:
    """Показывает все графики ВАХ на одной плоскости (для наглядности)."""
    plt.show()


# TODO: магнитное поле.
