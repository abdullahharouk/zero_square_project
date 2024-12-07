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
    filename="level_20.log",
    level=logging.INFO,
    format="%(message)s",
)

logging.info("--------------------BFS--------------------")

# tracemalloc.start()

map20 = state(5, 9)
map20.fill_const_row(1, 0, 3, "black", "⬛️")
map20.fill_const_row(0, 3, 6, "black", "⬛️")
map20.fill_const_row(1, 6, 8, "black", "⬛️")
map20.fill_const_row(4, 0, 8, "black", "⬛️")
map20.fill_const_row(3, 3, 3, "black", "⬛️")
map20.fill_const_row(3, 6, 6, "black", "⬛️")
map20.fill_const_col(1, 4, 0, "black", "⬛️")
map20.fill_const_col(1, 4, 8, "black", "⬛️")


map20.fill_color_cell(3, 7, "yellow", "🟨", False, False)
map20.fill_color_cell(1, 4, "red", "🟥", False, False)
map20.fill_color_cell(2, 3, "blue", "🟦", False, False)
map20.fill_color_cell(2, 2, "purple", "🟪", False, False)
map20.fill_color_cell(3, 2, "green", "🟩", False, False)
map20.destination_array=np.append(map20.destination_array,color_square(3, 7, "green", "🟢", True, False))
map20.des.append([3, 7, "green", "🟢"])
map20.destination_array=np.append(map20.destination_array,color_square(3, 2, "purple", "🟣", True, False))
map20.des.append([3, 2, "purple", "🟣"])
map20.fill_color_cell(2, 1, "blue", "🔵", True, False)
map20.des.append([2, 1, "blue", "🔵"])
map20.fill_color_cell(3, 4, "red", "🔴", True, False)
map20.des.append([3, 4, "red", "🔴"])
map20.fill_color_cell(1, 5, "yellow", "🟡", True, False)
map20.des.append([1, 5, "yellow", "🟡"])


start_time = time.time()
map2 = algorithem.BFS(map20)
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

map20 = state(5, 9)
map20.fill_const_row(1, 0, 3, "black", "⬛️")
map20.fill_const_row(0, 3, 6, "black", "⬛️")
map20.fill_const_row(1, 6, 8, "black", "⬛️")
map20.fill_const_row(4, 0, 8, "black", "⬛️")
map20.fill_const_row(3, 3, 3, "black", "⬛️")
map20.fill_const_row(3, 6, 6, "black", "⬛️")
map20.fill_const_col(1, 4, 0, "black", "⬛️")
map20.fill_const_col(1, 4, 8, "black", "⬛️")


map20.fill_color_cell(3, 7, "yellow", "🟨", False, False)
map20.fill_color_cell(1, 4, "red", "🟥", False, False)
map20.fill_color_cell(2, 3, "blue", "🟦", False, False)
map20.fill_color_cell(2, 2, "purple", "🟪", False, False)
map20.fill_color_cell(3, 2, "green", "🟩", False, False)
map20.destination_array=np.append(map20.destination_array,color_square(3, 7, "green", "🟢", True, False))
map20.des.append([3, 7, "green", "🟢"])
map20.destination_array=np.append(map20.destination_array,color_square(3, 2, "purple", "🟣", True, False))
map20.des.append([3, 2, "purple", "🟣"])
map20.fill_color_cell(2, 1, "blue", "🔵", True, False)
map20.des.append([2, 1, "blue", "🔵"])
map20.fill_color_cell(3, 4, "red", "🔴", True, False)
map20.des.append([3, 4, "red", "🔴"])
map20.fill_color_cell(1, 5, "yellow", "🟡", True, False)
map20.des.append([1, 5, "yellow", "🟡"])


start_time = time.time()
map2 = algorithem.DFS(map20)
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

map20 = state(5, 9)
map20.fill_const_row(1, 0, 3, "black", "⬛️")
map20.fill_const_row(0, 3, 6, "black", "⬛️")
map20.fill_const_row(1, 6, 8, "black", "⬛️")
map20.fill_const_row(4, 0, 8, "black", "⬛️")
map20.fill_const_row(3, 3, 3, "black", "⬛️")
map20.fill_const_row(3, 6, 6, "black", "⬛️")
map20.fill_const_col(1, 4, 0, "black", "⬛️")
map20.fill_const_col(1, 4, 8, "black", "⬛️")


map20.fill_color_cell(3, 7, "yellow", "🟨", False, False)
map20.fill_color_cell(1, 4, "red", "🟥", False, False)
map20.fill_color_cell(2, 3, "blue", "🟦", False, False)
map20.fill_color_cell(2, 2, "purple", "🟪", False, False)
map20.fill_color_cell(3, 2, "green", "🟩", False, False)
map20.destination_array=np.append(map20.destination_array,color_square(3, 7, "green", "🟢", True, False))
map20.des.append([3, 7, "green", "🟢"])
map20.destination_array=np.append(map20.destination_array,color_square(3, 2, "purple", "🟣", True, False))
map20.des.append([3, 2, "purple", "🟣"])
map20.fill_color_cell(2, 1, "blue", "🔵", True, False)
map20.des.append([2, 1, "blue", "🔵"])
map20.fill_color_cell(3, 4, "red", "🔴", True, False)
map20.des.append([3, 4, "red", "🔴"])
map20.fill_color_cell(1, 5, "yellow", "🟡", True, False)
map20.des.append([1, 5, "yellow", "🟡"])


start_time = time.time()
map2 = algorithem.DFS_R(map20)
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

map20 = state(5, 9)
map20.fill_const_row(1, 0, 3, "black", "⬛️")
map20.fill_const_row(0, 3, 6, "black", "⬛️")
map20.fill_const_row(1, 6, 8, "black", "⬛️")
map20.fill_const_row(4, 0, 8, "black", "⬛️")
map20.fill_const_row(3, 3, 3, "black", "⬛️")
map20.fill_const_row(3, 6, 6, "black", "⬛️")
map20.fill_const_col(1, 4, 0, "black", "⬛️")
map20.fill_const_col(1, 4, 8, "black", "⬛️")


map20.fill_color_cell(3, 7, "yellow", "🟨", False, False)
map20.fill_color_cell(1, 4, "red", "🟥", False, False)
map20.fill_color_cell(2, 3, "blue", "🟦", False, False)
map20.fill_color_cell(2, 2, "purple", "🟪", False, False)
map20.fill_color_cell(3, 2, "green", "🟩", False, False)
map20.destination_array=np.append(map20.destination_array,color_square(3, 7, "green", "🟢", True, False))
map20.des.append([3, 7, "green", "🟢"])
map20.destination_array=np.append(map20.destination_array,color_square(3, 2, "purple", "🟣", True, False))
map20.des.append([3, 2, "purple", "🟣"])
map20.fill_color_cell(2, 1, "blue", "🔵", True, False)
map20.des.append([2, 1, "blue", "🔵"])
map20.fill_color_cell(3, 4, "red", "🔴", True, False)
map20.des.append([3, 4, "red", "🔴"])
map20.fill_color_cell(1, 5, "yellow", "🟡", True, False)
map20.des.append([1, 5, "yellow", "🟡"])


start_time = time.time()
map2 = algorithem.UCS(map20)
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

map20 = state(5, 9)
map20.fill_const_row(1, 0, 3, "black", "⬛️")
map20.fill_const_row(0, 3, 6, "black", "⬛️")
map20.fill_const_row(1, 6, 8, "black", "⬛️")
map20.fill_const_row(4, 0, 8, "black", "⬛️")
map20.fill_const_row(3, 3, 3, "black", "⬛️")
map20.fill_const_row(3, 6, 6, "black", "⬛️")
map20.fill_const_col(1, 4, 0, "black", "⬛️")
map20.fill_const_col(1, 4, 8, "black", "⬛️")


map20.fill_color_cell(3, 7, "yellow", "🟨", False, False)
map20.fill_color_cell(1, 4, "red", "🟥", False, False)
map20.fill_color_cell(2, 3, "blue", "🟦", False, False)
map20.fill_color_cell(2, 2, "purple", "🟪", False, False)
map20.fill_color_cell(3, 2, "green", "🟩", False, False)
map20.destination_array=np.append(map20.destination_array,color_square(3, 7, "green", "🟢", True, False))
map20.des.append([3, 7, "green", "🟢"])
map20.destination_array=np.append(map20.destination_array,color_square(3, 2, "purple", "🟣", True, False))
map20.des.append([3, 2, "purple", "🟣"])
map20.fill_color_cell(2, 1, "blue", "🔵", True, False)
map20.des.append([2, 1, "blue", "🔵"])
map20.fill_color_cell(3, 4, "red", "🔴", True, False)
map20.des.append([3, 4, "red", "🔴"])
map20.fill_color_cell(1, 5, "yellow", "🟡", True, False)
map20.des.append([1, 5, "yellow", "🟡"])


start_time = time.time()
map2 = algorithem.A_star(map20)
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


logging.info("--------------------SIMPLE_HILL_CLIMBING--------------------")

# tracemalloc.start()

map20 = state(5, 9)
map20.fill_const_row(1, 0, 3, "black", "⬛️")
map20.fill_const_row(0, 3, 6, "black", "⬛️")
map20.fill_const_row(1, 6, 8, "black", "⬛️")
map20.fill_const_row(4, 0, 8, "black", "⬛️")
map20.fill_const_row(3, 3, 3, "black", "⬛️")
map20.fill_const_row(3, 6, 6, "black", "⬛️")
map20.fill_const_col(1, 4, 0, "black", "⬛️")
map20.fill_const_col(1, 4, 8, "black", "⬛️")


map20.fill_color_cell(3, 7, "yellow", "🟨", False, False)
map20.fill_color_cell(1, 4, "red", "🟥", False, False)
map20.fill_color_cell(2, 3, "blue", "🟦", False, False)
map20.fill_color_cell(2, 2, "purple", "🟪", False, False)
map20.fill_color_cell(3, 2, "green", "🟩", False, False)
map20.destination_array=np.append(map20.destination_array,color_square(3, 7, "green", "🟢", True, False))
map20.des.append([3, 7, "green", "🟢"])
map20.destination_array=np.append(map20.destination_array,color_square(3, 2, "purple", "🟣", True, False))
map20.des.append([3, 2, "purple", "🟣"])
map20.fill_color_cell(2, 1, "blue", "🔵", True, False)
map20.des.append([2, 1, "blue", "🔵"])
map20.fill_color_cell(3, 4, "red", "🔴", True, False)
map20.des.append([3, 4, "red", "🔴"])
map20.fill_color_cell(1, 5, "yellow", "🟡", True, False)
map20.des.append([1, 5, "yellow", "🟡"])


start_time = time.time()
map2 = algorithem.simple_hill_climbing(map20)
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

map20 = state(5, 9)
map20.fill_const_row(1, 0, 3, "black", "⬛️")
map20.fill_const_row(0, 3, 6, "black", "⬛️")
map20.fill_const_row(1, 6, 8, "black", "⬛️")
map20.fill_const_row(4, 0, 8, "black", "⬛️")
map20.fill_const_row(3, 3, 3, "black", "⬛️")
map20.fill_const_row(3, 6, 6, "black", "⬛️")
map20.fill_const_col(1, 4, 0, "black", "⬛️")
map20.fill_const_col(1, 4, 8, "black", "⬛️")


map20.fill_color_cell(3, 7, "yellow", "🟨", False, False)
map20.fill_color_cell(1, 4, "red", "🟥", False, False)
map20.fill_color_cell(2, 3, "blue", "🟦", False, False)
map20.fill_color_cell(2, 2, "purple", "🟪", False, False)
map20.fill_color_cell(3, 2, "green", "🟩", False, False)
map20.destination_array=np.append(map20.destination_array,color_square(3, 7, "green", "🟢", True, False))
map20.des.append([3, 7, "green", "🟢"])
map20.destination_array=np.append(map20.destination_array,color_square(3, 2, "purple", "🟣", True, False))
map20.des.append([3, 2, "purple", "🟣"])
map20.fill_color_cell(2, 1, "blue", "🔵", True, False)
map20.des.append([2, 1, "blue", "🔵"])
map20.fill_color_cell(3, 4, "red", "🔴", True, False)
map20.des.append([3, 4, "red", "🔴"])
map20.fill_color_cell(1, 5, "yellow", "🟡", True, False)
map20.des.append([1, 5, "yellow", "🟡"])


start_time = time.time()
map2 = algorithem.steepest_hill_climbing(map20)
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