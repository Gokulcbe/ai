def map_coloring(map_data, colors):
    def is_valid(region, color, coloring):
        for neighbor in map_data[region]:
            if neighbor in coloring and coloring[neighbor] == color:
                return False
        return True

    def backtrack(region_index, coloring):
        if region_index == len(map_data):
            return coloring
        region = list(map_data.keys())[region_index]
        for color in colors:
            if is_valid(region, color, coloring):
                coloring[region] = color
                result = backtrack(region_index + 1, coloring)
                if result is not None:
                    return result
                coloring.pop(region)
        return None

    return backtrack(0, {})

if __name__ == "__main__":
    # Example usage:
    # Define the map data (regions and their neighbors)
    map_data = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"]
    }

    # Define available colors
    colors = ["red", "green", "blue"]

    # Solve the Map Coloring Problem
    solution = map_coloring(map_data, colors)

    if solution:
        print("Map Coloring Solution:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution found")
