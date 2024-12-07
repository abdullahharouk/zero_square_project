from state import state
import algorithem
import player
import numpy as np
from state import state
from colorsquare import color_square

import logging
import time
# import tracemalloc

logging.basicConfig(
    filename="level_30.log",
    level=logging.INFO,
    format="%(message)s",
)

logging.info("--------------------BFS--------------------")

# tracemalloc.start()

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


start_time = time.time()
map2 = algorithem.BFS(map30)
end_time = time.time()
path_length = map2.get("path_len")
visited_length = map2.get("visited_len")
cost = map2.get("cost")
end_time = time.time()
logging.info(f"Path length: {path_length}")
logging.info(f"Visited state number: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")
# current, peak = tracemalloc.get_traced_memory()
# logging.info(f"Current memory usage: {current / 10**6:.2f} MB")
# tracemalloc.stop()

logging.info("--------------------BFS FINISHED--------------------")
logging.info("\n\n")


####################################################################################################################


logging.info("--------------------DFS--------------------")

# tracemalloc.start()

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


start_time = time.time()
map2 = algorithem.DFS(map30)
end_time = time.time()
path_length = map2.get("path_len")
visited_length = map2.get("visited_len")
cost = map2.get("cost")
end_time = time.time()
logging.info(f"Path length: {path_length}")
logging.info(f"Visited state number: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")
# current, peak = tracemalloc.get_traced_memory()
# logging.info(f"Current memory usage: {current / 10**6:.2f} MB")
# tracemalloc.stop()

logging.info("--------------------DFS FINISHED--------------------")
logging.info("\n\n")
####################################################################################################################


logging.info("--------------------DFS_R--------------------")

# tracemalloc.start()

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


start_time = time.time()
map2 = algorithem.DFS_R(map30)
end_time = time.time()
path_length = map2.get("path_len")
visited_length = map2.get("visited_len")
cost = map2.get("cost")
end_time = time.time()
logging.info(f"Path length: {path_length}")
logging.info(f"Visited state number: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")
# current, peak = tracemalloc.get_traced_memory()
# logging.info(f"Current memory usage: {current / 10**6:.2f} MB")
# tracemalloc.stop()

logging.info("--------------------DFS_R FINISHED--------------------")
logging.info("\n\n")




####################################################################################################################


logging.info("--------------------UCS--------------------")

# tracemalloc.start()

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


start_time = time.time()
map2 = algorithem.UCS(map30)
end_time = time.time()
path_length = map2.get("path_len")
visited_length = map2.get("visited_len")
cost = map2.get("cost")
end_time = time.time()
logging.info(f"Path length: {path_length}")
logging.info(f"Visited state number: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")
# current, peak = tracemalloc.get_traced_memory()
# logging.info(f"Current memory usage: {current / 10**6:.2f} MB")
# tracemalloc.stop()

logging.info("--------------------UCS FINISHED--------------------")
logging.info("\n\n")


####################################################################################################################


logging.info("--------------------A_STAR--------------------")

# tracemalloc.start()

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


start_time = time.time()
map2 = algorithem.A_star(map30)
end_time = time.time()
path_length = map2.get("path_len")
visited_length = map2.get("visited_len")
cost = map2.get("cost")
end_time = time.time()
logging.info(f"Path length: {path_length}")
logging.info(f"Visited state number: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")
# current, peak = tracemalloc.get_traced_memory()
# logging.info(f"Current memory usage: {current / 10**6:.2f} MB")
# tracemalloc.stop()

logging.info("--------------------A_STAR FINISHED--------------------")
logging.info("\n\n")



####################################################################################################################


logging.info("--------------------A_STAR_ADVANCE--------------------")

# tracemalloc.start()

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


start_time = time.time()
map2 = algorithem.A_star_advance(map30)
end_time = time.time()
path_length = map2.get("path_len")
visited_length = map2.get("visited_len")
cost = map2.get("cost")
end_time = time.time()
logging.info(f"Path length: {path_length}")
logging.info(f"Visited state number: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")
# current, peak = tracemalloc.get_traced_memory()
# logging.info(f"Current memory usage: {current / 10**6:.2f} MB")
# tracemalloc.stop()

logging.info("--------------------A_STAR_ADVANCE FINISHED--------------------")
logging.info("\n\n")
####################################################################################################################


logging.info("--------------------SIMPLE_HILL_CLIMBING--------------------")

# tracemalloc.start()

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


start_time = time.time()
map2 = algorithem.simple_hill_climbing(map30)
end_time = time.time()
path_length = map2.get("path_len")
visited_length = map2.get("visited_len")
cost = map2.get("cost")
end_time = time.time()
logging.info(f"Path length: {path_length}")
logging.info(f"Visited state number: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")
# current, peak = tracemalloc.get_traced_memory()
# logging.info(f"Current memory usage: {current / 10**6:.2f} MB")
# tracemalloc.stop()

logging.info("--------------------SIMPLE_HILL_CLIMBING FINISHED--------------------")
logging.info("\n\n")

####################################################################################################################


logging.info("--------------------STEEPEST_HILL_CLIMBING--------------------")

# tracemalloc.start()

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


start_time = time.time()
map2 = algorithem.steepest_hill_climbing(map30)
end_time = time.time()
path_length = map2.get("path_len")
visited_length = map2.get("visited_len")
cost = map2.get("cost")
end_time = time.time()
logging.info(f"Path length: {path_length}")
logging.info(f"Visited state number: {visited_length}")
logging.info(f"Cost: {cost}")
logging.info(f"Execution Time: {end_time - start_time:.4f} seconds")
# current, peak = tracemalloc.get_traced_memory()
# logging.info(f"Current memory usage: {current / 10**6:.2f} MB")
# tracemalloc.stop()

logging.info("--------------------STEEPEST_HILL_CLIMBING FINISHED--------------------")