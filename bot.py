import telebot
import config
import func

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['para'])
def welcome(message):
    sti = open('stickers/' + func.getPara(), 'rb')
    bot.send_sticker(message.chat.id, sti)


# RUN
bot.polling(none_stop=True)
