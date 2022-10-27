candy = 100
candys = 100
players = {"playerOne": 0, "playerTwo": 0}

def start():
    print("Начало игры!")
    choise_player = input("С кем хотите играть? (для выбора введите 'Игрок' или 'Компьютер') - ")
    if choise_player.lower() == "игрок":
        play_vs_play()
    else:
        play_vs_comp()

def step(player):
    try:
        perem = int(input(f"{player} введите число = "))
        while perem < 1 or perem > 28:
            perem = int(input(f"{player} введите число меньше 28 и больше 0 ="))
        players[f"{player}"] = players[f"{player}"] + perem
        return perem
    except:
        print("Не число")

def winner(player):
    global candys
    for key, values in players.items():
        if key == player:
            players[key] = candys
        else:
            players[key] = 0
    for key, values in players.items():
        if values != 0:
            print(f"{key} win!")

def play_vs_play():
    global candy
    while candy > 0:
        for key, values in players.items():
            candy = candy - step(key)
            print(values)
            print(candy)
            if candy == 0:
                winner(key)
                break

def play_vs_comp():
    global candy
    while candy > 0:
        for key, values in players.items():
            if candy > 28 and key == "playerTwo":
                candies = candy % 29
                if candies == 0:
                    candies = 28
                players[key] += candies
                candy = candy - candies
            elif key == "playerTwo":
                candies = candy
                players[key] += candies
                candy = candy - candies
            else:
                candy = candy - step(key)
            print(values)
            print(candy)
            if candy == 0:
                winner(key)
                break

start()

print(players)