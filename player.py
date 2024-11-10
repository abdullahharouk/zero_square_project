def play_game(cls, root_state):

    root_state.print_map()

    if root_state.is_finite():
        print("win")
    else:
        print("#######  enter 'r' or 'R' to move right  ########")
        print("#######  enter 'l' or 'L' to move left  ########")
        print("#######  enter 'd' or 'D' to move down  ########")
        print("#######  enter 'u' or 'U' to move up  ########")
        direction = input(" Enter the destination : ")

        if direction == "R" or direction == "r":
            next_state = cls.right_move(root_state)
            cls.play_game(next_state)
        elif direction == "L" or direction == "l":
            next_state = cls.left_move(root_state)
            cls.play_game(next_state)
        elif direction == "U" or direction == "u":
            next_state = cls.up_move(root_state)
            cls.play_game(next_state)
        elif direction == "D" or direction == "d":
            next_state = cls.down_move(root_state)
            cls.play_game(next_state)
        else:
            print("inncorect input")
            cls.play_game(root_state)
