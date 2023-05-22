#!/bin/bash

# Шаг 1: Создание данных
python data_creation.py
# Шаг 2: Предобработка данных
python data_preprocessing.py
# Шаг 3: Подготовка и обучение модели
python model_preparation.py
# Шаг 4: Тестирование модели
python model_testing.py