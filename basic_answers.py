
def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    print(update)

    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
