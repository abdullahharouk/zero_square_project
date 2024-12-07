from state import state
import algorithem
from state import state
import logging
import time
# import tracemalloc

logging.basicConfig(
    filename="level_10.log",
    level=logging.INFO,
    format="%(message)s",
)

logging.info("--------------------BFS--------------------")

# tracemalloc.start()

map10 = state(8, 12)
map10.fill_const_row(0, 2, 9, "black", "⬛️")
map10.fill_const_row(7, 0, 11, "black", "⬛️")
map10.fill_const_row(1, 1, 2, "black", "⬛️")
map10.fill_const_row(2, 0, 1, "black", "⬛️")
map10.fill_const_row(1, 9, 10, "black", "⬛️")
map10.fill_const_row(2, 10, 11, "black", "⬛️")
map10.fill_const_col(2, 7, 0, "black", "⬛️")
map10.fill_const_col(2, 7, 11, "black", "⬛️")
map10.fill_const_col(5, 6, 4, "black", "⬛️")
map10.fill_const_col(4, 5, 5, "black", "⬛️")
map10.fill_const_col(3, 4, 8, "black", "⬛️")
map10.fill_const_col(4, 5, 9, "black", "⬛️")


map10.fill_const_col(2, 2, 4, "black", "⬛️")
map10.fill_const_col(3, 3, 3, "black", "⬛️")
map10.fill_const_col(5, 5, 2, "black", "⬛️")
map10.fill_const_col(2, 2, 7, "black", "⬛️")


map10.fill_color_cell(5, 10, "blue", "🟦", False, False)
map10.fill_color_cell(5, 1, "red", "🟥", False, False)
map10.fill_color_cell(2, 6, "blue", "🔵", True, False)
map10.des.append([2, 6, "blue", "🔵"])
map10.fill_color_cell(3, 5, "red", "🔴", True, False)

map10.des.append([3, 5, "red", "🔴"])


start_time = time.time()
map2 = algorithem.BFS(map10)
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

map10 = state(8, 12)
map10.fill_const_row(0, 2, 9, "black", "⬛️")
map10.fill_const_row(7, 0, 11, "black", "⬛️")
map10.fill_const_row(1, 1, 2, "black", "⬛️")
map10.fill_const_row(2, 0, 1, "black", "⬛️")
map10.fill_const_row(1, 9, 10, "black", "⬛️")
map10.fill_const_row(2, 10, 11, "black", "⬛️")
map10.fill_const_col(2, 7, 0, "black", "⬛️")
map10.fill_const_col(2, 7, 11, "black", "⬛️")
map10.fill_const_col(5, 6, 4, "black", "⬛️")
map10.fill_const_col(4, 5, 5, "black", "⬛️")
map10.fill_const_col(3, 4, 8, "black", "⬛️")
map10.fill_const_col(4, 5, 9, "black", "⬛️")


map10.fill_const_col(2, 2, 4, "black", "⬛️")
map10.fill_const_col(3, 3, 3, "black", "⬛️")
map10.fill_const_col(5, 5, 2, "black", "⬛️")
map10.fill_const_col(2, 2, 7, "black", "⬛️")


map10.fill_color_cell(5, 10, "blue", "🟦", False, False)
map10.fill_color_cell(5, 1, "red", "🟥", False, False)
map10.fill_color_cell(2, 6, "blue", "🔵", True, False)
map10.des.append([2, 6, "blue", "🔵"])
map10.fill_color_cell(3, 5, "red", "🔴", True, False)

map10.des.append([3, 5, "red", "🔴"])

start_time = time.time()
map2 = algorithem.DFS(map10)
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

map10 = state(8, 12)
map10.fill_const_row(0, 2, 9, "black", "⬛️")
map10.fill_const_row(7, 0, 11, "black", "⬛️")
map10.fill_const_row(1, 1, 2, "black", "⬛️")
map10.fill_const_row(2, 0, 1, "black", "⬛️")
map10.fill_const_row(1, 9, 10, "black", "⬛️")
map10.fill_const_row(2, 10, 11, "black", "⬛️")
map10.fill_const_col(2, 7, 0, "black", "⬛️")
map10.fill_const_col(2, 7, 11, "black", "⬛️")
map10.fill_const_col(5, 6, 4, "black", "⬛️")
map10.fill_const_col(4, 5, 5, "black", "⬛️")
map10.fill_const_col(3, 4, 8, "black", "⬛️")
map10.fill_const_col(4, 5, 9, "black", "⬛️")


map10.fill_const_col(2, 2, 4, "black", "⬛️")
map10.fill_const_col(3, 3, 3, "black", "⬛️")
map10.fill_const_col(5, 5, 2, "black", "⬛️")
map10.fill_const_col(2, 2, 7, "black", "⬛️")


map10.fill_color_cell(5, 10, "blue", "🟦", False, False)
map10.fill_color_cell(5, 1, "red", "🟥", False, False)
map10.fill_color_cell(2, 6, "blue", "🔵", True, False)
map10.des.append([2, 6, "blue", "🔵"])
map10.fill_color_cell(3, 5, "red", "🔴", True, False)

map10.des.append([3, 5, "red", "🔴"])


start_time = time.time()
map2 = algorithem.DFS_R(map10)
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


map10 = state(8, 12)
map10.fill_const_row(0, 2, 9, "black", "⬛️")
map10.fill_const_row(7, 0, 11, "black", "⬛️")
map10.fill_const_row(1, 1, 2, "black", "⬛️")
map10.fill_const_row(2, 0, 1, "black", "⬛️")
map10.fill_const_row(1, 9, 10, "black", "⬛️")
map10.fill_const_row(2, 10, 11, "black", "⬛️")
map10.fill_const_col(2, 7, 0, "black", "⬛️")
map10.fill_const_col(2, 7, 11, "black", "⬛️")
map10.fill_const_col(5, 6, 4, "black", "⬛️")
map10.fill_const_col(4, 5, 5, "black", "⬛️")
map10.fill_const_col(3, 4, 8, "black", "⬛️")
map10.fill_const_col(4, 5, 9, "black", "⬛️")


map10.fill_const_col(2, 2, 4, "black", "⬛️")
map10.fill_const_col(3, 3, 3, "black", "⬛️")
map10.fill_const_col(5, 5, 2, "black", "⬛️")
map10.fill_const_col(2, 2, 7, "black", "⬛️")


map10.fill_color_cell(5, 10, "blue", "🟦", False, False)
map10.fill_color_cell(5, 1, "red", "🟥", False, False)
map10.fill_color_cell(2, 6, "blue", "🔵", True, False)
map10.des.append([2, 6, "blue", "🔵"])
map10.fill_color_cell(3, 5, "red", "🔴", True, False)

map10.des.append([3, 5, "red", "🔴"])


start_time = time.time()
map2 = algorithem.UCS(map10)
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

map10 = state(8, 12)
map10.fill_const_row(0, 2, 9, "black", "⬛️")
map10.fill_const_row(7, 0, 11, "black", "⬛️")
map10.fill_const_row(1, 1, 2, "black", "⬛️")
map10.fill_const_row(2, 0, 1, "black", "⬛️")
map10.fill_const_row(1, 9, 10, "black", "⬛️")
map10.fill_const_row(2, 10, 11, "black", "⬛️")
map10.fill_const_col(2, 7, 0, "black", "⬛️")
map10.fill_const_col(2, 7, 11, "black", "⬛️")
map10.fill_const_col(5, 6, 4, "black", "⬛️")
map10.fill_const_col(4, 5, 5, "black", "⬛️")
map10.fill_const_col(3, 4, 8, "black", "⬛️")
map10.fill_const_col(4, 5, 9, "black", "⬛️")


map10.fill_const_col(2, 2, 4, "black", "⬛️")
map10.fill_const_col(3, 3, 3, "black", "⬛️")
map10.fill_const_col(5, 5, 2, "black", "⬛️")
map10.fill_const_col(2, 2, 7, "black", "⬛️")


map10.fill_color_cell(5, 10, "blue", "🟦", False, False)
map10.fill_color_cell(5, 1, "red", "🟥", False, False)
map10.fill_color_cell(2, 6, "blue", "🔵", True, False)
map10.des.append([2, 6, "blue", "🔵"])
map10.fill_color_cell(3, 5, "red", "🔴", True, False)

map10.des.append([3, 5, "red", "🔴"])


start_time = time.time()
map2 = algorithem.A_star(map10)
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


map10 = state(8, 12)
map10.fill_const_row(0, 2, 9, "black", "⬛️")
map10.fill_const_row(7, 0, 11, "black", "⬛️")
map10.fill_const_row(1, 1, 2, "black", "⬛️")
map10.fill_const_row(2, 0, 1, "black", "⬛️")
map10.fill_const_row(1, 9, 10, "black", "⬛️")
map10.fill_const_row(2, 10, 11, "black", "⬛️")
map10.fill_const_col(2, 7, 0, "black", "⬛️")
map10.fill_const_col(2, 7, 11, "black", "⬛️")
map10.fill_const_col(5, 6, 4, "black", "⬛️")
map10.fill_const_col(4, 5, 5, "black", "⬛️")
map10.fill_const_col(3, 4, 8, "black", "⬛️")
map10.fill_const_col(4, 5, 9, "black", "⬛️")


map10.fill_const_col(2, 2, 4, "black", "⬛️")
map10.fill_const_col(3, 3, 3, "black", "⬛️")
map10.fill_const_col(5, 5, 2, "black", "⬛️")
map10.fill_const_col(2, 2, 7, "black", "⬛️")


map10.fill_color_cell(5, 10, "blue", "🟦", False, False)
map10.fill_color_cell(5, 1, "red", "🟥", False, False)
map10.fill_color_cell(2, 6, "blue", "🔵", True, False)
map10.des.append([2, 6, "blue", "🔵"])
map10.fill_color_cell(3, 5, "red", "🔴", True, False)

map10.des.append([3, 5, "red", "🔴"])


start_time = time.time()
map2 = algorithem.simple_hill_climbing(map10)
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

map10 = state(8, 12)
map10.fill_const_row(0, 2, 9, "black", "⬛️")
map10.fill_const_row(7, 0, 11, "black", "⬛️")
map10.fill_const_row(1, 1, 2, "black", "⬛️")
map10.fill_const_row(2, 0, 1, "black", "⬛️")
map10.fill_const_row(1, 9, 10, "black", "⬛️")
map10.fill_const_row(2, 10, 11, "black", "⬛️")
map10.fill_const_col(2, 7, 0, "black", "⬛️")
map10.fill_const_col(2, 7, 11, "black", "⬛️")
map10.fill_const_col(5, 6, 4, "black", "⬛️")
map10.fill_const_col(4, 5, 5, "black", "⬛️")
map10.fill_const_col(3, 4, 8, "black", "⬛️")
map10.fill_const_col(4, 5, 9, "black", "⬛️")


map10.fill_const_col(2, 2, 4, "black", "⬛️")
map10.fill_const_col(3, 3, 3, "black", "⬛️")
map10.fill_const_col(5, 5, 2, "black", "⬛️")
map10.fill_const_col(2, 2, 7, "black", "⬛️")


map10.fill_color_cell(5, 10, "blue", "🟦", False, False)
map10.fill_color_cell(5, 1, "red", "🟥", False, False)
map10.fill_color_cell(2, 6, "blue", "🔵", True, False)
map10.des.append([2, 6, "blue", "🔵"])
map10.fill_color_cell(3, 5, "red", "🔴", True, False)

map10.des.append([3, 5, "red", "🔴"])


start_time = time.time()
map2 = algorithem.steepest_hill_climbing(map10)
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
