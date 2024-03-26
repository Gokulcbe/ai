from queue import PriorityQueue

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class PuzzleState:
    def __init__(self, puzzle, parent=None, move="Initial"):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.h = self.calculate_heuristic()

    def __lt__(self, other):
        return self.h < other.h

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        return hash(str(self.puzzle))

    def __str__(self):
        return f"Move: {self.move}\n{self.print_puzzle()}"

    def print_puzzle(self):
        res = ""
        for row in self.puzzle:
            res += " ".join(map(str, row)) + "\n"
        return res

    def calculate_heuristic(self):
        h = 0
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] != goal_state[i][j] and self.puzzle[i][j] != 0:
                    h += 1
        return h

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] == 0:
                    return i, j

    def get_possible_moves(self):
        i, j = self.get_blank_position()
        possible_moves = []
        if i > 0:
            possible_moves.append((-1, 0))
        if i < 2:
            possible_moves.append((1, 0))
        if j > 0:
            possible_moves.append((0, -1))
        if j < 2:
            possible_moves.append((0, 1))
        return possible_moves

    def make_move(self, move):
        new_puzzle = [row[:] for row in self.puzzle]
        i, j = self.get_blank_position()
        x, y = move
        new_puzzle[i][j], new_puzzle[i + x][j + y] = new_puzzle[i + x][j + y], new_puzzle[i][j]
        return PuzzleState(new_puzzle, parent=self, move=f"Move: {new_puzzle[i + x][j + y]}")

def best_first_search(initial_state):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put(initial_state)
    while not priority_queue.empty():
        current_state = priority_queue.get()
        if current_state.puzzle == goal_state:
            return current_state
        visited.add(current_state)
        possible_moves = current_state.get_possible_moves()
        for move in possible_moves:
            new_state = current_state.make_move(move)
            if new_state not in visited:
                priority_queue.put(new_state)

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        path = []
        current_state = solution
        while current_state:
            path.append(current_state)
            current_state = current_state.parent
        path.reverse()
        for state in path:
            print(state)

initial_state = PuzzleState([[1, 2, 3], [0, 5, 6], [4, 7, 8]])
solution = best_first_search(initial_state)
print_solution(solution)
