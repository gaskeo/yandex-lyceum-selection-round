<a href="https://colab.research.google.com/github/tikovka72/yandex-lyceum-selection-round/blob/main/main.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
# yandex lyceum selection round task

[Решение](main.ipynb) для отборочного этапа в [Яндекс Лицей++](https://academy.yandex.ru/plusplus)

---

#### [Датасет](csv/filled_titanic.csv) с заполненными пропусками


#### [Датасет](csv/alive_titanic.csv) только с выжившими людьми

---
#### Модель для предсказания возраста
* [Google Drive](https://drive.google.com/drive/folders/1-6LeK9Z8WKHAy0vx96Wee4NnRItxWEqt?usp=sharing)
  (сама модель)
* [Dockerhub](https://hub.docker.com/repository/docker/tikovka72/age-model)
  (программа для заполнения пустых столбцов)

Как запустить с [docker](https://docker.com/):   
1. Скачать с [dockerhub](https://hub.docker.com/).
```
docker pull tikovka72/age-model:latest
```

2. Запустить контейнер. Необходимо поменять `your_file.csv` на имя вашего `csv` файла. 
```
docker run --name age-model -v /root/your_file.csv:/csv/your_file.csv -e csv=your_file.csv tikovka72/age-model
```
3. Скопировать файл из контейнера. Вместо `new_file.csv` можно использовать любое имя. 
```
docker cp age-model:/csv/docker_out.csv new_file.csv
```
4. Удалить контейнер и образ: 
```
docker container rm --force age-model
docker image rmi --force age-model
```

---

## Задачи

Провести анализ [датасета](https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv):

1. Найти решение для пропущенных значений в столбцах
2. Ответить на вопросы:
   <ol type="A" style="list-style-type: upper-latin">
    <li>Кого больше среди пассажиров — мужчин или женщин?</li>
    <li>Каков процент взрослых мужчин от всех пассажиров?</li>
    <li>Сколько людей в каждом классе?</li>
   </ol>
3. Провести анализ с помощью
   метода [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)
4. Создать новую таблицу только с выжившими пассажирами и по ее данным ответить на вопросы:
   <ol type="A" style="list-style-type: upper-latin">
    <li>Как изменился процент взрослых мужчин?</li>
    <li>Какие изменения произошли в других столбцах?</li>
   </ol>