from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from data import DIRECTIONS, CONTACT_NUMBER, format_price
from keyboards import (
    main_menu_keyboard,
    directions_keyboard,
    direction_detail_keyboard,
    back_to_main_keyboard,
)

router = Router()

WELCOME_TEXT = (
    "🎓 <b>Cyber University</b> ga xush kelibsiz!\n\n"
    "Biz zamonaviy ta'lim muassasasi sifatida sizga "
    "sifatli bilim va kelajak uchun kuchli poydevor taqdim etamiz.\n\n"
    "Quyidagi bo'limlardan birini tanlang 👇"
)


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        WELCOME_TEXT,
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML",
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    text = (
        "ℹ️ <b>Yordam</b>\n\n"
        "📚 <b>Yo'nalishlar</b> — barcha ta'lim yo'nalishlari va narxlari\n"
        "📞 <b>Bog'lanish</b> — qo'shimcha savollar uchun kontakt\n\n"
        "Boshlash uchun /start buyrug'ini yuboring."
    )
    await message.answer(text, reply_markup=back_to_main_keyboard(), parse_mode="HTML")


# ─── Callbacks ────────────────────────────────────────────────────────────────

@router.callback_query(F.data == "main_menu")
async def cb_main_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        WELCOME_TEXT,
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML",
    )
    await callback.answer()


@router.callback_query(F.data == "directions")
async def cb_directions(callback: CallbackQuery):
    text = (
        "📚 <b>Yo'nalishlar</b>\n\n"
        "Cyber University da quyidagi ta'lim yo'nalishlari mavjud.\n"
        "Batafsil ma'lumot uchun yo'nalishni tanlang 👇"
    )
    await callback.message.edit_text(
        text,
        reply_markup=directions_keyboard(),
        parse_mode="HTML",
    )
    await callback.answer()


@router.callback_query(F.data.startswith("dir_"))
async def cb_direction_detail(callback: CallbackQuery):
    direction_id = callback.data.replace("dir_", "")
    direction = next((d for d in DIRECTIONS if d["id"] == direction_id), None)

    if not direction:
        await callback.answer("❌ Yo'nalish topilmadi", show_alert=True)
        return

    text = (
        f"{direction['name']}\n\n"
        f"📝 {direction['description']}\n\n"
        f"💰 <b>Kontrakt narxi:</b> {format_price(direction['price'])} so'm / yil\n\n"
        f"📞 Qo'shimcha ma'lumot uchun: <b>{CONTACT_NUMBER}</b>"
    )
    await callback.message.edit_text(
        text,
        reply_markup=direction_detail_keyboard(),
        parse_mode="HTML",
    )
    await callback.answer()


@router.callback_query(F.data == "contact")
async def cb_contact(callback: CallbackQuery):
    text = (
        "📞 <b>Bog'lanish</b>\n\n"
        f"📱 Telefon: <b>{CONTACT_NUMBER}</b>\n\n"
        "Qo'ng'iroq qiling yoki xabar yuboring — "
        "mutaxassislarimiz sizga yordam berishadi! 🎓"
    )
    await callback.message.edit_text(
        text,
        reply_markup=back_to_main_keyboard(),
        parse_mode="HTML",
    )
    await callback.answer()
