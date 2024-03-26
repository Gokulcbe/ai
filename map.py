def map_coloring(states, neighbors):
    colors = {}
    for state in states:
        available_colors = set(["red", "green", "blue"])
        for neighbor in neighbors[state]:
            if neighbor in colors:
                available_colors.discard(colors[neighbor])
        if available_colors:
            colors[state] = available_colors.pop()
        else:
            return None
    return colors

# Define states and their neighbors
states = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW"],
    "Q": ["NT", "SA", "NSW", "V"],
    "NSW": ["SA", "Q", "V"],
    "V": ["Q", "NSW", "T"],
    "T": ["V"]
}

# Solve the problem
solution = map_coloring(states, neighbors)

# Print the solution
if solution:
    print("Solution found:")
    for state, color in solution.items():
        print(f"{state}: {color}")
else:
    print("No solution found.")
