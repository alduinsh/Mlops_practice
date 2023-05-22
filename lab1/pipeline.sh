#!/bin/bash
# 1-> Создание данных
python data_creation.py
# 2-> Предобработка данных
python data_preprocessing.py
# 3-> Подготовка и обучение модели
python model_preparation.py
# 4-> Тестирование модели
python model_testing.py