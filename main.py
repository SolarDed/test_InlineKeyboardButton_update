import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)
from aiogram.filters import CommandStart

BOT_TOKEN = ""

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Да",
                    callback_data="yes",
                    style="success"   
                ),
                InlineKeyboardButton(
                    text="❌ Нет",
                    callback_data="no",
                    style="danger"
                )
            ]
        ]
    )

    await message.answer(
        text="Тестируем кнопки",
        reply_markup=keyboard
    )


@dp.callback_query()
async def callbacks(callback: CallbackQuery):
    if callback.data == "yes":
        await callback.answer("Вы нажали ДА ✅")
    elif callback.data == "no":
        await callback.answer("Вы нажали НЕТ ❌")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
