from state import state
import algorithem
import player
import numpy as np
from state import state
from colorsquare import color_square
import time


# # map1 = state(8, 11)
# # map1.fill_const_col(1, 6, 0, "black", "⬛️")
# # map1.fill_const_col(6, 6, 1, "black", "⬛️")
# # map1.fill_const_col(1, 3, 9, "black", "⬛️")
# # map1.fill_const_col(3, 5, 10, "black", "⬛️")
# # map1.fill_const_col(5, 5, 9, "black", "⬛️")
# # map1.fill_const_row(1, 6, 5, "black", "⬛️")
# # map1.fill_const_row(2, 6, 5, "black", "⬛️")
# # map1.fill_const_row(1, 1, 0, "black", "⬛️")
# # map1.fill_const_row(0, 1, 5, "black", "⬛️")
# # map1.fill_const_row(1, 7, 9, "black", "⬛️")
# # map1.fill_const_row(4, 6, 4, "black", "⬛️")
# # map1.fill_const_row(6, 9, 4, "black", "⬛️")
# # map1.fill_const_row(7, 4, 1, "black", "⬛️")


# # map1.fill_color_cell(6, 2, "blue", "🟦", False, False)
# # map1.fill_color_cell(1, 2, "red", "🟥", False, False)
# # map1.fill_color_cell(2, 7, "blue", "🔵", True, False)
# # map1.des.append([2, 7, "blue","🔵"])
# # map1.fill_color_cell(4, 9, "red", "🔴", True, False)

# # map1.des.append([4, 9, "red","🔴"])


# # # # player.play_game(map1)
# # start_time = time.time()
# # map2 = algorithem.A_star(map1)

# # for item in map2.get("path"):
# #     item.print_map()
# #     print (item.des)
# #     print("@" * 100)

# # print(f"the path length is : {map2.get("path_len")}")
# # print(f"the visited state number is : {map2.get("visited_len")}")
# # print(f"the cost : {map2.get("cost")}")
# # end_time = time.time()

# # print(f"BFS Execution Time: {end_time - start_time:.4f} seconds")


# # player.play_game(map1)
# # solution (u,l,d,r,u,r,d,r,d,r,u,l)


# # # # 🟨🟪🟩🟡🟣🟢

start_time = time.time()


map30 = state(6, 16)
map30.fill_const_row(1, 0, 4, "black", "⬛️")
map30.fill_const_row(0, 3, 8, "black", "⬛️")
map30.fill_const_row(0, 10, 15, "black", "⬛️")
map30.fill_const_row(1, 8, 10, "black", "⬛️")
map30.fill_const_col(1, 4, 0, "black", "⬛️")
map30.fill_const_row(1, 12, 13, "black", "⬛️")
map30.fill_const_col(0, 4, 15, "black", "⬛️")
map30.fill_const_row(4, 1, 4, "black", "⬛️")
map30.fill_const_row(4, 6, 7, "black", "⬛️")
map30.fill_const_row(5, 4, 7, "black", "⬛️")
map30.fill_const_row(4, 9, 15, "black", "⬛️")
map30.fill_const_col(2, 2, 6, "black", "⬛️")
map30.fill_const_col(3, 3, 12, "black", "⬛️")
map30.fill_const_col(5, 5, 9, "black", "⬛️")


map30.fill_color_cell(2, 2, "blue", "🟦", False, False)
map30.fill_color_cell(2, 1, "red", "🟥", False, False)
map30.fill_color_cell(3, 1, "yellow", "🟨", False, False)
map30.fill_color_cell(2, 3, "green", "🟩", False, False)
map30.fill_color_cell(3, 2, "purple", "🟪", False, False)

map30.fill_color_cell(5, 8, "b", "🔲", True, False)
map30.fill_color_cell(4, 8, "blue", "🔵", True, False)
map30.des.append([4, 8, "blue", "🔵"])
map30.fill_color_cell(1, 7, "purple", "🟣", True, False)
map30.des.append([1, 7, "purple", "🟣"])
map30.fill_color_cell(1, 14, "green", "🟢", True, False)
map30.des.append([1, 14, "green", "🟢"])
map30.fill_color_cell(4, 5, "?", "🔶", True, False)
map30.des.append([4, 5, "?", "🔶"])
map30.fill_color_cell(1, 11, "yellow", "🟡", True, False)
map30.des.append([1, 11, "yellow", "🟡"])


# map30.print_map()
map2 = algorithem.DFS_R(map30)

for item in map2.get("path"):
    item.print_map()
    print(item.des)
    print("@" * 100)

print(f"the path length is : {map2.get("path_len")}")
print(f"the visited state number is : {map2.get("visited_len")}")
print(f"the cost is : {map2.get("cost")}")
end_time = time.time()

print(f"BFS Execution Time: {end_time - start_time:.4f} seconds")


# map10 = state(8, 12)
# map10.fill_const_row(0, 2, 9, "black", "⬛️")
# map10.fill_const_row(7, 0, 11, "black", "⬛️")
# map10.fill_const_row(1, 1, 2, "black", "⬛️")
# map10.fill_const_row(2, 0, 1, "black", "⬛️")
# map10.fill_const_row(1, 9, 10, "black", "⬛️")
# map10.fill_const_row(2, 10, 11, "black", "⬛️")
# map10.fill_const_col(2, 7, 0, "black", "⬛️")
# map10.fill_const_col(2, 7, 11, "black", "⬛️")
# map10.fill_const_col(5, 6, 4, "black", "⬛️")
# map10.fill_const_col(4, 5, 5, "black", "⬛️")
# map10.fill_const_col(3, 4, 8, "black", "⬛️")
# map10.fill_const_col(4, 5, 9, "black", "⬛️")


# map10.fill_const_col(2, 2, 4, "black", "⬛️")
# map10.fill_const_col(3, 3, 3, "black", "⬛️")
# map10.fill_const_col(5, 5, 2, "black", "⬛️")
# map10.fill_const_col(2, 2, 7, "black", "⬛️")


# map10.fill_color_cell(5, 10, "blue", "🟦", False, False)
# map10.fill_color_cell(5, 1, "red", "🟥", False, False)
# map10.fill_color_cell(2, 6, "blue", "🔵", True, False)
# map10.des.append([2, 6, "blue", "🔵"])
# map10.fill_color_cell(3, 5, "red", "🔴", True, False)

# map10.des.append([3, 5, "red", "🔴"])
# # map20.fill_const_row(0, 3, 6, "black", "⬛️")
# # map20.fill_const_row(1, 6, 8, "black", "⬛️")
# # map20.fill_const_row(4, 0, 8, "black", "⬛️")
# # map20.fill_const_row(3, 3, 3, "black", "⬛️")
# # map20.fill_const_row(3, 6, 6, "black", "⬛️")
# # map20.fill_const_col(1, 4, 0, "black", "⬛️")
# # map20.fill_const_col(1, 4, 8, "black", "⬛️")


# # map20.fill_color_cell(3, 7, "yellow", "🟨", False, False)
# # map20.fill_color_cell(1, 4, "red", "🟥", False, False)
# # map20.fill_color_cell(2, 3, "blue", "🟦", False, False)
# # map20.fill_color_cell(2, 2, "purple", "🟪", False, False)
# # map20.fill_color_cell(3, 2, "green", "🟩", False, False)
# # map20.destination_array=np.append(map20.destination_array,color_square(3, 7, "green", "🟢", True, False))
# # map20.des.append([3, 7, "green", "🟢"])
# # map20.destination_array=np.append(map20.destination_array,color_square(3, 2, "purple", "🟣", True, False))
# # map20.des.append([3, 2, "purple", "🟣"])
# # map20.fill_color_cell(2, 1, "blue", "🔵", True, False)
# # map20.des.append([2, 1, "blue", "🔵"])
# # map20.fill_color_cell(3, 4, "red", "🔴", True, False)
# # map20.des.append([3, 4, "red", "🔴"])
# # map20.fill_color_cell(1, 5, "yellow", "🟡", True, False)
# # map20.des.append([1, 5, "yellow", "🟡"])

# map10.print_map()

# start_time = time.time()
# map2 = algorithem.BFS(map10)

# for item in map2.get("path"):
#     item.print_map()
#     print("@" * 100)

# print(f"the path length is : {map2.get("path_len")}")
# print(f"the visited state number is : {map2.get("visited_len")}")
# print(f"the cost : {map2.get("cost")}")
# end_time = time.time()

# print(f"BFS Execution Time: {end_time - start_time:.4f} seconds")

# map20 = state(5, 9)
# map20.fill_const_row(1, 0, 3, "black", "⬛️")
# map20.fill_const_row(0, 3, 6, "black", "⬛️")
# map20.fill_const_row(1, 6, 8, "black", "⬛️")
# map20.fill_const_row(4, 0, 8, "black", "⬛️")
# map20.fill_const_row(3, 3, 3, "black", "⬛️")
# map20.fill_const_row(3, 6, 6, "black", "⬛️")
# map20.fill_const_col(1, 4, 0, "black", "⬛️")
# map20.fill_const_col(1, 4, 8, "black", "⬛️")


# map20.fill_color_cell(3, 7, "yellow", "🟨", False, False)
# map20.fill_color_cell(1, 4, "red", "🟥", False, False)
# map20.fill_color_cell(2, 3, "blue", "🟦", False, False)
# map20.fill_color_cell(2, 2, "purple", "🟪", False, False)
# map20.fill_color_cell(3, 2, "green", "🟩", False, False)
# map20.destination_array=np.append(map20.destination_array,color_square(3, 7, "green", "🟢", True, False))
# map20.des.append([3, 7, "green", "🟢"])
# map20.destination_array=np.append(map20.destination_array,color_square(3, 2, "purple", "🟣", True, False))
# map20.des.append([3, 2, "purple", "🟣"])
# map20.fill_color_cell(2, 1, "blue", "🔵", True, False)
# map20.des.append([2, 1, "blue", "🔵"])
# map20.fill_color_cell(3, 4, "red", "🔴", True, False)
# map20.des.append([3, 4, "red", "🔴"])
# map20.fill_color_cell(1, 5, "yellow", "🟡", True, False)
# map20.des.append([1, 5, "yellow", "🟡"])


# start_time = time.time()
# map2 = algorithem.BFS(map20)

# for item in map2.get("path"):
#     item.print_map()
#     print("@" * 100)

# print(f"the path length is : {map2.get("path_len")}")
# print(f"the visited state number is : {map2.get("visited_len")}")
# print(f"the cost : {map2.get("cost")}")
# end_time = time.time()

# print(f"BFS Execution Time: {end_time - start_time:.4f} seconds")