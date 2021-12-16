Задача
Написать сервис на Python, который имеет 3 REST ендпоинта:
* получает по HTTP имя CSV-файла (пример файла во вложении) в хранилище и
суммирует каждый 10й столбец ☑ 
* показывает количество задач на вычисление, которые на текущий момент в работе ☑ 
* принимает ID задачи из п.1 и отображает результат в JSON-формате ☑ 

Сервис должен поддерживать обработку нескольких задач от одного клиента
одновременно.☑ 

Сервис должен иметь возможность горизонтально масштабироваться  и  загружать данные из AWS S3  и/или с локального диска.☑ 

Количество строк в csv может достигать 3*10^6.
Подключение к хранилищу может работать нестабильно.

### Building 
```bash
docker-compose build
docker-compose up
```

###Env variables (in docker-compose.yml)

```yaml
REMOTE_STORAGE=false # is app must take files from S3
LOCAL_FOLDER=/usr/src/storage #local storage folder inside container
AWS_ACCESS_KEY_ID='' # amazon public key
AWS_SECRET_ACCESS_KEY='' # amazon private key
AWS_STORAGE_BUCKET_NAME='' #bucket name
```
####Also you need to specify a local folder where the csv files are located in local storage:
```yaml
volumes:
  - <your_folder>:/usr/src/storage
```