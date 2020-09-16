import telebot
import urllib3
import urllib.request

bot = telebot.TeleBot('1033970790:AAHgVbhB3yDw38jC4CIiEoi6jzbP5k_h0HQ')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Моё расписание', 'Goodbye')

link = "https://www.sibsiu.ru/files/raspisanie/iitias/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D0%B8%D0%B9/1%20%D0%BA%D1%83%D1%80%D1%81%20%D0%9E%D1%81%D0%B5%D0%BD%D0%BD%D0%B8%D0%B9%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80%202020-2021.pdf"

def saver(link):
    http = urllib3.PoolManager()
    r = http.request('GET', link)

    with open('1 курс Осенний семестр 2020-2021.pdf', 'wb') as f:
        f.write(r.data)

    # urllib.request.urlretrieve(link, "file.pdf")
    # print(link)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'моё расписание':
        bot.send_message(message.chat.id, 'Вот твое расписание\nИнститут ИТиАС 1 курс')
        saver(link)
        bot.send_document(message.chat.id, open('1 курс Осенний семестр 2020-2021.pdf', 'rb'))
    elif message.text.lower() == 'goodbye':
        bot.send_message(message.chat.id, 'Пока, человек!')

bot.polling()
