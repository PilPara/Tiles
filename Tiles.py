from collections import deque
from typing import Deque, List
import sys

target_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def print_state(state: List[int]) -> None:
    print("+---+---+---+")
    for i in range(0, 9, 3):
        row = [" " if x == 0 else x for x in state[i : i + 3]]
        print("| {} | {} | {} |".format(*row))
        print("+---+---+---+")


def left(state: List[int]) -> List[int]:
    result = state.copy()
    zero_index = state.index(0)
    if zero_index % 3 == 0:
        return result

    if 0 <= zero_index - 1 <= 8:
        temp = state[zero_index]
        result[zero_index] = result[zero_index - 1]
        result[zero_index - 1] = temp

    return result


def right(state: List[int]) -> List[int]:
    result = state.copy()
    zero_index = state.index(0)
    if zero_index % 3 == 2:
        return result

    if 0 <= zero_index + 1 <= 8:
        temp = state[zero_index]
        result[zero_index] = result[zero_index + 1]
        result[zero_index + 1] = temp

    return result


def up(state: List[int]) -> List[int]:
    result = state.copy()
    zero_index = state.index(0)
    if 0 <= zero_index - 3 <= 8:
        temp = result[zero_index]
        result[zero_index] = result[zero_index - 3]
        result[zero_index - 3] = temp

    return result


def down(state: List[int]) -> List[int]:
    result = state.copy()
    zero_index = state.index(0)
    if 0 <= zero_index + 3 <= 8:
        temp = result[zero_index]
        result[zero_index] = result[zero_index + 3]
        result[zero_index + 3] = temp

    return result


def is_goal(state: List[int]) -> bool:
    return state == target_state


def expand(state: List[int]) -> List[List[int]]:
    children = []
    for move in (left, right, up, down):
        new_state = move(state)
        if new_state is not None:
            children.append(new_state)
    return children


def main():
    if len(sys.argv) != 10:
        print("usage: python Tiles.py <9 digits>")
        sys.exit(1)

    initial_state = [int(x) for x in sys.argv[1:]]

    # NOTE: Action order - Left Right Up Down

    print_state(initial_state)
    node = initial_state
    if is_goal(node):
        print_state(node)
        exit(0)

    frontier = deque([node])
    reached = set()
    reached.add(tuple(initial_state))
    expanded = 0
    parents = []

    while frontier:
        node = frontier.popleft()
        expanded += 1
        children = expand(node)
        for child in children:
            if is_goal(child):
                print_state(child)
                print(expanded)
                exit(0)
            if tuple(child) not in reached:
                reached.add(tuple(child))
                frontier.append(child)


if __name__ == "__main__":
    main()
