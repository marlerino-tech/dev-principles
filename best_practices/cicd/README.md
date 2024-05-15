# 🪈 ci/cd
Полезный инструмент, который особенно подходит для нашей гибкой разработки.

*здесь когда-нибудь будут материалы, где изучать*

# Работа пайплайнов
Общий вид, я думаю пока всегда будет единный:
1. При всех push и pull-request будет запускаться CI(Continuous Integration).
2. При pull-request с `dev` запускаться сборка Build Test.
3. При push в `main` будет запускатьcя Build Production -> CD(Continuous Deployment) pipeline.

Версия проекта подтягивается из `Makefile`

## fastapi-dockercompose
### CI
- Линтинг
- Проверка типов с Mypy
- Тесты, когда-нибудь...
### Build Test / Production
- Сборка образов
- Отправка на dockerhub
### CD
- Настройка `.env.prod` и подтягивание всех важных значений из `Github Secrets`
- Подключение к серверу по `ssh`
- Создание нужных папок на сервере
- Копирование нужных конфигурационных файлов(`.env.prod, Makefile, docker-compose.yaml`)
- Запуск проекта через make команды, которые используют `docker-compose`