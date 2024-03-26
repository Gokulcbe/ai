import random
import math

def generate_initial_solution(num_cities):
    return list(range(num_cities))

def evaluate_cost(solution, distances):
    total_distance = 0
    for i in range(len(solution) - 1):
        city1, city2 = solution[i], solution[i+1]
        total_distance += distances[city1][city2]
    total_distance += distances[solution[-1]][solution[0]]  # Return to the starting city
    return total_distance

def generate_neighbor_solution(solution):
    neighbor_solution = solution[:]
    idx1, idx2 = random.sample(range(len(solution)), 2)
    neighbor_solution[idx1], neighbor_solution[idx2] = neighbor_solution[idx2], neighbor_solution[idx1]
    return neighbor_solution

def acceptance_probability(new_cost, old_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    return math.exp((old_cost - new_cost) / temperature)

def cool(temperature, cooling_rate):
    return temperature * cooling_rate

def simulated_annealing(distances, initial_temperature, cooling_rate, max_iterations):
    num_cities = len(distances)
    current_solution = generate_initial_solution(num_cities)
    current_cost = evaluate_cost(current_solution, distances)
    best_solution = current_solution[:]
    best_cost = current_cost
    temperature = initial_temperature

    for _ in range(max_iterations):
        new_solution = generate_neighbor_solution(current_solution)
        new_cost = evaluate_cost(new_solution, distances)
        if new_cost < current_cost or random.random() < acceptance_probability(new_cost, current_cost, temperature):
            current_solution = new_solution
            current_cost = new_cost
            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost
        temperature = cool(temperature, cooling_rate)

    return best_solution, best_cost

# Example usage:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
initial_temperature = 1000
cooling_rate = 0.95
max_iterations = 1000

best_solution, best_distance = simulated_annealing(distances, initial_temperature, cooling_rate, max_iterations)
print("Best solution:", best_solution)
print("Best distance:", best_distance)
