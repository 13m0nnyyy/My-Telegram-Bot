import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

API_TOKEN = "8083855809:AAEEWBl0R9dIKSDLJxw7GhR0ouLRABkLeB4"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(commands=["start"])
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Скажи Привіт", callback_data="say_hi")],
            [InlineKeyboardButton(text="Жарт", callback_data="joke")],
        ]
    )
    await message.answer("Натисни кнопку нижче:", reply_markup=keyboard)


@dp.callback_query()
async def handle_callback(callback: CallbackQuery):
    data = callback.data
    if data == "say_hi":
        await callback.message.answer("Привіт, друже! 🌟")
    elif data == "joke":
        await callback.message.answer("Чому Python не їде велосипедом? — Бо не має коліс! 😄")
    await callback.answer()  

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())