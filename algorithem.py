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
            if state.equals(item, current) and item.edge==current.edge:
                visited = True
                break

        if not visited:
           
            visited_array = np.append(visited_array, current)
          
            next_states = state.next_state(current)

            for item in next_states:
             
                item.parent = current
              
                item.edge = current_cost + 1  
              
                priority_queue.put((item.edge, item))

    return {
        "path": [],
        "path_len": [],
        "visited_len": [],
    }
