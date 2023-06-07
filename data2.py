import pandas as pd

# Загрузка 
df = pd.read_csv('datasets/data_mod1.csv')

# Заполнение пропущенных зн 
mean_age = df['Age'].mean()

# Изменение 
df['Age'].fillna(mean_age, inplace=True)

# Сохранение
df.to_csv('datasets/data_mod2.csv', index=False)