def welcome(name):
    print(f'''Hello {name} and welcome to the Wold of Games (WoG).
Here you can fid many cool games to play.''')

def get_game():
    # print(type(game_choose), game_choose)
    return input('Please choose the game from 1 to 3: ')

def get_difficulty():
    return input('Please choose game difficulty from 1 to 5: ')

def is_digital(num):
    return num.isdigit()

def num_is_valid (num, max):
    if num > max or num < 1:
        return False
    else:
        return True

def load_game():
    max_of_games = 3
    max_of_difficulty = 5
    game_choose = 0
    game_difficulty = 0
    game_ok = False
    difficulty_ok = False

    print('''1. Memory Game - a sequence of numbers will appear for 1 second and you have toguess it back
2. MGuess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')

    # check the game number parameters
    while not game_ok:
        game_choose = get_game()
        if is_digital(str(game_choose)):
           if num_is_valid(int(game_choose), max_of_games):
               game_ok = True

    #check the difficulty parameter is valid
    while not difficulty_ok:
        game_difficulty = get_difficulty()
        if is_digital(str(game_difficulty)):
            if num_is_valid(int(game_difficulty), max_of_difficulty):
                difficulty_ok = True

    return game_choose, game_difficulty


