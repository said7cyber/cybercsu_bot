# 🎓 Cyber University Telegram Bot

Telegram бот для Cyber University — информация о направлениях, ценах и контактах.

## 📁 Структура проекта

```
cyber_university_bot/
├── bot.py              # Точка входа
├── config.py           # Загрузка настроек из .env
├── data.py             # Данные о направлениях и ценах
├── keyboards.py        # Inline-кнопки
├── handlers/
│   ├── __init__.py
│   └── main_handler.py # Все команды и callback-и
├── .env                # Твой токен (не загружать в GitHub!)
├── .env.example        # Пример .env
└── requirements.txt    # Зависимости
```

## 🚀 Запуск локально (VS Code)

### 1. Установи зависимости
```bash
pip install -r requirements.txt
```

### 2. Создай файл `.env`
Скопируй `.env.example` → `.env` и вставь свой токен:
```
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```
Токен получи у [@BotFather](https://t.me/BotFather) командой `/mybots`

### 3. Запусти бота
```bash
python bot.py
```
В терминале появится: `✅ Бот запущен!`

### 4. Проверь в Telegram
Открой своего бота и напиши `/start`

---

## ☁️ Деплой на Railway

1. Загрузи код на GitHub (без файла `.env`!)
2. Зайди на [railway.app](https://railway.app)
3. New Project → Deploy from GitHub repo
4. В разделе **Variables** добавь: `BOT_TOKEN = твой_токен`
5. Готово — бот работает 24/7!

---

## ⚠️ Важно
- Файл `.env` **никогда не загружай** на GitHub
- Добавь `.env` в `.gitignore`
