import pandas as pd

# Загрузка
df = pd.read_csv('datasets/data.csv')

# Изменения
df = df[['Pclass', 'Sex', 'Age']]

# Сохранение 
df.to_csv('datasets/data_mod_1.csv', index=False)
