import pandas as pd

# Загружаем датасет
df = pd.read_csv('datasets/data.csv')

# Выбираем столбцы, которые будем использовать
df = df[['Pclass', 'Sex', 'Age']]

# Сохраненяем  датасета
df.to_csv('datasets/data_mod1.csv', index=False)
