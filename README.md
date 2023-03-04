# Keithley6221
Keithley6221 staircase sweep pulse

Данный проект создан для генерации последовательности импульсов прямоугольной формы в виде ступенчатой развертки.

![Схема](https://user-images.githubusercontent.com/86164563/220405225-a01bf79a-ba88-44f5-b0bc-8fef6b18d940.png)

LO (I-Low) – низкий уровень сигнала, HI (I-High) – высокий уровень сигнала. В данном проекте LO по умолчанию 0. HI и шаг увеличения HI задаются пользователем.

Максимальное напряжение, которое может быть во время работы прибора, задаётся пользователем.

Номер выбора прибора – выбор из имеющихся один прибор с его адресом порта.

Интервал импульса задаётся пользователем (это интервал времени от момента появления импульса до момента его окончания, выражается числом циклов мощности линии
питания (PLC). Для 60 Гц 1PLC составляет 16,667 мс, а для 50 Гц 1PLC равен 20 мс. Интервал может
быть задан от 5 PLC (значение по умолчанию) до 999999 PLC). Показан ниже.
  
  ![Impulse](https://user-images.githubusercontent.com/86164563/220405535-d8e74952-d313-4a24-bb4c-3cbb14a7a98e.png)
  
Ширина импульса определяет, сколько времени выводимый сигнал находится на высоком и на низком уровнях. Ширина импульса может быть от 50 мкс до 12 мс. Ширина импульса задаётся пользователем.
  
Задержка источника позволяет импульсу стабилизироваться перед тем, как устройству 2182А будет отправлен сигнал, разрешающий выполнение аналого-цифрового преобразования. 
Задержка источника может быть задана в диапазоне от 16 мкс (значение по умолчанию) до 11,966 мс. 

Число интервалов для измерения – каждый импульсный интервал дает одно значение разности импульса напряжения. Может быть задано конечное число (от 1 до 65536) или бесконечность (Infinity).
  
Интерфейс примерного заполнения данных для запуска представлен ниже.

![Interface](https://user-images.githubusercontent.com/86164563/222907653-e3c4919e-05f7-4d71-9f65-f5bf4eb50ed2.png)

Примеры результатов работы программы:

![textFiles](https://user-images.githubusercontent.com/86164563/220614310-923ca178-2a81-4db1-a374-09e51fb83472.png)

И их графики:

![Figure_1](https://user-images.githubusercontent.com/86164563/220614725-951298c6-39b6-4a54-8ed6-8899d2b8fdff.png)

Построить графики на основе созданных текстовых файлов можно с помощью следующей программы:
```
import matplotlib

# Из-за конфликта библиотек matplotlib и PySide6 здесь явно указывается использование первой.
matplotlib.use('tkagg')
from matplotlib import pyplot as plt
import pandas as pd
import random as random


def read(filename):
    df = pd.read_table(filename, header=None, sep=r"\s+")
    I = df[1].tolist()
    U = df[0].tolist()
    return U, I


def plot_func(U, I):
    r = random.random()
    g = random.random()
    b = random.random()
    color = (r, g, b)
    plt.plot(I, U, c=color)


U_f, I_f = read('f.txt')
U_r, I_r = read('r.txt')

plt.title('Вольт-амперная характеристика')
plt.xlabel('Сила тока (A)')
plt.ylabel('Напряжение (U)')
plot_func(U_f, I_f)
plot_func(U_r, I_r)

plt.show()
```
