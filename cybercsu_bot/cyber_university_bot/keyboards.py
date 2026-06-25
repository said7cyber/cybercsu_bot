from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import TEXTS


def main_menu_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    t = TEXTS[lang]
    buttons = [
        [InlineKeyboardButton(text=t["directions_btn"], callback_data="directions")],
        [InlineKeyboardButton(text=t["murojaat_btn"], callback_data="murojaat")],
        [InlineKeyboardButton(text=t["location_btn"], callback_data="location")],
        [InlineKeyboardButton(text=t["contact_btn"], callback_data="contact")],
        [InlineKeyboardButton(text=t["language_btn"], callback_data="change_language")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def directions_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    from data import DIRECTIONS
    t = TEXTS[lang]
    buttons = []
    for direction in DIRECTIONS[lang]:
        buttons.append([
            InlineKeyboardButton(
                text=direction["name"],
                callback_data=f"dir_{direction['id']}"
            )
        ])
    buttons.append([
        InlineKeyboardButton(text=t["main_menu_btn"], callback_data="main_menu")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def direction_detail_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    t = TEXTS[lang]
    buttons = [
        [InlineKeyboardButton(text=t["murojaat_btn"], callback_data="murojaat")],
        [InlineKeyboardButton(text=t["contact_btn"], callback_data="contact")],
        [InlineKeyboardButton(text=t["back_btn"], callback_data="directions")],
        [InlineKeyboardButton(text=t["main_menu_btn"], callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def back_to_main_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    t = TEXTS[lang]
    buttons = [
        [InlineKeyboardButton(text=t["main_menu_btn"], callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def language_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="set_lang_uz")],
        [InlineKeyboardButton(text="🇷🇺 Русский язык", callback_data="set_lang_ru")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def murojaat_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    t = TEXTS[lang]
    buttons = [
        [InlineKeyboardButton(text="💬 @ADMISSION_CU", url="https://t.me/ADMISSION_CU")],
        [InlineKeyboardButton(text=t["main_menu_btn"], callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
