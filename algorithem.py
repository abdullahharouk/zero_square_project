import numpy as np
from state import state
import queue


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


my_lifo_queue = queue.LifoQueue()
visited_array = np.array([])


def DFS_R(start_state):

    my_lifo_queue.put(start_state)

    current = start_state
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
        next = my_lifo_queue.get()
        DFS_R(next)
