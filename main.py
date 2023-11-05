from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from taxi import get_route_info
import json
# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = '6896066546:AAG-kyR_bg_YfoP4tsAkTTTmx7_A-COXEH0'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды для запроса геопозиции пользователя
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton("Отправить мою геопозицию", request_location=True)
    keyboard.add(button)
    await message.answer("Привет 👋\nОтправь мне свою геопозицию, чтобы я получил информацию о спросе в твоем районе.", reply_markup=keyboard)
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def handle_location(message: types.Message):
    print(message)
    if "live_period" in message["location"]:
        print("WOW")
    latitude = message.location.latitude
    longitude = message.location.longitude
    routes = [longitude, latitude]
    price, demand, estimated_time = get_route_info(routes)
    await message.answer(f'Загруженность: {demand}\nМинимальная цена: {price}₽\nВремя подачи машины: {estimated_time}')

if __name__ == '__main__':

    executor.start_polling(dp)
