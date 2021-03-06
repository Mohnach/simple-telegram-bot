"""
Basic telegram bot
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from basic_answers import greet_user, talk_to_me
from ephem_skills import planet_info, next_moon
from words_skills import words_counter
from cities_game import cities_game

# Настройки прокси
PROXY = {
    'proxy_url': 'socks5h://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater("KEY", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(CommandHandler("next_full_moon", next_moon))
    dp.add_handler(CommandHandler("wordcount", words_counter))
    dp.add_handler(CommandHandler("game", cities_game))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
