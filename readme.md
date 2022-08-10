<a href="https://colab.research.google.com/github/gaskeo/yandex-lyceum-selection-round/blob/main/main.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
<a href="https://nbviewer.org/github/gaskeo/yandex-lyceum-selection-round/blob/main/main.ipynb" target="_parent"><img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" alt="render in nbviewer"/></a>

# Отборочный тур в [Яндекс Лицей++](https://academy.yandex.ru/plusplus)

[Решение](main.ipynb) представляет собой оценку датасета 
с [титаником](https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv).
### Задачи 
1. Найти решение для пропущенных значений в столбцах
   > Для столбцов порта и города посадки и палубы 
   > было принято решение заполнить пропуски простыми флагами 
   > `U` или `Unknown`. Для столбца с возрастом 
   > была написана небольшая 
   > [нейронная сеть](#модель-для-предсказания-возраста) 
2. Ответить на вопросы:
   
    A. Кого больше среди пассажиров — мужчин или женщин?
   
    > Больше было мужчин
   
    B. Каков процент взрослых мужчин от всех пассажиров?
   
    > 59% взрослых мужчин 
   
    C. Сколько людей в каждом классе?

    > Первый класс - 216 человек
    > 
    > Второй класс - 184 человека
    >
    > Третий класс - 491 человек  
   
3. Провести анализ с помощью
   метода [`describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)
   
    > Развернутый ответ 
    [здесь](https://nbviewer.org/github/gaskeo/yandex-lyceum-selection-round/blob/main/main.ipynb#4.-%D0%92%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B-%D0%B8%D0%B7-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%BE%D0%B2)
     
4. Создать новую таблицу только с выжившими пассажирами и по ее данным ответить на вопросы:
   
    A. Как изменился процент взрослых мужчин?
   
    > Процент взрослых мужчин упал с 59% до 25%
   
    B. Какие изменения произошли в других столбцах?

    > Развернутый ответ на вопрос можно найти 
    [здесь](https://nbviewer.org/github/tikovka72/yandex-lyceum-selection-round/blob/main/main.ipynb#%D0%98%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%81%D0%BE%D0%BE%D1%82%D0%BD%D0%BE%D1%88%D0%B5%D0%BD%D0%B8%D0%B8-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%BE%D0%B2) 
   

---

### Датасеты
* [Датасет](csv/filled_titanic.csv) с заполненными пропусками
* [Датасет](csv/alive_titanic.csv) только с выжившими людьми

---
### Модель для предсказания возраста
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
4. После работы удалить контейнер и образ: 
```
docker container rm --force age-model
docker image rmi --force age-model
```


