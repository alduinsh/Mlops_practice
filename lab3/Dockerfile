# Базовый образ
FROM Python 3.9

WORKDIR /app

# Объявление порта
EXPOSE 80

#COPY main.py /main.py
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# Запуск приложения
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]



