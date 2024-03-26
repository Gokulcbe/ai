import heapq

class PuzzleState:
    def __init__(self, puzzle, parent=None):
        self.puzzle = puzzle
        self.parent = parent
        self.cost = 0
        self.heuristic = 0
        self.depth = 0

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        return hash(str(self.puzzle))

    def goal_test(self):
        return self.puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def generate_children(self):
        children = []
        zero_index = self.puzzle.index(0)
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Right, Left, Down, Up

        for dx, dy in moves:
            new_x, new_y = zero_index // 3 + dx, zero_index % 3 + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_puzzle = self.puzzle[:]
                new_zero_index = new_x * 3 + new_y
                new_puzzle[zero_index], new_puzzle[new_zero_index] = new_puzzle[new_zero_index], new_puzzle[zero_index]
                new_state = PuzzleState(new_puzzle, self)
                children.append(new_state)

        return children

def manhattan_distance(state):
    distance = 0
    for i in range(1, 9):
        current_x, current_y = state.puzzle.index(i) // 3, state.puzzle.index(i) % 3
        goal_x, goal_y = (i - 1) // 3, (i - 1) % 3
        distance += abs(current_x - goal_x) + abs(current_y - goal_y)
    return distance

def best_first_search(initial_state):
    frontier = []
    heapq.heappush(frontier, initial_state)

    explored = set()
    while frontier:
        current_state = heapq.heappop(frontier)

        if current_state.goal_test():
            return current_state

        explored.add(current_state)

        for child in current_state.generate_children():
            if child not in explored:
                child.cost = current_state.cost + 1
                child.heuristic = manhattan_distance(child)
                heapq.heappush(frontier, child)

    return None

def print_solution(solution):
    path = []
    current_state = solution
    while current_state:
        path.append(current_state.puzzle)
        current_state = current_state.parent
    path.reverse()
    for i, state in enumerate(path):
        print(f"Move {i}:")
        print_puzzle(state)
        print()

def print_puzzle(puzzle):
    for i in range(0, 9, 3):
        print(puzzle[i:i+3])

if __name__ == "__main__":
    initial_puzzle = [1, 2, 3, 0, 4, 5, 6, 7, 8]  # Initial state of the puzzle
    initial_state = PuzzleState(initial_puzzle)

    solution = best_first_search(initial_state)

    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found.")
