# yandex lyceum selection round task

[Решение](main.ipynb) для отборочного этапа в `Яндекс Лицей++`

---

* [Датасет с заполненными пропусками](csv/filled_titanic.csv)

* [Датасет только с выжившими людьми](csv/alive_titanic.csv)

---

## Задачи

Провести анализ [датасета](https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv):

1. Найти решение для пропущенных значений в столбцах
2. Ответить на вопросы:
   <ol style="list-style-type: upper-alpha">
    <li>Кого больше среди пассажиров — мужчин или женщин?</li>
    <li>Каков процент взрослых мужчин от всех пассажиров?</li>
    <li>Сколько людей в каждом классе?</li>
   </ol>
3. Провести анализ с помощью
   метода [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)
4. Создать новую таблицу только с выжившими пассажирами и по ее данным ответить на вопросы:
   <ol style="list-style-type: upper-alpha">
    <li>Как изменился процент взрослых мужчин?</li>
    <li>Какие изменения произошли в других столбцах?</li>
   </ol>