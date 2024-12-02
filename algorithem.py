import numpy as np
from state import state
import queue


def heuristic(state):
    cost = 0

    for i in range(state.size):
        for j in range(state.size):
            cell = state.my_array[i][j]

            if "final" in cell and cell["final"] == True:
                goal_color = cell["color"]

                for x in range(state.size):
                    for y in range(state.size):
                        piece = state.my_array[x][y]
                        if "color" in piece and piece["color"] == goal_color:

                            cost += abs(i - x) + abs(j - y)
                            break
    return cost


def BFS(start_state):
    my_queue = queue.Queue()
    my_queue.put(start_state)
    visited_array = np.array([])

    while my_queue.empty() == False:

        current = my_queue.get()
        if current.is_finite() == True:
            path = np.array([current])
            while current.parent != None:
                path = np.append(path, current.parent)
                current = current.parent
            path = np.flip(path)
            return {
                "path": path,
                "path_len": len(path),
                "visited_len": len(visited_array),
            }
        else:
            visited = False
            for item in visited_array:
                if state.equals(item, current) == True:
                    visited = True
                    break
                continue
            if visited == False:
                visited_array = np.append(visited_array, current)
                next_states = state.next_state(current)
                for item1 in next_states:
                    item1.parent = current
                    my_queue.put(item1)
    return {
        "path": [],
        "path_len": [],
        "visited_len": [],
    }


def DFS(start_state):
    my_lifo_queue = queue.LifoQueue()
    my_lifo_queue.put(start_state)
    visited_array = np.array([])

    while my_lifo_queue.empty() == False:

        current = my_lifo_queue.get()
        if current.is_finite() == True:
            path = np.array([current])
            while current.parent != None:
                path = np.append(path, current.parent)
                current = current.parent
            path = np.flip(path)

            return {
                "path": path,
                "path_len": len(path),
                "visited_len": len(visited_array),
            }
        else:
            visited = False
            for item in visited_array:
                if state.equals(item, current) == True:
                    visited = True
                    break
                continue
            if visited == False:
                visited_array = np.append(visited_array, current)
                next_states = state.next_state(current)
                for item1 in next_states:
                    item1.parent = current
                    my_lifo_queue.put(item1)
    return {
        "path": [],
        "path_len": [],
        "visited_len": [],
    }


def DFS_R(start_state, visited_array=None, my_lifo_queue=None):
    if visited_array is None:
        visited_array = np.array([])
    if my_lifo_queue is None:
        my_lifo_queue = queue.LifoQueue()
        my_lifo_queue.put(start_state)

    if my_lifo_queue.empty() == False:

        current = my_lifo_queue.get()
        if current.is_finite() == True:
            path = np.array([current])
            while current.parent != None:
                path = np.append(path, current.parent)
                current = current.parent
            path = np.flip(path)

            return {
                "path": path,
                "path_len": len(path),
                "visited_len": len(visited_array),
            }

        else:
            visited = False
            for item in visited_array:
                if state.equals(item, current) == True:
                    visited = True
                    break
                continue
            if visited == False:
                visited_array = np.append(visited_array, current)
                next_states = state.next_state(current)
                for item1 in next_states:
                    item1.parent = current
                    my_lifo_queue.put(item1)
            return DFS_R(my_lifo_queue.queue[-1], visited_array, my_lifo_queue)
    return {
        "path": [],
        "path_len": [],
        "visited_len": [],
    }


def UCS(start_state):

    priority_queue = queue.PriorityQueue()

    priority_queue.put((start_state.edge, start_state))
    visited_array = np.array([])

    while not priority_queue.empty():

        current_cost, current = priority_queue.get()

        if current.is_finite():
            path = np.array([current])
            while current.parent is not None:
                path = np.append(path, current.parent)
                current = current.parent
            path = np.flip(path)
            return {
                "path": path,
                "path_len": len(path),
                "visited_len": len(visited_array),
            }

        visited = False
        for item in visited_array:
            if state.equals(item, current) and item.edge == current.edge:
                visited = True
                break

        if not visited:

            visited_array = np.append(visited_array, current)

            next_states = state.next_state(current)
            if current.parent == None:
                for item in next_states:

                    item.parent = current

                    item.edge = current_cost + 1

                    priority_queue.put((item.edge, item))
            else:
                for item in next_states:
                    if state.equals(item, current.parent) == False:
                        item.parent = current

                        item.edge = current_cost + 1

                        priority_queue.put((item.edge, item))

    return {
        "path": [],
        "path_len": [],
        "visited_len": [],
    }


def A_star(start_state):
    priority_queue = queue.PriorityQueue()
    start_cost = heuristic(start_state)
    priority_queue.put((start_cost, 0, start_state))
    visited_array = np.array([])

    while not priority_queue.empty():
        _, current_cost, current = priority_queue.get()

        if current.is_finite():
            path = np.array([current])
            while current.parent is not None:
                path = np.append(path, current.parent)
                current = current.parent
            path = np.flip(path)
            return {
                "path": path,
                "path_len": len(path),
                "visited_len": len(visited_array),
            }

        visited = False
        for item in visited_array:
            if state.equals(item, current):
                visited = True
                break

        if not visited:
            visited_array = np.append(visited_array, current)

            next_states = state.next_state(current)
            for item in next_states:
                if current.parent is None or not state.equals(item, current.parent):
                    item.parent = current
                    g_cost = current_cost + 1
                    f_cost = g_cost + heuristic(item)
                    priority_queue.put((f_cost, g_cost, item))

    return {
        "path": [],
        "path_len": [],
        "visited_len": len(visited_array),
    }


def simple_hill_climbing(start_state):
    current = start_state
    visited_array = np.array([])

    while not current.is_finite():
        visited_array = np.append(visited_array, current)
        next_states = state.next_state(current)

        if len(next_states) == 0:
            break

        best_state = None

        if heuristic(next_states[0]) < heuristic(current):
            best_state = next_states[0]

        if best_state is None:
            break

        best_state.parent = current
        current = best_state

    if current.is_finite():
        path = np.array([current])
        while current.parent is not None:
            path = np.append(path, current.parent)
            current = current.parent
        path = np.flip(path)
        return {
            "path": path,
            "path_len": len(path),
            "visited_len": len(visited_array),
        }

    return {
        "path": [],
        "path_len": 0,
        "visited_len": visited_array,
    }


def steepest_hill_climbing(start_state):
    current = start_state
    visited_array = np.array([])

    while not current.is_finite():
        visited_array = np.append(visited_array, current)
        next_states = state.next_state(current)

        if len(next_states) == 0:
            break

        best_next_state = min(next_states, key=heuristic)

        if heuristic(best_next_state) >= heuristic(current):
            break

        best_next_state.parent = current
        current = best_next_state

    if current.is_finite():
        path = np.array([current])
        while current.parent is not None:
            path = np.append(path, current.parent)
            current = current.parent
        path = np.flip(path)
        return {
            "path": path,
            "path_len": len(path),
            "visited_len": len(visited_array),
        }

    return {
        "path": [],
        "path_len": 0,
        "visited_len": visited_array,
    }
