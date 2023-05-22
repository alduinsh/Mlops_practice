import pandas as pd
import os
import numpy as np

from sklearn.preprocessing import StandardScaler

# Загрузка данных из файлов
train_data = pd.read_csv('train/train_data.csv')
test_data = pd.read_csv('test/test_data.csv')

# Обработка пропусков
train_data.fillna(train_data.mean(), inplace=True)
test_data.fillna(test_data.mean(), inplace=True)

# Кодирование категориальных переменных
train_data = pd.get_dummies(train_data)
test_data = pd.get_dummies(test_data)

# Выбор функции
corr_matrix = train_data.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), 
                                  k=1).astype(bool)
                          )
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
train_data.drop(to_drop, axis=1, inplace=True)
test_data.drop(to_drop, axis=1, inplace=True)

# Масштабирование признаков
scaler = StandardScaler()
train_data[['temperature', 'humidity', 'pressure']] = scaler.fit_transform(
    train_data[['temperature', 'humidity', 'pressure']])
test_data[['temperature', 'humidity', 'pressure']] = scaler.transform(
    test_data[['temperature', 'humidity', 'pressure']])

# Сохранение обработанных данных в файлы
if not os.path.exists('train_preprocessed'):
    os.makedirs('train_preprocessed')
if not os.path.exists('test_preprocessed'):
    os.makedirs('test_preprocessed')

train_data.to_csv(
    'train_preprocessed/train_data_preprocessed.csv', index=False)
test_data.to_csv('test_preprocessed/test_data_preprocessed.csv', index=False)
