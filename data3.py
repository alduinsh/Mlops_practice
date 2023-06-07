import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Загрузка
df = pd.read_csv('datasets/data_mod2.csv')

# Создание нового признака
onehot_encoder = OneHotEncoder(sparse_output=False)
sex_ohe = onehot_encoder.fit_transform(df[['Sex']])
sex_ohe_df = pd.DataFrame(sex_ohe, columns=onehot_encoder.categories_[0])
df = pd.concat([df, sex_ohe_df], axis=1)

# Сохранение
df.to_csv('datasets/data_mod3.csv', index=False)
