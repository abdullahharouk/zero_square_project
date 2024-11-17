from state import state
import algorithem
import player

map1 = state(11)
map1.fill_const_col(1, 6, 0, "black", "⬛️")
map1.fill_const_col(6, 6, 1, "black", "⬛️")
map1.fill_const_col(1, 3, 9, "black", "⬛️")
map1.fill_const_col(3, 5, 10, "black", "⬛️")
map1.fill_const_col(5, 5, 9, "black", "⬛️")
map1.fill_const_row(1, 6, 5, "black", "⬛️")
map1.fill_const_row(2, 6, 5, "black", "⬛️")
map1.fill_const_row(1, 1, 0, "black", "⬛️")
map1.fill_const_row(0, 1, 5, "black", "⬛️")
map1.fill_const_row(1, 7, 9, "black", "⬛️")
map1.fill_const_row(4, 6, 4, "black", "⬛️")
map1.fill_const_row(6, 9, 4, "black", "⬛️")
map1.fill_const_row(7, 4, 1, "black", "⬛️")


map1.fill_color_cell(6, 2, "blue", "🟦", False, False)
map1.fill_color_cell(1, 2, "red", "🟥", False, False)
map1.fill_color_cell(2, 7, "blue", "🔵", True, False)
map1.fill_color_cell(4, 10, "red", "🔴", True, False)


# map2 = algorithem.DFS(map1)

# for item in map2.get("path"):
#     item.print_map()
#     print("@" * 100)

# print(f"the path length is : {map2.get("path_len")}")
# print(f"the visited state number is : {map2.get("visited_len")}")

# print("#" * 300)


# map3 = algorithem.BFS(map1)

# for item in map3.get("path"):
#     item.print_map()
#     print("@" * 100)

# print(f"the path length is : {map3.get("path_len")}")
# print(f"the visited state number is : {map3.get("visited_len")}")


# map1.print_map()
# print("#" * 100)


# next = state.next_state(map1)
# for item in next:
#     item.print_map()
#     print("#" * 100)


# player.play_game(map1)
# solution (u,l,d,r,u,r,d,r,d,r,u,l)


# map2 = state(9)
# map2.fill_color_cell(0, 0, "red", "🟥", False, False)
# # map2.fill_color_cell(1, 0, "red", "🟥", False, False)
# map2.fill_color_cell(4, 0, "red", "🔴", True, False)
# # map2.fill_color_cell(5, 0, "blue", "🔵", True, False)
# # map2.fill_color_cell(6, 0, "blue", "🔵", True, False)
# map2.print_map()
# print("#" * 100)


# print("#" * 100)
# map4 = state.right_move(map3)
# map4.print_map()
