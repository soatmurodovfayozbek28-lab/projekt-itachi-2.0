# MODULES — Modullar vazifalari

> Holat: hamma modul **reja** bosqichida. Hali birortasi yozilmagan.

## Umumiy jadval

| # | Modul | Bosqich | Holat |
|---|---|---|---|
| 1 | Itachi Core | 2 | reja |
| 2 | Memory System | 3 | reja |
| 3 | AI Gateway | 4 | reja |
| 4 | Research Engine | 5 | reja |
| 5 | Mentor Engine | 6 | reja |
| 6 | Analyst Engine | 6 | reja |
| 7 | Business Intelligence | 6 | reja |
| 8 | Strategist Engine | 6 | reja |
| 9 | Scheduler | 7 | reja |
| 10 | Android Interface | 8 | reja |

Ishlash tartibi: avval Core, Memory va AI Gateway (poydevor), keyin Research, keyin boshqa engine'lar, oxirida Scheduler va Android.

## 1. Itachi Core — asosiy miya

- Vazifasi: buyruqni qabul qilish, kerakli engine'ga berish, modullar ishini muvofiqlashtirish, tizim holatini kuzatish, ruxsat darvozasini ishga tushirish.
- Kiradi: API'dan buyruq, Scheduler'dan vazifa.
- Chiqadi: natija va tizim holati.
- Bog'liq: hamma engine'lar, Memory System.

## 2. Memory System — xotira

- Vazifasi: egasi, maqsadlar, rejalar, bajarilgan vazifalar, xatolar, muhim qarorlar, tadqiqot natijalari va suhbatlardan kerakli ma'lumotni uzoq muddat saqlash.
- Kiradi: engine'lardan yozish so'rovlari.
- Chiqadi: so'ralgan ma'lumot.
- Texnologiya: SQLite (tuzilgan ma'lumot) va Markdown (matnli hisobotlar).

## 3. AI Gateway — AI modellar markazi

- Vazifasi: turli AI modellarni ulash, ular orasida almashish, bepul va arzon modellarni qo'llab-quvvatlash, API xatolarini boshqarish, asosiy model ishlamasa zaxirasiga o'tish.
- Kiradi: engine'lardan so'rov (matn).
- Chiqadi: modeldan javob yoki aniq xato xabari.
- Bog'liq: tashqi AI xizmatlari.

## 4. Research Engine — tadqiqotchi

- Vazifasi: internetdan ma'lumot izlash, AI va IT yangiliklarini o'rganish, kelajak texnologiyalarini tahlil qilish, yangi imkoniyatlarni topish, kunlik tadqiqot hisoboti.
- Kiradi: mavzu yoki kunlik vazifa.
- Chiqadi: Markdown hisobot (Memory'ga saqlanadi).
- Bog'liq: AI Gateway, internet, Memory.

## 5. Mentor Engine — shaxsiy ustoz

- Vazifasi: egasining maqsadlarini bilish, kunlik va haftalik reja tuzish, aniq vazifa berish, natijani baholash, kamchiliklarni aniqlash, rivojlanish strategiyasini yangilash.
- Kiradi: maqsadlar, Analyst hisobotlari.
- Chiqadi: kunlik vazifalar va baho.
- Bog'liq: Memory, Analyst, AI Gateway.

## 6. Analyst Engine — tahlilchi

- Vazifasi: kundalik natijalarni tahlil qilish, reja bilan amaliy natijani solishtirish, takrorlanayotgan xatolarni topish, rivojlanish darajasini baholash, haftalik hisobot.
- Kiradi: bajarilgan va bajarilmagan vazifalar.
- Chiqadi: haftalik hisobot, xatolar ro'yxati.
- Bog'liq: Memory, AI Gateway.

## 7. Business Intelligence — biznes tahlilchisi

- Vazifasi: bozorni o'rganish, raqobatchilarni tahlil qilish, AI orqali daromad imkoniyatlarini izlash, biznes g'oyalarini baholash, daromad strategiyalarini tayyorlash.
- Kiradi: Research natijalari, egasining maqsadlari.
- Chiqadi: g'oyalar bahosi va tavsiyalar.
- Bog'liq: Research, Memory, AI Gateway.

## 8. Strategist Engine — strateg

- Vazifasi: 30 kunlik reja, 90 kunlik strategiya, bir yillik maqsadlar, eng foydali yo'nalishni tanlash, natijaga qarab strategiyani yangilash.
- Kiradi: Analyst hisobotlari, BI tavsiyalari, maqsadlar.
- Chiqadi: yangilangan reja va strategiya.
- Bog'liq: Analyst, BI, Memory.

## 9. Scheduler — avtomatik boshqaruv

- Vazifasi: belgilangan vaqtda vazifalarni ishga tushirish (tadqiqot, kunlik hisobot), rejalangan ishlarni tekshirish, orqa fonda ishlash.
- Kiradi: jadval (qachon nima qilinishi).
- Chiqadi: Core'ga vazifa.
- Eslatma: Scheduler o'zi qaror qilmaydi, faqat vaqtida ishga tushiradi.

## 10. Android Interface — telefon ilovasi

- Vazifasi: AI bilan suhbat, ovozli muloqot, kunlik vazifalar, rivojlanish statistikasi, tadqiqot hisobotlari, xotirani ko'rish, tizim holati, sozlamalar.
- Aloqa: faqat FastAPI (REST API) orqali.
- Eslatma: ishlab chiqish eng oxirgi bosqichda.