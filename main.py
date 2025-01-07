def move(move_word, player_pos,map):
    y = player_pos[0]
    x = player_pos[1]
    if move_word == 'w' and map[y-1][x] !='#':
        return (y-1, x)
    if move_word == 's' and map[y+1][x] !='#':
        return (y+1, x)
    if move_word == 'a' and map[y][x-1] !='#':
        return (y, x-1)
    if move_word == 'd' and map[y][x+1] !='#':
        return (y, x+1)
    return player_pos

def print_maze(player_pos, map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if (y, x) == player_pos:
                print("I", end=" ")  # Отображение игрока
            elif map[y][x] == "#":
                print("#", end=" ")  # Стена
            elif map[y][x] == "%":
                print("%", end=" ")  # Выход
            else:
                print(".", end=" ")  # Пустое пространство
        print()

def main():
    map = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
           ["#", ".", "I", ".", ".", ".", ".", ".", ".", "#"],
           ["#", ".", "#", "#", "#", ".", "#", "#", ".", "#"],
           ["#", ".", ".", "#", "#", ".", "#", "#", ".", "#"],
           ["#", "#", ".", ".", ".", ".", ".", "#", "#", "#"],
           ["#", ".", ".", "#", ".", "#", ".", ".", ".", "#"],
           ["#", ".", "#", "#", ".", "#", ".", "#", "#", "#"],
           ["#", ".", ".", "#", "#", ".", ".", ".", ".", "#"],
           ["#", "#", ".", ".", "#", ".", "#", "#", ".", "#"],
           ["#", "#", "#", "#", "#", "%", "#", "#", "#", "#"]]
    player_pos = (1, 2)
    game_running = True
    while game_running:
        print_maze(player_pos,map)
        user_move = input("Введи в какую сторону хочешь пойти ").lower()
        if user_move in ['w', 's', 'd', 'a']:
            new_pos = move(user_move, player_pos, map)
            if new_pos == player_pos:
                print("Туда нельзя, там стена")
            else:
                print("Вы успешно переместились")
            player_pos = new_pos
            if map[player_pos[0]][player_pos[1]] == "%":
                print("Поздравляю! Ты нашел выход!")
                game_running = False
        else:
            print("Вы ввели неизвестную команду")



if __name__=="__main__":
    main()

