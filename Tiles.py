from collections import deque
from typing import List

goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def pretty_print(state: List[int]):
    print("+---+---+---+")
    for i in range(0, 9, 3):
        print("| {} | {} | {} |".format(*state[i : i + 3]))
        print("+---+---+---+")


def print_state(state: List[int]) -> None:
    for i in state:
        print(i, end=" ")
    print()


def swap(arr: List[int], i: int, j: int):
    l = arr.copy()
    l[i] = arr[j]
    l[j] = arr[i]
    return l


def find_blank_index(arr: List[int]) -> int:
    for i in range(len(arr)):
        if arr[i] == 0:
            return i

    return -1


def up(arr: List[int]) -> List[int]:
    l = []
    zero = find_blank_index(arr)
    new_index = zero - 3
    if 0 <= new_index <= 8:
        l = swap(arr, zero, zero - 3)
    return l


def down(arr: List[int]) -> List[int]:
    l = []
    zero = find_blank_index(arr)
    new_index = zero + 3
    if 0 <= new_index <= 8:
        l = swap(arr, zero, zero + 3)
    return l


def right(arr: List[int]) -> List[int]:
    l = []
    zero = find_blank_index(arr)
    if zero % 3 != 2:
        new_index = zero + 1
        if 0 <= new_index <= 8:
            l = swap(arr, zero, zero + 1)
    return l


def left(arr: List[int]) -> List[int]:
    l = []
    zero = find_blank_index(arr)
    if zero % 3 != 0:
        new_index = zero - 1
        if 0 <= new_index <= 8:
            l = swap(arr, zero, zero - 1)
    return l


def is_goal(state: List[int]) -> bool:
    return state == goal_state


def expand(state) -> List[int]:
    children = []
    for move in (left, right, up, down):
        child = move(state)
        if child:
            children.append(child)

    return children


def bfs(initial_state: List[int]) -> List[int]:
    node = initial_state
    expanded = 0
    if is_goal(node):
        return node

    frontier = deque([node])
    reached = set()
    reached.add(tuple(node))

    while frontier:
        node = frontier.popleft()
        expanded += 1
        children = expand(node)
        for child in children:
            state = child
            if is_goal(state):
                print(expanded)
                return child
            if tuple(state) not in reached:
                reached.add(tuple(state))
                frontier.append(state)
    print(expanded)
    return []


def main():
    initial_state = [1, 4, 0, 5, 8, 2, 3, 6, 7]
    state = bfs(initial_state)

    pretty_print(state)


if __name__ == "__main__":
    main()
