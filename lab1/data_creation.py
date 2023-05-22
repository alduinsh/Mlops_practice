# Импорт
import numpy as np
import pandas as pd
import os

# Создадим тренировочного сета
train_data = pd.DataFrame({
    'temperature': np.random.normal(loc=20, scale=5, size=2500),
    'humidity': np.random.normal(loc=50, scale=10, size=2500),
    'pressure': np.random.normal(loc=1000, scale=50, size=2500)
})
# Добавим шум
train_data['temperature'] = train_data['temperature'] + np.random.normal(loc=0, scale=2, size=2500)
train_data['humidity'] = train_data['humidity'] + np.random.normal(loc=0, scale=2, size=2500)
train_data['pressure'] = train_data['pressure'] + np.random.normal(loc=0, scale=2, size=2500)

# Определение метки
train_data['label'] = np.where(train_data['temperature'] > 25, 1, 0)

# Создание тестовой выборки
test_data = pd.DataFrame({
    'temperature': np.random.normal(loc=25, scale=5, size=1000),
    'humidity': np.random.normal(loc=50, scale=10, size=1000),
    'pressure': np.random.normal(loc=1000, scale=50, size=1000)
})
test_data['label'] = np.where(test_data['temperature'] > 25, 1, 0)

# Создание train и test
if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists('test'):
    os.makedirs('test')

# Сохранение данных в файлы
train_data.to_csv('train/train_data.csv', index=False)
test_data.to_csv('test/test_data.csv', index=False)
