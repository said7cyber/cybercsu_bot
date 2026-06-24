CONTACT_NUMBER = "+998 55 888 55 55"

DIRECTIONS = [
    {
        "id": "kiberxavfsizlik",
        "name": "🔐 Kiberxavfsizlik injiniringi",
        "price": 20_275_000,
        "description": (
            "Axborot tizimlarini himoya qilish, kiberhujumlarga qarshi kurashish "
            "va xavfsizlik tizimlarini loyihalash yo'nalishi."
        ),
    },
    {
        "id": "yurisprudensiya",
        "name": "⚖️ Yurisprudensiya",
        "price": 28_125_000,
        "description": (
            "Huquq fanlari, qonunchilik, sud-huquq tizimi va yuridik amaliyot "
            "bo'yicha chuqur bilim beruvchi yo'nalish."
        ),
    },
    {
        "id": "iqtisodiyot",
        "name": "📊 Iqtisodiyot",
        "price": 26_250_000,
        "description": (
            "Makro va mikroiqtisodiyot, moliyaviy tahlil, bozor munosabatlari "
            "va iqtisodiy modellashtirish yo'nalishi."
        ),
    },
    {
        "id": "menejment",
        "name": "💼 Menejment",
        "price": 26_250_000,
        "description": (
            "Biznesni boshqarish, tashkiliy rivojlantirish, strategik rejalashtirishva "
            "HR-menejment bo'yicha tayyorlov yo'nalishi."
        ),
    },
    {
        "id": "dasturiy_injiniringi",
        "name": "💻 Dasturiy injiniringi",
        "price": 20_350_000,
        "description": (
            "Dasturiy ta'minot ishlab chiqish, algoritmlar, web va mobil ilovalar "
            "yaratish bo'yicha zamonaviy yo'nalish."
        ),
    },
    {
        "id": "komputer_injiniringi",
        "name": "🖥️ Komputer injiniringi",
        "price": 20_350_000,
        "description": (
            "Komputer apparati, tarmoqlar, tizimli dasturlash va embedded tizimlar "
            "bo'yicha muhandislik yo'nalishi."
        ),
    },
]

def format_price(price: int) -> str:
    """Format price with thousands separator"""
    return f"{price:,}".replace(",", " ")
