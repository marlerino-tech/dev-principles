# 🌹 gitflow
Понимаю, что есть отдельная методология для этого, 
но пока для наших задач данного подхода будет достаточно.

*здесь когда-нибудь будут материалы, где изучать*

Также процесс очень сильно завязан на процессе [CI/CD]()

## Работа с ветками и pull-request
1. **Никогда, ещё раз, никогда не push** в `main`. Там хранится последняя рабочая версия.
2. Всегда push в `dev-(ваше имя)` - где ты выполняешь определённый пулл своих задач.
3. Когда закрываешь определённый пулл задач, делаешь pull-request с `dev`. После чего получаешь образ _тестового продакшена_.
4. Когда полностью уверен в успехе всех проверок(тесты начни писать), то делаем pull-request с `main`.
5. После того как pull-request пройдёт CI и ревью, он будет отправлен в `main`.