from state import state
import algorithem
import player

from state import state


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
map1.fill_color_cell(4, 9, "red", "🔴", True, False)
map1.print_map()

# player.play_game(map1)

map2 = algorithem.A_star(map1)

for item in map2.get("path"):
    item.print_map()
    print("@" * 100)

print(f"the path length is : {map2.get("path_len")}")
print(f"the visited state number is : {map2.get("visited_len")}")


map3 = algorithem.simple_hill_climbing(map1)

for item in map3.get("path"):
    item.print_map()
    print("@" * 100)

print(f"the path length is : {map3.get("path_len")}")

for item in map3.get("visited_len"):
    item.print_map()
    print("@" * 100)


map3 = algorithem.steepest_hill_climbing(map1)

for item in map3.get("path"):
    item.print_map()
    print("@" * 100)

print(f"the path length is : {map3.get("path_len")}")

for item in map3.get("visited_len"):
    item.print_map()
    print("@" * 100)


# map4 = algorithem.DFS_R(map1)

# for item in map4.get("path"):
#     item.print_map()
#     print("@" * 100)

# print(f"the path length is : {map4.get("path_len")}")
# print(f"the visited state number is : {map4.get("visited_len")}")


# map5 = algorithem.UCS(map1)

# for item in map5.get("path"):
#     item.print_map()
#     print("@" * 100)

# print(f"the path length is : {map5.get("path_len")}")
# print(f"the visited state number is : {map5.get("visited_len")}")


# map1 = state(11)
# map1.fill_const_col(1, 6, 0, "black", "⬛️")
# map1.fill_const_col(6, 6, 1, "black", "⬛️")
# map1.fill_const_col(1, 3, 9, "black", "⬛️")
# map1.fill_const_col(3, 5, 10, "black", "⬛️")
# map1.fill_const_col(5, 5, 9, "black", "⬛️")
# map1.fill_const_row(1, 6, 5, "black", "⬛️")
# map1.fill_const_row(2, 6, 5, "black", "⬛️")
# map1.fill_const_row(1, 1, 0, "black", "⬛️")
# map1.fill_const_row(0, 1, 5, "black", "⬛️")
# map1.fill_const_row(1, 7, 9, "black", "⬛️")
# map1.fill_const_row(4, 6, 4, "black", "⬛️")
# map1.fill_const_row(6, 9, 4, "black", "⬛️")
# map1.fill_const_row(7, 4, 1, "black", "⬛️")


# map1.fill_color_cell(6, 2, "blue", "🟦", False, False)
# # map1.fill_color_cell(1, 2, "red", "🟥", False, False)
# map1.fill_color_cell(1, 4, "blue", "🔵", True, False)
# # map1.fill_color_cell(4, 10, "red", "🔴", True, False)


# map2 = algorithem.hill_climbing(map1)

# for item in map2.get("path"):
#     item.print_map()
#     print("@" * 100)

# print(f"the path length is : {map2.get("path_len")}")
# print(f"the visited state number is : {map2.get("visited_len")}")


# map1 = state(11)
# map1.fill_const_col(1, 6, 0, "black", "⬛️")
# map1.fill_const_col(6, 6, 1, "black", "⬛️")
# map1.fill_const_col(1, 3, 9, "black", "⬛️")
# map1.fill_const_col(3, 5, 10, "black", "⬛️")
# map1.fill_const_col(5, 5, 9, "black", "⬛️")
# map1.fill_const_row(1, 6, 5, "black", "⬛️")
# map1.fill_const_row(2, 6, 5, "black", "⬛️")
# map1.fill_const_row(1, 1, 0, "black", "⬛️")
# map1.fill_const_row(0, 1, 5, "black", "⬛️")
# map1.fill_const_row(1, 7, 9, "black", "⬛️")
# map1.fill_const_row(4, 6, 4, "black", "⬛️")
# map1.fill_const_row(6, 9, 4, "black", "⬛️")
# map1.fill_const_row(7, 4, 1, "black", "⬛️")


# map1.fill_color_cell(6, 2, "blue", "🟦", False, False)
# # map1.fill_color_cell(1, 2, "red", "🟥", False, False)
# map1.fill_color_cell(1, 4, "blue", "🔵", True, False)
# # map1.fill_color_cell(4, 10, "red", "🔴", True, False)


# map2 = algorithem.hill_climbing(map1)

# for item in map2.get("path"):
#     item.print_map()
#     print("@" * 100)

# print(f"the path length is : {map2.get("path_len")}")
# print(f"the visited state number is : {map2.get("visited_len")}")

# print("#" * 300)
# map2 = algorithem.UCS(map1)

# for item in map2.get("path"):
#     item.print_map()
#     print("@" * 100)

# print(f"the path length is : {map2.get("path_len")}")
# print(f"the visited state number is : {map2.get("visited_len")}")


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


# map5 = state(16)
# map5.fill_const_row(1, 0, 4, "black", "⬛️")
# map5.fill_const_row(0, 3, 8, "black", "⬛️")
# map5.fill_const_row(0, 10, 15, "black", "⬛️")
# map5.fill_const_row(1, 8, 10, "black", "⬛️")
# map5.fill_const_col(1, 4, 0, "black", "⬛️")
# map5.fill_const_row(1, 12, 13, "black", "⬛️")
# map5.fill_const_col(0, 4, 15, "black", "⬛️")
# map5.fill_const_row(4, 1, 4, "black", "⬛️")
# map5.fill_const_row(4, 6, 7, "black", "⬛️")
# map5.fill_const_row(5, 4, 7, "black", "⬛️")
# map5.fill_const_row(4, 9, 15, "black", "⬛️")
# map5.fill_const_col(2, 2, 6, "black", "⬛️")
# map5.fill_const_col(3, 3, 12, "black", "⬛️")
# map5.fill_const_col(5, 5, 9, "black", "⬛️")


# map5.fill_color_cell(2, 2, "blue", "🟦", False, False)
# map5.fill_color_cell(2, 1, "red", "🟥", False, False)
# map5.fill_color_cell(3, 1, "yellow", "🟨", False, False)
# map5.fill_color_cell(2, 3, "green", "🟩", False, False)
# map5.fill_color_cell(3, 2, "purple", "🟪", False, False)

# map5.fill_color_cell(4, 8, "blue", "🔵", True, False)
# map5.fill_color_cell(1, 7, "purple", "🟣", True, False)
# map5.fill_color_cell(1, 14, "green", "🟢", True, False)
# map5.fill_color_cell(4, 5, "?", "🔶", True, False)
# map5.fill_color_cell(1, 11, "yellow", "🟡", True, False)


# # 🟨🟪🟩🟡🟣🟢

# map2 = algorithem.BFS(map5)

# for item in map2.get("path"):
#     item.print_map()
#     print("@" * 100)

# print(f"the path length is : {map2.get("path_len")}")
# print(f"the visited state number is : {map2.get("visited_len")}")


map5 = state(9)
map5.fill_const_col(1, 4, 0, "black", "⬛️")
