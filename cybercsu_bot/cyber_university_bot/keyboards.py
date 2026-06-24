from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import DIRECTIONS


def main_menu_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="📚 Yo'nalishlar", callback_data="directions")],
        [InlineKeyboardButton(text="📞 Bog'lanish", callback_data="contact")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def directions_keyboard() -> InlineKeyboardMarkup:
    buttons = []
    for direction in DIRECTIONS:
        buttons.append([
            InlineKeyboardButton(
                text=direction["name"],
                callback_data=f"dir_{direction['id']}"
            )
        ])
    buttons.append([
        InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="main_menu")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def direction_detail_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="📞 Bog'lanish", callback_data="contact")],
        [InlineKeyboardButton(text="◀️ Yo'nalishlar", callback_data="directions")],
        [InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def back_to_main_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
