import pandas as pd
from catboost.datasets import titanic


# Получение данных о пассажирах
train_df, _ = titanic()

# Сохранение данных в файл
train_df.to_csv('datasets/data.csv', index=False)
