field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]


def printf():
    print("  0 1 2")
    for i in range(0, 3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")


count = 0


def steps(count):
    print(f"Игрок номер {count % 2 + 1} введите поле")
    coords = list(map(int, input().split()))
    if len(coords) == 2:
        if 0<=coords[0]<=2 and 0<=coords[1]<=2:
            if count % 2 == 1:
                field[coords[0]][coords[1]] = 'x'
            else:
                field[coords[0]][coords[1]] = 'o'
        else:
            steps(count)
    else:
        steps(count)



def win(count):
    if (field[0][0] == field[0][1] == field[0][2] != ' ') or (field[1][0] == field[1][1] == field[1][2] != ' ') or (
            field[2][0] == field[2][1] == field[2][2] != ' ') or (field[0][0] == field[1][0] == field[2][0] != ' ') or (
            field[0][1] == field[1][1] == field[2][1] != ' ') or (field[0][2] == field[1][2] == field[2][2] != ' ') or (
            field[0][0] == field[1][1] == field[2][2] != ' ') or (field[0][2] == field[1][1] == field[2][0] != ' ') :
        if count % 2 == 0:
            print("Победил o")
            return True
        else:
            print("Победил x")
            return True
    else:
        return False

while True:
    printf()
    steps(count)
    if win(count):
        printf()
        break
    count += 1

