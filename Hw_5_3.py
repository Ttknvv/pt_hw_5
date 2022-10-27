player = {"firstPlayer": "x", "secondPlayer": "o"}

matrix = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]

def usl():
    if matrix[0][0] == "x" and matrix[1][0] == "x" and matrix[2][0] == "x":
        return "Player 1 Win!"
    elif matrix[0][1] == "x" and matrix[1][1] == "x" and matrix[2][1] == "x":
        return "Player 1 Win!"
    elif matrix[0][2] == "x" and matrix[1][2] == "x" and matrix[2][2] == "x":
        return "Player 1 Win!"
    elif matrix[0][0] == "x" and matrix[0][1] == "x" and matrix[0][2] == "x":
        return "Player 1 Win!"
    elif matrix[1][0] == "x" and matrix[1][1] == "x" and matrix[1][2] == "x":
        return "Player 1 Win!"
    elif matrix[2][0] == "x" and matrix[2][1] == "x" and matrix[2][2] == "x":
        return "Player 1 Win!"
    elif matrix[0][0] == "x" and matrix[1][1] == "x" and matrix[2][2] == "x":
        return "Player 1 Win!"
    elif matrix[0][2] == "x" and matrix[1][1] == "x" and matrix[0][2] == "x":
        return "Player 1 Win!"
    elif matrix[0][0] == "o" and matrix[1][0] == "o" and matrix[2][0] == "o":
        return "Player 2 Win!"
    elif matrix[0][1] == "o" and matrix[1][1] == "o" and matrix[2][1] == "o":
        return "Player 2 Win!"
    elif matrix[0][2] == "o" and matrix[1][2] == "o" and matrix[2][2] == "o":
        return "Player 2 Win!"
    elif matrix[0][0] == "o" and matrix[0][1] == "o" and matrix[0][2] == "o":
        return "Player 2 Win!"
    elif matrix[1][0] == "o" and matrix[1][1] == "o" and matrix[1][2] == "o":
        return "Player 2 Win!"
    elif matrix[2][0] == "o" and matrix[2][1] == "o" and matrix[2][2] == "o":
        return "Player 2 Win!"
    elif matrix[0][0] == "o" and matrix[1][1] == "o" and matrix[2][2] == "o":
        return "Player 2 Win!"
    elif matrix[0][2] == "o" and matrix[1][1] == "o" and matrix[2][0] == "o":
        return "Player 2 Win!"
    else:
        return ""

def usl1():
    list = []
    for i in range(0, 3):
        for j in range(0, 3):
            list.append(matrix[i][j])
    if " " not in list:
        return "ничья!"
    else:
        return ""

def hod():
    while True:
        x = int(input("Введите номер строки = "))
        y = int(input("Введите номер столбца = "))
        if matrix[x - 1][y - 1] == " ":
            break
        else:
            print("Эта позиция уже занята")
    return x, y


while True:
    for key, value in player.items():
        x, y = hod()
        matrix[x - 1][y - 1] = value
        for i in matrix:
            print(i)
        if usl() != "":
            print(usl())
            break
        elif usl1() != "":
            print(usl1())
            break