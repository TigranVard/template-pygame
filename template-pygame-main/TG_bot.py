import telebot

API_TOKEN = "7174008273:AAGPeAqDKggonAOhzzV3M4WMRk3X2mB0Y8M"


bot = telebot.TeleBot(API_TOKEN)

photo = open('./tort.jpg', 'rb')

@bot.message_handler(content_types=['text','video','document'])
def get_tex_message(message):
    chat_id = message.from_user.id
    if message.text == "Привет":
        bot.send_message(chat_id, 'я Алина, Повар-Кондитер ')
    elif message.text == "/start":
        bot.send_message(chat_id, 'Привет')
    elif message.text == "Сколько прошло секунд с 1970 года?":
        bot.send_message(chat_id, message.date)
    elif message.text == "Покажи торт":
        bot.send_photo(chat_id, photo)

bot.polling(none_stop=True,interval=0)