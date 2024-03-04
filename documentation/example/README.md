# 📜 Example Documentation Project

> Основная документация в `example.py` и файлах в папке `core`.
> **Также хорошим тоном будет прикладывать `Makefile` для упрощения запуска и настройки проекта.**

### Стек

**⭕️ Virtual Enviroment:** Pipenv

**🔙 Backend:** FastAPI

## ⚙️ Настройка окружения
1. Установка виртуального окружения и зависимостей
```shell
pipenv sync
```

2. Запуск виртуального окружения
```shell
pipenv shell
```

## 🧑🏼‍🔧 Основные команды для разработки

1. Запуск приложения(для разработки)
```shell
source .env
uvicorn core.server:app --reload --host 127.0.0.1 --port $PORT
```
or
```shell
source .env
make start PORT=$PORT
```

2. Запуск приложения(для деплоя)
```shell
source .env.prod
gunicorn core.server:app --workers $WORKERS --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```
or
```shell
source .env.prod
make start_deploy PORT=$PORT WORKERS=$WORKERS
```

## 🐋 Запуск проекта в Docker Compose

### Настройка окружения
1. Заполнить .env файл

**Dev**
```shell
cp .env.example .env.dev
```
**Prod**
```shell
cp .env.example .env.prod
```
(Не обязательно .env.prod или .env.dev. Как удобно, зависит от того, что напишете в docker-compose)

2. Настроить docker-compose файл

Так как я инфы насчёт запуска разных docker-compose файлов я почти не нашёл(про новые версии docker compose).
То запускается здесь главный `docker-compose.yml`, в остальных необходимые инструкции

**Dev**
```shell
mv docker-compose-dev.yml docker-compose.yml 
```
**Prod**
```shell
mv docker-compose-prod.yml docker-compose.yml 
```

### 🚀 Полетели!

**Prod**
```shell
docker compose up -d
```
или
```shell
make docker_start
```

## 📋 Планируемые доработки(refactoring and features)
- [ ] Возможно добавить ещё примеров
- [ ] Проверить понимается ли формат документирования