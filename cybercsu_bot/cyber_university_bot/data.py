import os

CONTACT_NUMBER = "+998 55 888 55 55"
ADMIN_ID = 6173375816
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEXTS = {
    "uz": {
        "welcome": (
            "🎓 <b>Cyber University</b> ga xush kelibsiz!\n\n"
            "📌 Bu bot orqali siz:\n"
            "📚 Yo'nalishlar va imtihon fanlarini bilib olishingiz\n"
            "💰 Kontrakt narxlarini ko'rishingiz\n"
            "📍 Universitetning manzilini topishingiz\n"
            "📞 Biz bilan bog'lanishingiz mumkin!\n\n"
            "Quyidagi bo'limlardan birini tanlang 👇"
        ),
        "directions_title": "📚 <b>Yo'nalishlar</b>\n\nCyber University da quyidagi ta'lim yo'nalishlari mavjud.\nBatafsil ma'lumot uchun yo'nalishni tanlang 👇",
        "contact_title": "📞 <b>Bog'lanish</b>",
        "contact_body": "Qo'ng'iroq qiling yoki xabar yuboring — mutaxassislarimiz sizga yordam berishadi! 🎓",
        "location_title": "📍 <b>Cyber University manzili:</b>\nToshkent viloyati, Nurafshon shahri,\nYangiobod ko'chasi, 42-uy",
        "contract": "💰 <b>Kontrakt narxi:</b>",
        "per_year": "so'm / yil",
        "contact_btn": "📞 Bog'lanish",
        "directions_btn": "📚 Yo'nalishlar",
        "location_btn": "📍 Manzil",
        "main_menu_btn": "🏠 Bosh menyu",
        "back_btn": "◀️ Yo'nalishlar",
        "language_btn": "🌐 Til: O'zbek 🇺🇿",
        "choose_language": "🌐 Tilni tanlang:",
        "exams_title": "📚 <b>Imtihon fanlari:</b>",
        "contact_number": "📱 Telefon:",
        "murojaat_btn": "📩 Murojaat uchun",
        "murojaat_text": (
            "📩 <b>Murojaat uchun</b>\n\n"
            "Savollaringiz bo'lsa, bizga murojaat qiling:\n\n"
            "📱 Telefon: <b>+998 55 888 55 55</b>\n"
            "💬 Telegram: <b>@ADMISSION_CU</b>\n\n"
            "🕐 Ish vaqti: Dushanba — Juma, 9:00 — 18:00"
        ),
        "help_text": (
            "ℹ️ <b>Yordam</b>\n\n"
            "📚 <b>Yo'nalishlar</b> — barcha ta'lim yo'nalishlari va narxlari\n"
            "📍 <b>Manzil</b> — universitetning joylashuvi\n"
            "📞 <b>Bog'lanish</b> — qo'shimcha savollar uchun kontakt\n\n"
            "Boshlash uchun /start buyrug'ini yuboring."
        ),
    },
    "ru": {
        "welcome": (
            "🎓 Добро пожаловать в <b>Cyber University</b>!\n\n"
            "📌 Через этого бота вы можете:\n"
            "📚 Узнать о направлениях и экзаменационных предметах\n"
            "💰 Посмотреть стоимость контракта\n"
            "📍 Найти адрес университета\n"
            "📞 Связаться с нами!\n\n"
            "Выберите один из разделов 👇"
        ),
        "directions_title": "📚 <b>Направления</b>\n\nВ Cyber University доступны следующие направления.\nВыберите направление для подробной информации 👇",
        "contact_title": "📞 <b>Контакты</b>",
        "contact_body": "Позвоните или напишите нам — наши специалисты с радостью помогут! 🎓",
        "location_title": "📍 <b>Адрес Cyber University:</b>\nТашкентская область, город Нурафшон,\nулица Янгиобод, дом 42",
        "contract": "💰 <b>Стоимость контракта:</b>",
        "per_year": "сум / год",
        "contact_btn": "📞 Контакты",
        "directions_btn": "📚 Направления",
        "location_btn": "📍 Адрес",
        "main_menu_btn": "🏠 Главное меню",
        "back_btn": "◀️ Направления",
        "language_btn": "🌐 Язык: Русский 🇷🇺",
        "choose_language": "🌐 Выберите язык:",
        "exams_title": "📚 <b>Экзаменационные предметы:</b>",
        "contact_number": "📱 Телефон:",
        "murojaat_btn": "📩 Для обращений",
        "murojaat_text": (
            "📩 <b>Для обращений</b>\n\n"
            "Если у вас есть вопросы, свяжитесь с нами:\n\n"
            "📱 Телефон: <b>+998 55 888 55 55</b>\n"
            "💬 Telegram: <b>@ADMISSION_CU</b>\n\n"
            "🕐 Время работы: Понедельник — Пятница, 9:00 — 18:00"
        ),
        "help_text": (
            "ℹ️ <b>Помощь</b>\n\n"
            "📚 <b>Направления</b> — все направления и стоимость\n"
            "📍 <b>Адрес</b> — местоположение университета\n"
            "📞 <b>Контакты</b> — для дополнительных вопросов\n\n"
            "Для начала отправьте команду /start."
        ),
    },
}

DIRECTIONS = {
    "uz": [
        {
            "id": "kiberxavfsizlik",
            "name": "🔐 Kiberxavfsizlik injiniringi",
            "price": 20_275_000,
            "description": "Axborot tizimlarini himoya qilish, kiberhujumlarga qarshi kurashish va xavfsizlik tizimlarini loyihalash yo'nalishi.",
            "exams": ["1️⃣ Matematika", "2️⃣ Fizika", "3️⃣ Majburiy fanlar: Matematika, Ona tili, O'zbekiston tarixi"],
            "photo": os.path.join(BASE_DIR, "photo_tech.jpg"),
        },
        {
            "id": "yurisprudensiya",
            "name": "⚖️ Yurisprudensiya",
            "price": 28_125_000,
            "description": "Huquq fanlari, qonunchilik, sud-huquq tizimi va yuridik amaliyot bo'yicha chuqur bilim beruvchi yo'nalish.",
            "exams": ["1️⃣ Huquqshunoslik", "2️⃣ Chet tili", "3️⃣ Majburiy fanlar: Matematika, Ona tili, O'zbekiston tarixi"],
            "photo": os.path.join(BASE_DIR, "photo_law.jpg"),
        },
        {
            "id": "iqtisodiyot",
            "name": "📊 Iqtisodiyot",
            "price": 26_250_000,
            "description": "Makro va mikroiqtisodiyot, moliyaviy tahlil, bozor munosabatlari va iqtisodiy modellashtirish yo'nalishi.",
            "exams": ["1️⃣ Matematika", "2️⃣ Chet tili", "3️⃣ Majburiy fanlar: Matematika, Ona tili, O'zbekiston tarixi"],
            "photo": os.path.join(BASE_DIR, "photo_econ.jpg"),
        },
        {
            "id": "menejment",
            "name": "💼 Menejment",
            "price": 26_250_000,
            "description": "Biznesni boshqarish, tashkiliy rivojlantirish, strategik rejalashtirish va HR-menejment bo'yicha tayyorlov yo'nalishi.",
            "exams": ["1️⃣ Matematika", "2️⃣ Chet tili", "3️⃣ Majburiy fanlar: Matematika, Ona tili, O'zbekiston tarixi"],
            "photo": os.path.join(BASE_DIR, "photo_econ.jpg"),
        },
        {
            "id": "dasturiy_injiniringi",
            "name": "💻 Dasturiy injiniringi",
            "price": 20_350_000,
            "description": "Dasturiy ta'minot ishlab chiqish, algoritmlar, web va mobil ilovalar yaratish bo'yicha zamonaviy yo'nalish.",
            "exams": ["1️⃣ Matematika", "2️⃣ Fizika", "3️⃣ Majburiy fanlar: Matematika, Ona tili, O'zbekiston tarixi"],
            "photo": os.path.join(BASE_DIR, "photo_tech.jpg"),
        },
        {
            "id": "komputer_injiniringi",
            "name": "🖥️ Komputer injiniringi",
            "price": 20_350_000,
            "description": "Komputer apparati, tarmoqlar, tizimli dasturlash va embedded tizimlar bo'yicha muhandislik yo'nalishi.",
            "exams": ["1️⃣ Matematika", "2️⃣ Fizika", "3️⃣ Majburiy fanlar: Matematika, Ona tili, O'zbekiston tarixi"],
            "photo": os.path.join(BASE_DIR, "photo_tech.jpg"),
        },
    ],
    "ru": [
        {
            "id": "kiberxavfsizlik",
            "name": "🔐 Инженерия кибербезопасности",
            "price": 20_275_000,
            "description": "Направление по защите информационных систем, противодействию кибератакам и проектированию систем безопасности.",
            "exams": ["1️⃣ Математика", "2️⃣ Физика", "3️⃣ Обязательные предметы: Математика, Родной язык, История Узбекистана"],
            "photo": os.path.join(BASE_DIR, "photo_tech.jpg"),
        },
        {
            "id": "yurisprudensiya",
            "name": "⚖️ Юриспруденция",
            "price": 28_125_000,
            "description": "Направление с углублённым изучением правовых наук, законодательства, судебной системы и юридической практики.",
            "exams": ["1️⃣ Правоведение", "2️⃣ Иностранный язык", "3️⃣ Обязательные предметы: Математика, Родной язык, История Узбекистана"],
            "photo": os.path.join(BASE_DIR, "photo_law.jpg"),
        },
        {
            "id": "iqtisodiyot",
            "name": "📊 Экономика",
            "price": 26_250_000,
            "description": "Направление по макро- и микроэкономике, финансовому анализу, рыночным отношениям и экономическому моделированию.",
            "exams": ["1️⃣ Математика", "2️⃣ Иностранный язык", "3️⃣ Обязательные предметы: Математика, Родной язык, История Узбекистана"],
            "photo": os.path.join(BASE_DIR, "photo_econ.jpg"),
        },
        {
            "id": "menejment",
            "name": "💼 Менеджмент",
            "price": 26_250_000,
            "description": "Направление по управлению бизнесом, организационному развитию, стратегическому планированию и HR-менеджменту.",
            "exams": ["1️⃣ Математика", "2️⃣ Иностранный язык", "3️⃣ Обязательные предметы: Математика, Родной язык, История Узбекистана"],
            "photo": os.path.join(BASE_DIR, "photo_econ.jpg"),
        },
        {
            "id": "dasturiy_injiniringi",
            "name": "💻 Программная инженерия",
            "price": 20_350_000,
            "description": "Современное направление по разработке программного обеспечения, алгоритмам, созданию веб- и мобильных приложений.",
            "exams": ["1️⃣ Математика", "2️⃣ Физика", "3️⃣ Обязательные предметы: Математика, Родной язык, История Узбекистана"],
            "photo": os.path.join(BASE_DIR, "photo_tech.jpg"),
        },
        {
            "id": "komputer_injiniringi",
            "name": "🖥️ Компьютерная инженерия",
            "price": 20_350_000,
            "description": "Инженерное направление по компьютерному оборудованию, сетям, системному программированию и встроенным системам.",
            "exams": ["1️⃣ Математика", "2️⃣ Физика", "3️⃣ Обязательные предметы: Математика, Родной язык, История Узбекистана"],
            "photo": os.path.join(BASE_DIR, "photo_tech.jpg"),
        },
    ],
}


def format_price(price: int) -> str:
    return f"{price:,}".replace(",", " ")
