
def words_counter(bot, update):
    user_text = update.message.text

    delimiters = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for delimiter in delimiters:
        user_text = user_text.replace(delimiter, ' ')

    user_text = user_text.split()

    count = len(user_text) - 1
    answer = f'Число слов в вашей строке: {count}'
    print(answer)
    update.message.reply_text(answer)
