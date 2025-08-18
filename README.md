# Sprint 7 - Тестирование API Курьера и Заказов

В этом проекте протестирован API учебного сервиса [Яндекс Самокат](https://qa-scooter.praktikum-services.ru/). 

Документация доступна по [ссылке](https://qa-scooter.praktikum-services.ru/api/v1/docs).

Все тесты находятся в папке tests. 
Тесты проверяют возможность:
- создания аккаунта курьера,
- авторизации курьера,
- создание заказа
- получение списка заказов.

## Генерация отчёта

### Запуск тестов с генерацией результатов
```
pytest --alluredir=./target/allure-results
```
### Генерация HTML-отчёта
```
allure generate ./target/allure-results -o ./target/allure-report --clean
```
### Просмотр отчёта (открыть готовый HTML)
```
allure open ./target/allure-report
```

---
## Установка зависимостей
### Для установки зависимостей используйте команду:
```
pip install -r requirements.txt
```

