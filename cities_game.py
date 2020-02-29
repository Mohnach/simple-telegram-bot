dict_of_games = {}

class CitiesGame:
    def __init__(self, player):
        self.player = str(player)
        self.init_base()
       # print(self.cities_base)

    def human_turn(self, city):
        # попытка найти город в списке
        # если нашли
        #   фиксируем букву
        #   передаем ход боту
        self.check_cities_list()
        
        print(city)

        if self.last_letter != '':
           if city[0] != self.last_letter.upper():
               raise ValueError(f'Ваш город должен начинаться на {self.last_letter}')

        if city in self.cities_base:
            self.set_last_letter(city)
            print(self.last_letter)
            self.cities_base.remove(city)
        else:
            print("Недопустимый ход")
            raise ValueError("Недопустимый ход")

    def bot_turn(self, update):
        # ищем город на заданную букву
        # Если нашли
        #   , то возвращаем город
        #   и устанавливаем букву
        #   передаем ход
        # иначе
        #   - бот проиграл
        self.check_cities_list()

        for city in self.cities_base:
            if city[0] == self.last_letter.upper():
                update.message.reply_text(f'Ход бота: {city}')
                
                self.set_last_letter(city)
                update.message.reply_text(f'Вам ходить с: {self.last_letter.upper()}')
                
                self.cities_base.remove(city)
                break
        else:
            print('game over')
            raise NameError('Бот сдается')

    def set_last_letter(self, city):
        last_letter = city[-1]
        if last_letter == 'ь':
            self.last_letter = city[-2]
        elif last_letter == 'й':
            self.last_letter = 'и'
        else:
            self.last_letter = last_letter

    def check_cities_list(self):
        if len(self.cities_base) == 0:
            print('game over')
            raise NameError('города закончились')

    def init_base(self):
        # инициализируем базу городов
        self.cities_base = []
        with open('data/cities.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.replace(' ','')
                line = line.replace('\n','')
                self.cities_base.append(line)
        

    def __repr__(self):
        return f'Game object. Player: {self.player}'

def init_game(update, name):
    # если юзер еще не играл,
    #   создаем базу
    #   разрешаем ход с любой буквы
    # иначе
    #   ход с текущей буквы
    game = dict_of_games.get(name)
    if game == None:
        print('create new game')
        dict_of_games[name]=CitiesGame(name)
        game = dict_of_games.get(name)
        print('ходи с любой буквы')
        game.last_letter = ''

    return game

def get_user_id(update):
    user_id = update.message.chat.id
    # message = update.get('message')
    # chat = message.get('chat')
    # print(chat.get('username'))
    print(update.message.chat.username)
    return user_id

def play_round(update, name, city):
    game = init_game(update, name)

    try:
        game.human_turn(city)
        # не передавать update внутрь игры
        game.bot_turn(update)
    except ValueError as try_again:
        update.message.reply_text(f'Попробуй еще: {try_again}')
    except NameError as game_over:
        update.message.reply_text(f'game over: {game_over}')
        del dict_of_games[name]

def cities_game(bot, update):

    user_text = update.message.text.split()
    if len(user_text) != 2:
        error_text = 'Необходим 1 аргумент'
        print(error_text)
        update.message.reply_text(error_text)
        return

    city = user_text[1].title()

    play_round(update, get_user_id(update), city)
    #update.message.reply_text(text)


if __name__ == "__main__":
    while True:
        turn = input("Твой ход: ")
        play_round(None, 'test', turn)
#    play_round('another','Москва')
#    play_round('test','Москва')
