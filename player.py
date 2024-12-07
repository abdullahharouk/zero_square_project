def play_game(root_state):

    root_state.print_map()
    print(root_state.game_over)
    if root_state.is_finite():
        print("win")
    else:
        print("#######  enter 'r' or 'R' to move right  ########")
        print("#######  enter 'l' or 'L' to move left  ########")
        print("#######  enter 'd' or 'D' to move down  ########")
        print("#######  enter 'u' or 'U' to move up  ########")
        direction = input(" Enter the destination : ")

        if direction == "R" or direction == "r":
            next_state = root_state.right_move(root_state)
            play_game(next_state)
        elif direction == "L" or direction == "l":
            next_state = root_state.left_move(root_state)
            play_game(next_state)
        elif direction == "U" or direction == "u":
            next_state = root_state.up_move(root_state)
            play_game(next_state)
        elif direction == "D" or direction == "d":
            next_state = root_state.down_move(root_state)
            play_game(next_state)
        else:
            print("inncorect input")
            play_game(root_state)
