import itertools

# Function to calculate the distance between two cities (Euclidean distance)
def distance(city1, city2):
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def total_distance(route, cities):
    total = 0
    for i in range(len(route) - 1):
        total += distance(cities[route[i]], cities[route[i+1]])
    # Add distance from last city back to the starting city
    total += distance(cities[route[-1]], cities[route[0]])
    return total

def tsp_brute_force(cities):
    shortest_distance = float('inf')
    shortest_route = None

    # Generate all possible permutations of cities
    for route in itertools.permutations(range(len(cities))):
        route_distance = total_distance(route, cities)
        if route_distance < shortest_distance:
            shortest_distance = route_distance
            shortest_route = route

    return shortest_route, shortest_distance

# Example usage
if __name__ == "__main__":
    # Example cities (format: [x, y])
    cities = [(0, 0), (1, 2), (3, 1), (5, 3)]

    # Find the shortest route and its distance
    shortest_route, shortest_distance = tsp_brute_force(cities)

    print("Shortest route:", shortest_route)
    print("Shortest distance:", shortest_distance)
