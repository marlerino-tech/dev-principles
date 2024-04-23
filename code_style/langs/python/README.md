# 🐍 Стиль для документации Python

Мы будем использовать для Python [Google Style Guide](https://google.github.io/styleguide/pyguide.html).

Достаточно современный и удобный стиль, без трудностей reStructedText.

**Обязательно к прочтению:** https://google.github.io/styleguide/pyguide.html
или pdf приложенная

**Для особого искушения)**
- https://peps.python.org/pep-0008/
- https://www.python.org/dev/peps/pep-0257/
- https://peps.python.org/pep-0484/

## ⚙️ Для настройки в PyCharm:

`Settings -> Tools -> Python Integrated Tools -> Docstring Format -> Google`
1. Заходим в `Settings`
2. Дальше секция `Tools`
3. Дальше секция `Python Integrated Tools`
4. В поле `Docstring Format` выбираем **Google**

## 🦀 Настройка Ruff(linter and formatter)
### Команды
- `ruff check <filename>` - lint
- `ruff format <filename>` - format