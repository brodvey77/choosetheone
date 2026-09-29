import requests
from urllib.parse import urlencode
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ============================================================
# НАСТРОЙКИ
# ============================================================

API_URL = "https://nsi.eaeunion.org/api/v1/dictionaries/1995/elements"

CARD_URL = "https://nsi.eaeunion.org/portal/1995/card"

TIMEOUT = 30

# Максимальное количество записей, которое разрешено получить
LIMIT = 1500

# Токен вашего Telegram бота (получите у @BotFather)
TELEGRAM_BOT_TOKEN = "8993485243:AAHCe-dfDLpyJwWJ3lf6BcrbNNGH9rTD0yM"

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# ============================================================
# НОРМАЛИЗАЦИЯ НОМЕРА
# ============================================================

def normalize_number(number):
    """
    Нормализация номера СГР.

    Удаляет пробелы по краям и приводит латинские символы
    к верхнему регистру.

    ВАЖНО:
    Кириллическая Е и латинская E намеренно НЕ заменяются
    друг на друга.
    """
    return number.strip().upper()


# ============================================================
# ВАРИАНТЫ НОМЕРА СГР
# ============================================================

def get_number_variants(number):
    """
    Создаёт варианты номера для поиска.

    В реестре встречается как латинская E,
    так и кириллическая Е.
    """
    number = normalize_number(number)
    variants = [number]

    # Латинская E
    if "E" in number:
        cyrillic_variant = number.replace("E", "Е")
        if cyrillic_variant not in variants:
            variants.append(cyrillic_variant)

    # Кириллическая Е
    if "Е" in number:
        latin_variant = number.replace("Е", "E")
        if latin_variant not in variants:
            variants.append(latin_variant)

    return variants


# ============================================================
# ЗАПРОС К API
# ============================================================

def search_api(number):
    """
    Выполняет запрос к API НСИ ЕАЭС
    по номеру свидетельства.
    """
    params = {
        "conditions[0].conditionType": "like",
        "conditions[0].code": "NUMB_DOC",
        "conditions[0].value": number,
        "limit": LIMIT,
        "offset": 0
    }

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=TIMEOUT
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        logger.error("Превышено время ожидания ответа API.")
        return None

    except requests.exceptions.ConnectionError:
        logger.error("Невозможно подключиться к серверу НСИ ЕАЭС.")
        return None

    except requests.exceptions.HTTPError as error:
        logger.error(f"HTTP ошибка: {error}")
        return None

    except requests.exceptions.JSONDecodeError:
        logger.error("Сервер вернул некорректный JSON.")
        return None

    except requests.exceptions.RequestException as error:
        logger.error(f"Ошибка запроса: {error}")
        return None


# ============================================================
# ПОЛУЧЕНИЕ ЗАПИСЕЙ
# ============================================================

def get_records(data):
    if not data:
        return []
    return data.get("elements", [])


# ============================================================
# ПОЛУЧЕНИЕ ЗНАЧЕНИЯ
# ============================================================

def get_value(data, key, default="—"):
    value = data.get(key)

    if value is None:
        return default

    if isinstance(value, str):
        value = value.strip()
        if not value:
            return default

    return value


# ============================================================
# ФОРМИРОВАНИЕ ССЫЛКИ
# ============================================================

def make_card_url(record):
    record_id = record.get("id")
    if not record_id:
        return None
    return f"{CARD_URL}/{record_id}"


# ============================================================
# СТАТУС
# ============================================================

def get_status(data):
    status = data.get("STATUS")

    if isinstance(status, dict):
        return status.get("name", "—")

    if isinstance(status, str):
        return status

    return "—"


# ============================================================
# СТРАНА
# ============================================================

def get_country(data, field):
    country = data.get(field)

    if isinstance(country, dict):
        return country.get("name", "—")

    if country:
        return str(country)

    return "—"


# ============================================================
# ПОИСК
# ============================================================

def find_sgr(number):
    variants = get_number_variants(number)
    all_records = {}

    for variant in variants:
        logger.info(f"Поиск номера: {variant}")
        data = search_api(variant)

        if data is None:
            continue

        records = get_records(data)
        logger.info(f"Получено записей: {len(records)}")

        for record in records:
            record_id = record.get("id")
            if record_id:
                all_records[record_id] = record

    return list(all_records.values())


# ============================================================
# ФОРМАТИРОВАНИЕ ОТВЕТА
# ============================================================

def format_record_message(record):
    """
    Форматирует информацию о записи для отправки в Telegram.
    """
    data = record.get("data", {})

    message = (
        "📄 *СВИДЕТЕЛЬСТВО О ГОСУДАРСТВЕННОЙ РЕГИСТРАЦИИ*\n\n"
        f"🔢 *Номер СГР:* `{get_value(data, 'NUMB_DOC')}`\n"
        f"✅ *Статус:* {get_status(data)}\n"
        f"📅 *Дата оформления:* {get_value(data, 'DATE_DOC')}\n"
        f"🏷 *Типографский №:* {get_value(data, 'SERIALNUMB')}\n\n"
        f"📦 *Продукция:* {get_value(data, 'NAME_PROD')}\n"
        f"📝 *Наименование:* {get_value(data, 'PROD_APP')}\n\n"
        f"🏭 *Изготовитель:* {get_value(data, 'FIRMMADE_NAME')}\n"
        f"📍 *Адрес изготовителя:* {get_value(data, 'FIRMMADE_ADDR')}\n\n"
        f"📬 *Получатель:* {get_value(data, 'FIRMGET_NAME')}\n"
        f"📍 *Адрес получателя:* {get_value(data, 'FIRMGET_ADDR')}\n\n"
        f"🌍 *Страна изготовителя:* {get_country(data, 'N_ALFA_NAME')}\n"
        f"📋 *Нормативный документ:* {get_value(data, 'DOC_NORM')}\n"
        f"🎯 *Область применения:* {get_value(data, 'DOC_USEAREA')}\n"
        f"🕐 *Дата последнего изменения:* {get_value(data, 'DATE_LASTEDIT')}\n"
    )

    return message


# ============================================================
# ОБРАБОТЧИКИ КОМАНД
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обработчик команды /start.
    """
    welcome_message = (
        "👋 Добро пожаловать в бот поиска свидетельств о государственной регистрации (СГР) ЕАЭС!\n\n"
        "🔍 *Как использовать:*\n"
        "• Просто отправьте мне номер СГР для поиска\n"
        "• Я найду информацию и предоставлю ссылку на карточку\n\n"
        "📝 *Примеры номеров:*\n"
        "• RU.77.99.88.001.Е.000001.01.20\n"
        "• BY.10.20.30.002.Е.000002.02.21\n\n"
        "💡 *Особенности:*\n"
        "• Автоматический поиск с учётом кириллических и латинских символов\n"
        "• Поддержка нескольких вариантов написания номера\n\n"
        "Отправьте номер СГР для начала поиска! 🚀"
    )

    await update.message.reply_text(
        welcome_message,
        parse_mode='Markdown'
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обработчик команды /help.
    """
    help_message = (
        "ℹ️ *Помощь по использованию бота*\n\n"
        "🔍 *Поиск СГР:*\n"
        "• Отправьте номер свидетельства в любом формате\n"
        "• Бот автоматически обработает различные варианты написания\n\n"
        "📋 *Что вы получите:*\n"
        "• Полную информацию о свидетельстве\n"
        "• Прямую ссылку на карточку в реестре НСИ ЕАЭС\n\n"
        "⚠️ *Важно:*\n"
        "• Поиск может занять несколько секунд\n"
        "• Если ничего не найдено - проверьте правильность номера\n\n"
        "Команды:\n"
        "/start - Запустить бота\n"
        "/help - Показать эту справку"
    )

    await update.message.reply_text(
        help_message,
        parse_mode='Markdown'
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обработчик текстовых сообщений (поиск СГР).
    """
    user_input = update.message.text.strip()

    if not user_input:
        await update.message.reply_text("❌ Пожалуйста, введите номер СГР для поиска.")
        return

    # Отправляем сообщение о начале поиска
    searching_message = await update.message.reply_text(
        "🔍 Ищу свидетельство... Пожалуйста, подождите."
    )

    try:
        # Выполняем поиск
        records = find_sgr(user_input)

        # Обновляем сообщение о поиске
        await searching_message.delete()

        if not records:
            not_found_message = (
                "❌ *СВИДЕТЕЛЬСТВО НЕ НАЙДЕНО*\n\n"
                "Проверьте правильность номера СГР.\n\n"
                "💡 *Советы:*\n"
                "• Убедитесь, что номер введён полностью\n"
                "• Проверьте правильность написания символов\n"
                "• Попробуйте ввести номер в другом формате"
            )
            await update.message.reply_text(
                not_found_message,
                parse_mode='Markdown'
            )
            return

        # Если найдено несколько записей
        if len(records) > 1:
            multiple_found = (
                f"✅ *Найдено записей: {len(records)}*\n\n"
                "Ниже представлена информация по каждому свидетельству:"
            )
            await update.message.reply_text(
                multiple_found,
                parse_mode='Markdown'
            )

        # Отправляем информацию по каждой записи
        for i, record in enumerate(records, 1):
            message = format_record_message(record)

            # Добавляем кнопку со ссылкой на карточку
            card_url = make_card_url(record)

            if card_url:
                keyboard = [[InlineKeyboardButton("🔗 Открыть карточку в реестре", url=card_url)]]
                reply_markup = InlineKeyboardMarkup(keyboard)

                await update.message.reply_text(
                    message,
                    parse_mode='Markdown',
                    reply_markup=reply_markup,
                    disable_web_page_preview=True
                )
            else:
                await update.message.reply_text(
                    message,
                    parse_mode='Markdown'
                )

    except Exception as e:
        logger.error(f"Ошибка при обработке сообщения: {e}")
        await update.message.reply_text(
            "❌ Произошла ошибка при поиске. Пожалуйста, попробуйте позже.",
            parse_mode='Markdown'
        )


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обработчик ошибок.
    """
    logger.error(f"Update {update} caused error {context.error}")

    if update and update.message:
        await update.message.reply_text(
            "❌ Произошла непредвиденная ошибка. Пожалуйста, попробуйте позже."
        )


# ============================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ============================================================

def main():
    """
    Запуск бота.
    """
    print("=" * 80)
    print("       TELEGRAM БОТ ПОИСКА СГР ЕАЭС")
    print("=" * 80)
    print()
    print("Бот запущен и ожидает сообщения...")
    print()
    print("Для остановки нажмите Ctrl+C")
    print()

    # Создаём приложение
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Добавляем обработчик ошибок
    application.add_error_handler(error_handler)

    # Запускаем бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)


# ============================================================
# ЗАПУСК
# ============================================================

if __name__ == "__main__":
    main()
