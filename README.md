# Keithley6221
  Keithley6221 staircase sweep pulse

  Данный проект создан для генерации последовательности импульсов прямоугольной формы в виде ступенчатой развертки.

![Схема](https://user-images.githubusercontent.com/86164563/220405225-a01bf79a-ba88-44f5-b0bc-8fef6b18d940.png)
  
  LO (I-Low) – низкий уровень сигнала, HI (I-High) – высокий уровень сигнала. В данном проекте LO по умолчанию 0. HI и шаг увеличения HI задаются пользователем.
  Максимальное напряжение, которое может быть во время работы прибора, задаётся пользователем.
  Номер выбора прибора – выбор из имеющихся один прибор с его адресом порта.
  Интервал импульса задаётся пользователем (это интервал времени от момента появления импульса до момента его окончания). Показан ниже.
  
  ![Impulse](https://user-images.githubusercontent.com/86164563/220405535-d8e74952-d313-4a24-bb4c-3cbb14a7a98e.png)
  
  Ширина импульса определяет, сколько времени выводимый сигнал находится на высоком и на низком уровнях. Ширина импульса может быть от 50 мкс до 12 мс. Ширина импульса задаётся пользователем.
  Задержка источника позволяет импульсу стабилизироваться перед тем, как устройству 2182А будет отправлен сигнал, разрешающий выполнение аналого-цифрового преобразования. Задержка источника может быть задана в диапазоне от 16 мкс (значение по умолчанию) до 11,966 мс. 
  Число интервалов для измерения – каждый импульсный интервал дает одно значение разности импульса напряжения. Может быть задано конечное число (от 1 до 65536) или бесконечность (Infinity).
  Интерфейс примерного заполнения данных для запуска представлен ниже.

![Interface](https://user-images.githubusercontent.com/86164563/220405671-a3cb323b-af6d-49e0-a121-70cb4f7d0390.png)
