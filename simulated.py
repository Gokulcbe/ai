import random
import math
import numpy as np

class SimulatedAnnealingTSP:
    def __init__(self, cities, temperature=10000, cooling_rate=0.003, num_iterations=1000):
        self.cities = cities
        self.temperature = temperature
        self.cooling_rate = cooling_rate
        self.num_iterations = num_iterations

    def initial_solution(self):
        return random.sample(self.cities, len(self.cities))

    def fitness(self, route):
        total_distance = 0
        for i in range(len(route)):
            total_distance += np.linalg.norm(np.array(route[i - 1]) - np.array(route[i]))
        return 1 / total_distance

    def acceptance_probability(self, cost_diff, temperature):
        if cost_diff < 0:
            return 1.0
        return math.exp(-cost_diff / temperature)

    def anneal(self):
        current_solution = self.initial_solution()
        current_cost = self.fitness(current_solution)
        best_solution = current_solution
        best_cost = current_cost
        for i in range(self.num_iterations):
            new_solution = current_solution[:]
            city1, city2 = random.sample(range(len(new_solution)), 2)
            new_solution[city1], new_solution[city2] = new_solution[city2], new_solution[city1]
            new_cost = self.fitness(new_solution)
            cost_diff = new_cost - current_cost
            if self.acceptance_probability(cost_diff, self.temperature) > random.random():
                current_solution = new_solution
                current_cost = new_cost
            if current_cost > best_cost:
                best_solution = current_solution
                best_cost = current_cost
            self.temperature *= 1 - self.cooling_rate
        return best_solution

if __name__ == "__main__":
    # Example cities (format: [x, y])
    cities = [(0, 0), (2, 3), (3, 8), (3, 9)]
    # Initialize and run Simulated Annealing Algorithm
    sa_tsp = SimulatedAnnealingTSP(cities)
    best_route = sa_tsp.anneal()
    print("Best Route:", best_route)
