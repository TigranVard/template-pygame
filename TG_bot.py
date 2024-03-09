import telebot

API_TOKEN = "7174008273:AAGPeAqDKggonAOhzzV3M4WMRk3X2mB0Y8M"


bot = telebot.TeleBot(API_TOKEN)

photo = open('./Оладушки.jpg', 'rb')

oladi = 'Ингредиенты\nМолоко 2 стакан = 400 г \nЯйца  2 шт. = 120 г \nРжаная мука 1 стакан = 130 г \nСоль 5 г \nСахар 1 ст. л. = 25 г'

photo_vish = open('./vish.jpg', 'rb')

vish = 'Ингредиенты\nШоколад 50 Грамм\nВишня вяленая 12 Штук\nКоньяк 30 Миллилитров\nВода 60 Миллилитров\nКукурузный крахмал 1 Чайная ложка\nСахар 2 Ст. ложки' 

pelmen = 'ДЛЯ ТЕСТА:\nПшеничная мука 500 гр\nВода250 мл\nСоль (без горки)1 чайн.л.''\nДЛЯ НАЧИНКИ:\nГовядина 500 гр.\nЛук репчатый 2 шт.\nВода (холодная) 500 мл.\nЗелень кинзы 1 пуч.\nПетрушка по вкусу\nСпеции сухие по вкусу\nПерец красный молотый по вкусу\nПерец черный молотый по вкусу\nСоль по вкусу'

photo_pelmen = open('./hinkal.jpg','rb')

@bot.message_handler(command=["start"])
def start (message):
    markup = telebot.types.InlineKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.InlineKeyboardButton(text="Пьяная Вишня")
    markup.add(button1)
    bot.send_message(message.chat_id, "Привет, выбирай команду", reply_markup=markup)
    markup = telebot.types.InlineKeyboardMarkup(resize_keyboard=True)
    button2 = telebot.types.InlineKeyboardButton(text="Хинкальи")
    markup.add(button2)
    bot.send_message(message.chat_id, "Привет, выбирай команду", reply_markup=markup)
    markup = telebot.types.InlineKeyboardMarkup(resize_keyboard=True)
    button3 = telebot.types.InlineKeyboardButton(text="Оладьи")
    markup.add(button3)
    bot.send_message(message.chat_id, "Привет, выбирай команду", reply_markup=markup)


@bot.message_handler(content_types=['text','video','document'])
def get_tex_message(message):
    chat_id = message.from_user.id
    if message.text == "Привет":
        bot.send_message(chat_id, f'Привет, {message.from_user.username}')
    elif message.text == "/start":
        bot.send_message(chat_id, 'Привет')
    elif message.text == "Сколько прошло секунд с 1970 года?":
        bot.send_message(chat_id, message.date)
    elif message.text == "Рецепт оладушек":
        bot.send_message(chat_id, oladi)
        bot.send_photo(chat_id, photo)
    elif message.text == "Рецепт Пьяная вишня":
        bot.send_message(chat_id, vish)
        bot.send_photo(chat_id, photo_vish)
    elif message.text == "Рецепт Хинкаль":
        bot.send_message(chat_id, pelmen)
        bot.send_photo(chat_id, photo_pelmen)


bot.polling(none_stop=True,interval=0)