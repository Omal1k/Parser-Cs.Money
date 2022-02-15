import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from main import collect_data
from aiogram.utils.markdown import hbold, hlink
import time 

bot = Bot(token='your_token', parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    
    start_buttons = ['Ножи', 'Штурмовые винтовки', 'AWP']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выбирите категорию', reply_markup=keyboard)

@dp.message_handler(Text(equals='Ножи'))
async def get_discount_knives(message: types.Message):
    await message.answer('Ожидайте...')
    collect_data(cat_type=2)
    with open('result.json') as file:
        data = json.load(file)
    
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)

@dp.message_handler(Text(equals='AWP'))
async def get_discount_awp(message: types.Message):
    await message.answer('Ожидайте...')
    collect_data(cat_type=4)
    with open('result.json') as file:
        data = json.load(file)
    
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)



@dp.message_handler(Text(equals='Штурмовые винтовки'))
async def get_discount_gloves(message: types.Message):
    await message.answer('Ожидайте...')
    collect_data(cat_type=3)
    with open('result.json') as file:
        data = json.load(file)
    
    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("item_price")}'

        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)

def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()