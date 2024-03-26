import random
import numpy as np

class GeneticAlgorithmTSP:
    def __init__(self, cities, population_size=50, mutation_rate=0.01, generations=100):
        self.cities = cities
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations

    def initial_population(self):
        return [random.sample(self.cities, len(self.cities)) for _ in range(self.population_size)]

    def fitness(self, route):
        total_distance = 0
        for i in range(len(route)):
            total_distance += np.linalg.norm(np.array(route[i-1]) - np.array(route[i]))
        return 1 / total_distance

    def mutate(self, route):
        for swap in range(len(route)):
            if random.random() < self.mutation_rate:
                swap_with = int(random.random() * len(route))
                route[swap], route[swap_with] = route[swap_with], route[swap]
        return route

    def crossover(self, parent1, parent2):
        start = int(random.random() * len(parent1))
        end = int(random.random() * len(parent1))
        if start > end:
            start, end = end, start
        child = [None] * len(parent1)
        for i in range(start, end):
            child[i] = parent1[i]
        for i in range(len(parent2)):
            if parent2[i] not in child:
                for j in range(len(child)):
                    if child[j] is None:
                        child[j] = parent2[i]
                        break
        return child

    def evolve(self, population):
        graded = [(self.fitness(route), route) for route in population]
        graded = [route[1] for route in sorted(graded, key=lambda x: x[0], reverse=True)]
        retain_length = int(len(graded) * 0.2)
        parents = graded[:retain_length]
        for individual in graded[retain_length:]:
            if random.random() < 0.5:
                parents.append(individual)
        parents_length = len(parents)
        desired_length = len(population) - parents_length
        children = []
        while len(children) < desired_length:
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child = self.crossover(parent1, parent2)
            child = self.mutate(child)
            children.append(child)
        parents.extend(children)
        return parents

    def optimize(self):
        population = self.initial_population()
        for i in range(self.generations):
            population = self.evolve(population)
        best_route = max([(self.fitness(route), route) for route in population], key=lambda x: x[0])[1]
        return best_route

# Example usage:
if __name__ == "__main__":
    # Example cities (format: [x, y])
    cities = [(0, 0), (1, 2), (3, 1), (5, 3)]
    # Initialize and run Genetic Algorithm
    ga_tsp = GeneticAlgorithmTSP(cities)
    best_route = ga_tsp.optimize()
    print("Best Route:", best_route)
