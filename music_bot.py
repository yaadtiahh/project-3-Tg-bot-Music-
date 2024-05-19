import os
import telebot
from dotenv import load_dotenv


load_dotenv()
tg_bot_token = os.environ.get("TG_BOT_TOKEN")
bot = telebot.TeleBot(tg_bot_token)

# Словарь с музыкальными подборками
playlists = {
    "Вечеринка": [
        "Party Rock Anthem - LMFAO",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "Can't Stop the Feeling! - Justin Timberlake",
        "Sexy and I Know It - LMFAO",
        "I Gotta Feeling - The Black Eyed Peas",
    ],
    "Поездка в машине": [
        "On the Road Again - Willie Nelson",
        "Drive - The Cars",
        "Take It Easy - Eagles",
        "Born to Run - Bruce Springsteen",
        "Life is a Highway - Tom Cochrane",
    ],
    "Расслабление": [
        "Weightless - Marconi Union",
        "Clair de Lune - Claude Debussy",
        "Thinking Out Loud - Ed Sheeran",
        "Gravity - John Mayer",
        "River Flows in You - Yiruma",
    ],
    "Тренировка": [
        "Eye of the Tiger - Survivor",
        "Stronger - Kanye West",
        "Lose Yourself - Eminem",
        "Till I Collapse - Eminem ft. Nate Dogg",
        "Push It - Salt-N-Pepa",
    ],
}

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Веселюсь", "В дороге", "Отдыхаю", "Тренеруюсь")
    bot.send_message(message.chat.id, "Привет! Чем ты сейчас занимаешься?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_profile(message):
    if message.text == 'Веселюсь':
        party_link = "https://music.yandex.by/users/music.partners/playlists/1881"
        bot.send_message(message.chat.id, f"Я подобрал для тебя пару треков:")
        for track in playlists['Вечеринка']:
            bot.send_message(message.chat.id,track)
        bot.send_message(message.chat.id, f"А также вот тебе подборка с Яндекс музыки:{party_link}")

    elif message.text == 'В дороге':
        trip_link = "https://music.yandex.by/users/music-blog/playlists/1868"
        bot.send_message(message.chat.id, f"Думаю тебе стоит послушать эти треки:")
        for track in playlists['Поездка в машине']:
            bot.send_message(message.chat.id,track)
        bot.send_message(message.chat.id, f"А также вот тебе подборка с Яндекс музыки:{trip_link}")

    elif message.text == 'Отдыхаю':
        chill_link = "https://music.yandex.by/users/music-blog/playlists/2467"
        bot.send_message(message.chat.id, f"Я думаю для тебя подойдут следующие треки:")
        for track in playlists['Расслабление']:
            bot.send_message(message.chat.id,track)
        bot.send_message(message.chat.id, f"А также вот тебе подборка с Яндекс музыки:{chill_link}")

    elif message.text == 'Тренеруюсь':
        workout_link = "https://music.yandex.by/users/music-blog/playlists/1585"
        bot.send_message(message.chat.id, f"Мне кажется для тебя сейчас не будет ничего лучше, чем послушать вот эти треки:")
        for track in playlists['Тренировка']:
            bot.send_message(message.chat.id,track)
        bot.send_message(message.chat.id, f"А также вот тебе подборка с Яндекс музыки:{workout_link}")
    else:
        bot.send_message(message.chat.id, 'Я вас не понял, признавайтесь что вы сейчас делаете!')


bot.polling(none_stop=True, interval=0)
