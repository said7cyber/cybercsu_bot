from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from data import DIRECTIONS, CONTACT_NUMBER, TEXTS, format_price
from keyboards import (
    main_menu_keyboard,
    directions_keyboard,
    direction_detail_keyboard,
    back_to_main_keyboard,
    language_keyboard,
    murojaat_keyboard,
)

router = Router()
user_langs: dict = {}


def get_lang(user_id: int) -> str:
    return user_langs.get(user_id, "uz")


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    lang = get_lang(message.from_user.id)
    t = TEXTS[lang]
    await message.answer(
        t["welcome"],
        reply_markup=main_menu_keyboard(lang),
        parse_mode="HTML",
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    lang = get_lang(message.from_user.id)
    t = TEXTS[lang]
    await message.answer(
        t["help_text"],
        reply_markup=back_to_main_keyboard(lang),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "main_menu")
async def cb_main_menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    lang = get_lang(callback.from_user.id)
    t = TEXTS[lang]
    await callback.answer()
    try:
        await callback.message.edit_text(
            t["welcome"],
            reply_markup=main_menu_keyboard(lang),
            parse_mode="HTML",
        )
    except Exception:
        await callback.message.answer(
            t["welcome"],
            reply_markup=main_menu_keyboard(lang),
            parse_mode="HTML",
        )


@router.callback_query(F.data == "directions")
async def cb_directions(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    t = TEXTS[lang]
    await callback.answer()
    try:
        await callback.message.edit_text(
            t["directions_title"],
            reply_markup=directions_keyboard(lang),
            parse_mode="HTML",
        )
    except Exception:
        await callback.message.delete()
        await callback.message.answer(
            t["directions_title"],
            reply_markup=directions_keyboard(lang),
            parse_mode="HTML",
        )


@router.callback_query(F.data.startswith("dir_"))
async def cb_direction_detail(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    t = TEXTS[lang]
    direction_id = callback.data.replace("dir_", "")
    direction = next((d for d in DIRECTIONS[lang] if d["id"] == direction_id), None)

    if not direction:
        await callback.answer("❌ Topilmadi", show_alert=True)
        return

    exams_text = "\n".join(direction["exams"])
    text = (
        f"{direction['name']}\n\n"
        f"📝 {direction['description']}\n\n"
        f"{t['exams_title']}\n{exams_text}\n\n"
        f"{t['contract']} {format_price(direction['price'])} {t['per_year']}\n\n"
        f"{t['contact_number']} <b>{CONTACT_NUMBER}</b>"
    )

    photo_path = direction.get("photo")
    await callback.answer()
    await callback.message.delete()

    if photo_path:
        await callback.message.answer_photo(
            photo=FSInputFile(photo_path),
            caption=text,
            reply_markup=direction_detail_keyboard(lang),
            parse_mode="HTML",
        )
    else:
        await callback.message.answer(
            text,
            reply_markup=direction_detail_keyboard(lang),
            parse_mode="HTML",
        )


@router.callback_query(F.data == "contact")
async def cb_contact(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    t = TEXTS[lang]
    text = (
        f"{t['contact_title']}\n\n"
        f"{t['contact_number']} <b>{CONTACT_NUMBER}</b>\n\n"
        f"{t['contact_body']}"
    )
    await callback.answer()
    try:
        await callback.message.edit_text(
            text,
            reply_markup=back_to_main_keyboard(lang),
            parse_mode="HTML",
        )
    except Exception:
        await callback.message.answer(
            text,
            reply_markup=back_to_main_keyboard(lang),
            parse_mode="HTML",
        )


@router.callback_query(F.data == "murojaat")
async def cb_murojaat(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    t = TEXTS[lang]
    await callback.answer()
    try:
        await callback.message.edit_text(
            t["murojaat_text"],
           reply_markup=murojaat_keyboard(lang),
            parse_mode="HTML",
        )
    except Exception:
        await callback.message.answer(
            t["murojaat_text"],
            reply_markup=murojaat_keyboard(),
            parse_mode="HTML",
        )


@router.callback_query(F.data == "location")
async def cb_location(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    t = TEXTS[lang]
    await callback.answer()
    try:
        await callback.message.delete()
    except Exception:
        pass
    await callback.message.answer(
        t["location_title"],
        parse_mode="HTML",
    )
    await callback.message.answer_location(
        latitude=41.029389,
        longitude=69.346139,
        reply_markup=back_to_main_keyboard(lang)
    )


@router.callback_query(F.data == "change_language")
async def cb_change_language(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    t = TEXTS[lang]
    await callback.answer()
    try:
        await callback.message.edit_text(
            t["choose_language"],
            reply_markup=language_keyboard(),
            parse_mode="HTML",
        )
    except Exception:
        await callback.message.answer(
            t["choose_language"],
            reply_markup=language_keyboard(),
            parse_mode="HTML",
        )


@router.callback_query(F.data.startswith("set_lang_"))
async def cb_set_language(callback: CallbackQuery):
    new_lang = callback.data.replace("set_lang_", "")
    user_langs[callback.from_user.id] = new_lang
    t = TEXTS[new_lang]
    await callback.answer()
    try:
        await callback.message.edit_text(
            t["welcome"],
            reply_markup=main_menu_keyboard(new_lang),
            parse_mode="HTML",
        )
    except Exception:
        await callback.message.answer(
            t["welcome"],
            reply_markup=main_menu_keyboard(new_lang),
            parse_mode="HTML",
        )
