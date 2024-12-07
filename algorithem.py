from state import state

from collections import deque
from heapq import heappush, heappop
import sys

sys.setrecursionlimit(2000000)


def heuristic(state):
    cost = 0

    for cell in state.des:
        if cell[3] == "🔶":
            for x in range(state.rows):
                for y in range(state.cols):
                    if (
                        state.my_array[x][y]["color"] != "white"
                        and state.my_array[x][y]["color"] != "black"
                    ):
                        if state.my_array[x][y]["final"] == False:
                            check = False
                            for cell1 in state.des:
                                if (
                                    state.my_array[x][y]["color"] == cell1[2]
                                    and cell1[3] != "🔶"
                                ):
                                    check = True
                                    break
                            if not check:
                                cost += abs(cell[0] - x) + abs(cell[1] - y)

        else:
            goal_color = cell[2]

            for x in range(state.rows):
                for y in range(state.cols):
                    piece = state.my_array[x][y]
                    if "color" in piece and piece["color"] == goal_color:

                        cost += abs(cell[0] - x) + abs(cell[1] - y)
                        break
    return cost


def BFS(start_state):
    my_queue = deque([start_state])
    visited_set = set()

    while my_queue:
        print(len(visited_set))
        current = my_queue.popleft()

        if current.is_finite():
            cost = current.edge
            path = [current]
            while current.parent:
                path.append(current.parent)
                current = current.parent
            path.reverse()
            return {
                "path": path,
                "path_len": len(path),
                "visited_len": len(visited_set),
                "cost": cost,
            }

        current_h = current.get_hash()
        if current_h not in visited_set:
            visited_set.add(current_h)
            for item in state.next_state(current):
                if (
                    current.parent is None
                    or item.get_hash() != current.parent.get_hash()
                ) and not item.game_over:
                    item.parent = current
                    my_queue.append(item)

    return {
        "path": [],
        "path_len": 0,
        "visited_len": len(visited_set),
    }


def DFS(start_state, max_depth=27):
    my_stack = deque([(start_state, 0)])
    visited_set = set()

    while my_stack:
        print(len(visited_set))
        current, depth = my_stack.pop()
        if depth > max_depth:
            continue

        if current.is_finite():
            path = [current]
            cost = current.edge
            while current.parent:
                path.append(current.parent)
                current = current.parent
            path.reverse()
            return {
                "path": path,
                "path_len": len(path),
                "visited_len": len(visited_set),
                "cost": cost,
            }

        current_h = current.get_hash()
        if current_h not in visited_set:
            visited_set.add(current_h)
            next_states = state.next_state(current)

            for item in next_states:
                if (
                    current.parent is None
                    or item.get_hash() != current.parent.get_hash()
                ) and not item.game_over:
                    item.parent = current
                    my_stack.append((item, depth + 1))  # زيادة العمق

    return {
        "path": [],
        "path_len": 0,
        "visited_len": len(visited_set),
    }


# ,max_depth=22  if depth>max_depth:
#         DFS_R(my_stack[-1], visited_set, my_stack)
#       else:


def DFS_R(start_state, visited_set=None, my_stack=None, max_depth=27):
    if visited_set is None:
        visited_set = set()
    if my_stack is None:
        my_stack = deque([(start_state, 0)])

    if my_stack:
        print(len(visited_set))
        current, depth = my_stack.pop()
        if depth > max_depth:
            return DFS_R(my_stack[-1], visited_set, my_stack)
        else:
            if current.is_finite():
                cost = current.edge
                path = [current]
                while current.parent:

                    path.append(current.parent)
                    current = current.parent
                path.reverse()
                return {
                    "path": path,
                    "path_len": len(path),
                    "visited_len": len(visited_set),
                    "cost": cost,
                }

            current_h = current.get_hash()
            if current_h not in visited_set:
                visited_set.add(current_h)
                next_states = state.next_state(current)

                for item in next_states:
                    if (
                        current.parent is None
                        or item.get_hash() != current.parent.get_hash()
                    ) and not item.game_over:
                        item.parent = current
                        my_stack.append((item, depth + 1))

            return DFS_R(my_stack[-1], visited_set, my_stack)

    return {
        "path": [],
        "path_len": 0,
        "visited_len": len(visited_set),
    }


def UCS(start_state):

    priority_queue = []
    heappush(priority_queue, (start_state.edge, start_state))

    visited_set = set()

    while priority_queue:
        print(len(visited_set))
        current_cost, current = heappop(priority_queue)

        if current.is_finite():

            path = [current]
            cost = current_cost
            while current.parent:
                path.append(current.parent)
                current = current.parent
            path.reverse()
            return {
                "path": path,
                "path_len": len(path),
                "visited_len": len(visited_set),
                "cost": cost,
            }

        current_h = current.get_hash()
        if current_h not in visited_set:
            visited_set.add(current_h)

            next_states = state.next_state(current)
            for item in next_states:
                if (
                    current.parent is None
                    or item.get_hash() != current.parent.get_hash()
                ) and not item.game_over:
                    item.parent = current

                    heappush(priority_queue, (item.edge, item))

    return {"path": [], "path_len": 0, "visited_len": len(visited_set), "cost": 0}


def A_star(start_state):
    priority_queue = []
    start_cost = heuristic(start_state)
    heappush(priority_queue, (start_cost, 0, start_state))
    visited_set = set()

    while priority_queue:
        _, current_cost, current = heappop(priority_queue)
        print(len(visited_set))

        if current.is_finite():

            path = [current]
            cost = current_cost
            while current.parent:
                path.append(current.parent)
                current = current.parent
            path.reverse()
            return {
                "path": path,
                "path_len": len(path),
                "visited_len": len(visited_set),
                "cost": cost,
            }

        current_h = current.get_hash()
        if current_h not in visited_set:
            visited_set.add(current_h)

            next_states = state.next_state(current)
            for item in next_states:
                if (
                    current.parent is None
                    or item.get_hash() != current.parent.get_hash()
                ):
                    item.parent = current
                    g_cost = item.edge
                    f_cost = g_cost + heuristic(item)
                    heappush(priority_queue, (f_cost, g_cost, item))

    return {
        "path": [],
        "path_len": 0,
        "visited_len": len(visited_set),
        "cost": 0,
    }


def A_star_advance(start_state):
    priority_queue = []
    start_cost = heuristic(start_state)
    heappush(priority_queue, (start_cost, 0, start_state))
    visited_set = set()

    while priority_queue:
        _, current_cost, current = heappop(priority_queue)
        print(len(visited_set))

        if current.is_finite():

            path = [current]
            cost = current_cost
            while current.parent:
                path.append(current.parent)
                current = current.parent
            path.reverse()
            return {
                "path": path,
                "path_len": len(path),
                "visited_len": len(visited_set),
                "cost": cost,
            }

        current_h = current.get_hash()
        if current_h not in visited_set:
            visited_set.add(current_h)

            next_states = state.next_state(current)
            for item in next_states:
                if (
                    current.parent is None
                    or item.get_hash() != current.parent.get_hash()
                ) and not item.game_over:
                    item.parent = current
                    g_cost = item.edge
                    f_cost = g_cost + heuristic(item)

                    heappush(priority_queue, (f_cost, g_cost, item))

    return {
        "path": [],
        "path_len": 0,
        "visited_len": len(visited_set),
        "cost": 0,
    }


def simple_hill_climbing(start_state):
    current = start_state
    visited_set = set()

    while not current.is_finite():

        visited_set.add(current)
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
        path = []
        while current is not None:
            path.append(current)
            current = current.parent
        path.reverse()
        return {
            "path": path,
            "path_len": len(path),
            "visited_len": len(visited_set),
        }

    return {
        "path": [],
        "path_len": 0,
        "visited_len": len(visited_set),
    }


def steepest_hill_climbing(start_state):
    current = start_state
    visited_set = set()

    while not current.is_finite():
        visited_set.add(current)
        next_states = state.next_state(current)

        if len(next_states) == 0:
            break

        best_next_state = min(next_states, key=heuristic)

        if heuristic(best_next_state) >= heuristic(current):
            break

        best_next_state.parent = current
        current = best_next_state

    if current.is_finite():
        path = []
        while current is not None:
            path.append(current)
            current = current.parent
        path.reverse()
        return {
            "path": path,
            "path_len": len(path),
            "visited_len": len(visited_set),
        }

    return {
        "path": [],
        "path_len": 0,
        "visited_len": len(visited_set),
    }
