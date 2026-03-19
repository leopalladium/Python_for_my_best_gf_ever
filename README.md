# Python для Ани 🎓

Образовательный проект с решениями и разборами задач по программированию на Python.
Включает Jupyter ноутбуки с подробными объяснениями и домашние задания с тестами.

## 🚀 Быстрый старт

### Требования
- Python 3.14+
- `uv` (менеджер пакетов и виртуальных сред) — [установка](https://docs.astral.sh/uv/getting-started/installation/)

### Установка

1. **Клонируй репозиторий:**
```bash
git clone <repo-url>
cd "Python для Ани"
```

2. **Установи зависимости и создай виртуальную среду с помощью `uv`:**
```bash
uv sync
```

Это автоматически:
- Создаст виртуальную среду `.venv/`
- Установит все зависимости из `pyproject.toml`
- Синхронизирует версии с `uv.lock`

### Запуск Jupyter Notebook

#### Способ 1: Прямой запуск через `uv`

```bash
uv run jupyter notebook
```

Этой командой Jupyter автоматически запустится в виртуальной среде и откроет браузер на `http://localhost:8888`.

#### Способ 2: Активация виртуальной среды (для повторного использования)

```bash
# Активируешь виртуальную среду
source .venv/bin/activate  # На macOS/Linux
# или
.venv\Scripts\activate  # На Windows

# Теперь запускаешь Jupyter
jupyter notebook
```

## 🔧 Настройка PyCharm для работы с Jupyter

### Подключение локального Jupyter сервера

1. **Открой PyCharm** и перейди в файл `.ipynb`

2. **Откроется диалог выбора интерпретатора** — нажми на выпадающий список и выбери:
   - **Use Configured Server** (Использовать настроенный сервер)
   - Если его нет, выбери **Configure Jupyter Server**

3. **Ручная настройка (если необходимо):**
   - Перейди в **Settings → Languages & Frameworks → Jupyter**
   - Выбери **New Environment** или **Existing Environment**
   - Укажи путь к интерпретатору из виртуальной среды:
     ```
     ./venv/bin/python  (на macOS/Linux)
     .\.venv\Scripts\python.exe  (на Windows)
     ```
   - Нажми **OK**

4. **После этого в ноутбуках появится:**
   - Возможность запускать ячейки напрямую (Shift+Enter)
   - Подсветка синтаксиса с поддержкой типов
   - Встроенный дебаггер для Python кода

### Альтернативный способ: Запуск Jupyter сервера отдельно

Если хочешь большего контроля:

```bash
# В отдельном терминале запусти сервер
uv run jupyter notebook --no-browser --port=8888

# В PyCharm перейди в Settings → Languages & Frameworks → Jupyter
# → Use Existing Server и укажи http://localhost:8888
```

## 📁 Структура проекта

```
.
├── 1. Начало.ipynb           # Разбор решений с объяснениями
├── Start.ipynb               # Стартовый ноутбук (пример)
├── ukol_1_zadani (1).py      # Задание 1 с функциями для заполнения
├── pyproject.toml            # Конфигурация проекта (зависимости)
├── uv.lock                   # Зафиксированные версии пакетов
├── README.md                 # Этот файл
└── .gitignore                # Git исключения
```

## 📚 Зависимости

Текущие зависимости (в `pyproject.toml`):
- **jupyter** (≥1.1.1) — для работы с ноутбуками
- **typing** (≥3.10.0.0) — для аннотаций типов

Чтобы добавить новый пакет:
```bash
uv add <package-name>
```

Чтобы обновить все зависимости:
```bash
uv sync --upgrade
```

## 🔍 Рекомендуемое чтение

Для понимания основных концепций:
- [Big O Notation на Proglib](https://proglib.io/p/big-o-notaciya-chto-eto-takoe-i-pochemu-ee-obyazatelno-nuzhno-znat-kazhdomu-programmistu-2022-02-17)
- [Big O Notation на Хабре](https://habr.com/ru/companies/sberbank/articles/851982/)
- [Big O Notation на Skillbox](https://skillbox.ru/media/code/big-o-notation-chto-eto-takoe-i-kak-eye-poschitat/)

## 🎯 Что находится в каждом файле

### `1. Начало.ipynb`
- **Часть I:** Анализ временной сложности алгоритмов
- **Часть II:** Исправление функций с ошибками:
  - `multiply_numbers()` — произведение чисел в диапазоне (проблема: индексация, проверка границ)
  - `has_correct_parentheses()` — проверка парных скобок
  - `sequence_sum()` — специальная сумма последовательности
  - `find_substring()` — поиск подстроки в строке
- Каждая функция включает объяснение ошибок и правильное решение

### `ukol_1_zadani (1).py`
Файл для самостоятельного решения домашнего задания с подготовленными шаблонами функций и тестами.

## 🐛 Частые проблемы

**PyCharm не видит Jupyter сервер?**
- Убедись, что виртуальная среда создана: `ls .venv` (или проверь папку)
- Перезагрузи PyCharm: **File → Invalidate Caches**
- Явно укажи путь к интерпретатору в Settings

**`uv command not found`?**
- Установи `uv`: https://docs.astral.sh/uv/getting-started/installation/
- Проверь, что он в PATH: `uv --version`

**Ноутбук зависает при запуске?**
- Попробуй перезапустить kernel: **Kernel → Restart**
- Проверь логи в терминале для ошибок

## 📝 Лицензия

Образовательный проект 📖

---

**Удачи с учёбой!** 🚀✨

