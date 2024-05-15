# 💌 env

## 🗄️️ Работа c окружениями
Больная тема, долго не мог понять как будет удобнее. Но в итоге выбрал такой подход, пока не найду другой.

В репозитории представлены примеры 3 `.env` файлов.
* `.env.dev` - файл для локальной разработки
* `.env.test` - файл для _тестового продакшена_ в `docker-compose`
* `.env.prod` - файл для продакшена(служит как подсказка для заполнения `GitHub Secretes`)

Соответственно каждый необходимо заполнить для каждого из этапов. 

Типов окружения также 3:
- `development` - локальная разработка
- `test` - зачастую повторяет `production`, но может иметь свои особенности
- `production` - окружения продакшена