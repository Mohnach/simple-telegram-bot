
import ephem
from datetime import date, datetime

def current_date():
    today = date.today()
    return today.strftime("%Y/%m/%d")

def planet_info(bot, update):
    user_text = update.message.text.split()
    if len(user_text) != 2:
        error_text = 'Необходим 1 аргумент'
        print(error_text)
        update.message.reply_text(error_text)
        return

    planet_name = user_text[1].title()
    print(current_date())

    planet_builder = None
    try:
        planet_builder = getattr(ephem, planet_name)
    except AttributeError:
        error_text = 'Нет информации по вашей планете'
        print(error_text)
        update.message.reply_text(error_text)
        return

    if planet_builder is not None:
        planet = planet_builder(current_date())
        const = ephem.constellation(planet)
        answer = f'Сегодня планета {planet_name} в созвездии {const[1]}'
        print(answer)
        update.message.reply_text(answer)


def next_moon(bot, update):
    user_text = update.message.text.split()
    date = None
    if len(user_text) == 1:
        date = current_date()
    else:
        try:
            date = datetime.strptime(user_text[1], "%d.%m.%Y")
        except ValueError:
            error_text = 'Дата должна быть в формате day.month.year'
            print(error_text)
            update.message.reply_text(error_text)

    full_moon_date = ephem.next_full_moon(date).datetime()
    print(full_moon_date)
    answer = f'Дата следующего полнолуния: {full_moon_date.strftime("%d.%m.%Y")}'
    print(answer)
    update.message.reply_text(answer)
