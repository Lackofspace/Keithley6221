import pyvisa


class Keythley6221(object):
    # TODO: сделать документацию класса.
    def __init__(self,
                 startCurrent,
                 stopCurrent,
                 step,
                 delay,
                 span,
                 count,
                 compliance,
                 lowSignal,
                 highSignal,
                 impulseInterval,
                 width,
                 sweepMode,
                 delayOfMode,
                 bufSize,
                 fileName) -> None:
        self.rm = pyvisa.ResourceManager()
        self.connection = False
        self.startCurrent = startCurrent
        self.stopCurrent = stopCurrent
        self.step = step
        self.delay = delay
        self.span = span
        self.count = count
        self.compliance = compliance
        self.lowSignal = lowSignal
        self.highSignal = highSignal
        self.impulseInterval = impulseInterval
        self.width = width
        self.sweepMode = sweepMode
        self.delayOfMode = delayOfMode
        self.bufSize = bufSize
        self.fileName = fileName

    @staticmethod
    def checkRules():
        """Описывание инструкций по работе с данной программой."""

        # TODO: сделать вывод описаний атрибутов класса,
        #  рекомендации по их выбору и вывести список доступных значений.

        pass

    def connect(self) -> None:
        """Подключение к выбранному прибору по его адресу."""
        instruments = self.rm.list_resources()
        for address in instruments:
            print(f'{instruments.index(address) + 1} '
                  f'инструмент использует {address} адрес')
        choice = int(input('Выберите нужный номер прибора: '))
        self.connection = self.rm.open_resource(instruments[choice])

    def getStatus(self) -> None:
        """Получение общей информации о приборе."""
        print(f'Информация о данном приборе: '
              f'{self.connection.query("*IDN?")}')

    def reset(self) -> None:
        """Восстановление настроек по умолчанию."""
        self.connection.write('*RST')

    def setLinearStaircase(self) -> None:
        """Выбор линейно-ступенчатой развертки."""
        self.connection.write('SOUR:SWE:SPAC LIN')

    def setStartCurrent(self) -> None:
        """Установка начального значения тока."""
        self.connection.write(f'SOUR:CURR:STAR {self.startCurrent}')

    def setStopCurrent(self) -> None:
        """Установка конечного значения тока = максимальная амплитуда тока."""
        self.connection.write(f'SOUR:CURR:STOP {self.stopCurrent}')

    def setStep(self) -> None:
        """Установка шага увеличения амплитуды тока."""
        self.connection.write(f'SOUR:CURR:STEP {self.step}')

    def setDelay(self) -> None:
        """Установка ожидания между импульсами."""
        self.connection.write(f'SOUR:DEL {self.delay}')

    def setSpan(self) -> None:
        """Установка диапазона источника."""
        self.connection.write(f'SOUR:SWE:RANG {self.span}')

    def setCount(self) -> None:
        """Установка числа повторений развертки."""
        self.connection.write(f'SOUR:SWE:COUN {self.count}')

    def setCompliance(self) -> None:
        """Установка развертки."""
        self.connection.write(f'SOUR:SWE:CAB {self.compliance}')

    def setLowSignal(self) -> None:
        """Установка низкого уровня сигнала."""
        self.connection.write(f'SOUR:PDEL:LOW {self.lowSignal}')

    def setHighSignal(self) -> None:
        """Установка высокого уровня сигнала (не обязательно)."""
        self.connection.write(f'SOUR:PDEL:HIGH {self.highSignal}')

    def setImpulseInterval(self) -> None:
        """Установка интервала импульса."""
        self.connection.write(f'SOUR:PDEL:INT {self.impulseInterval}')

    def setWidth(self) -> None:
        """Установка ширины импульса."""
        self.connection.write(f'SOUR:PDEL:WIDT {self.width}')

    def setSweepMode(self) -> None:
        """Инициализация функции развертки."""
        self.connection.write(f'SOUR:PDEL:SWE {self.sweepMode}')

    def setDelayOfMode(self) -> None:
        """Установка времени задержки развертки."""
        self.connection.write(f'SOUR:PDEL:SDEL {self.delayOfMode}')

    def setBufSize(self) -> None:
        """Установка размера буфера."""
        self.connection.write(f'TRAC:POIN {self.bufSize}')

    def initialise(self) -> None:
        """Инициализация импульсного дельта-теста."""
        self.connection.write('SOUR:PDEL:ARM')

    def run(self) -> None:
        """Запуск импульсного дельта-теста."""
        self.connection.write('INIT:IMM')

    def complete(self) -> None:
        """Прекращение импульсного дельта-теста."""
        self.connection.write('SOUR:SWE:ABOR')

    def dataProcessing(self):
        """Считывание показания измерений из буфера Keithley6221 и обработка данных."""
        data = self.connection.query('TRAC:DATA?')

        # TODO: сделать обработку данных для их последующего
        #  сохранения в файл и для построения графика.

        pass

    def saveToFile(self):
        """Сохранение показаний с прибора в файл."""

        # TODO: сделать сохранение данных в файл.

        pass

    def draw(self):
        """Построение графика по измеренным данным."""

        # TODO: сделать работу с графиком.

        pass

    def configureSweep(self) -> None:
        """Установка значений в режиме линейно-ступенчатой развертки."""
        self.setLinearStaircase()
        self.setStartCurrent()
        self.setStopCurrent()
        self.setStep()
        self.setDelay()
        self.setSpan()
        self.setCount()
        self.setCompliance()

    def pulseSweep(self) -> None:
        """Установка значений в режиме импульсного дельта-теста."""
        self.setLowSignal()
        self.setHighSignal()
        self.setImpulseInterval()
        self.setWidth()
        self.setSweepMode()
        self.setDelayOfMode()
        self.setBufSize()
        self.initialise()

# TODO: магнитное поле.
