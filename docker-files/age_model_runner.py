from tensorflow.keras.models import load_model, Model
import pandas as pd
import numpy as np
from sys import argv


class FileNotAttached(Exception):
    ...


survived = 'survived'
pclass = 'pclass'
sex = 'sex'
age = 'age'
sibsp = 'sibsp'
parch = 'parch'
fare = 'fare'
embarked = 'embarked'
class_ = 'class'
who = 'who'
adult_male = 'adult_male'
deck = 'deck'
embark_town = 'embark_town'
alive = 'alive'
alone = 'alone'

X_COLUMNS = [pclass, sex, sibsp, parch, fare, class_, alive, alone]
Y_COLUMNS = [age]
AGE_NORMALIZER = 0.01
FARE_NORMALIZER = 0.001
SIBSP_NORMALIZER = 0.1
PARCH_NORMALIZER = 0.1
CLASSES = {'First': 0.1, 'Second': 0.5, 'Third': 0.9}
P_CLASSES = {1: 0.1, 2: 0.5, 3: 0.9}


def prepare_data(data_frame):
    """
    Функция для подготовки данных

    """
    data_frame_copy = data_frame.copy()
    data_frame_copy[pclass] = data_frame_copy[pclass] \
        .apply(lambda text_pclass: P_CLASSES[text_pclass])

    data_frame_copy[sex] = data_frame_copy[sex].apply(lambda text_sex: int(text_sex == 'female'))
    data_frame_copy[fare] *= FARE_NORMALIZER
    data_frame_copy[sibsp] *= SIBSP_NORMALIZER
    data_frame_copy[parch] *= PARCH_NORMALIZER
    data_frame_copy[class_] = data_frame_copy[class_].apply(lambda text_class: CLASSES[text_class])
    data_frame_copy[alive] = data_frame_copy[alive] \
        .apply(lambda text_alive: int(text_alive == 'yes'))

    data_frame_copy[alone] = data_frame_copy[alone].apply(int)

    data_frame_copy[age] *= AGE_NORMALIZER

    return data_frame_copy


def age_reformer(row):
    """
    Вставляет все пропуски в столбце возраст

    """
    if row.isnull()[age]:
        prepared_row = prepare_data(row.to_frame().transpose())
        age_value = age_model.predict(np.asarray(
            prepared_row[X_COLUMNS].to_numpy()).astype('float32'))[0][0]
        row[age] = round(age_value / AGE_NORMALIZER)
    return row


if len(argv) <= 1:
    raise FileNotAttached('File not found in argv')

df = pd.read_csv(argv[1])

age_model: Model = load_model('../age-model')
df = df.apply(age_reformer, 1)
df.to_csv(f'/csv/docker_out.csv')
