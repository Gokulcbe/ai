import random

def initialize_population(population_size, num_cities):
    population = []
    for _ in range(population_size):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population

def evaluate_fitness(individual, distances):
    total_distance = 0
    for i in range(len(individual) - 1):
        city1, city2 = individual[i], individual[i+1]
        total_distance += distances[city1][city2]
    total_distance += distances[individual[-1]][individual[0]]  # Return to the starting city
    return total_distance

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point]
    for gene in parent2:
        if gene not in child:
            child.append(gene)
    return child

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

def genetic_algorithm(distances, population_size, mutation_rate, generations):
    num_cities = len(distances)
    population = initialize_population(population_size, num_cities)

    for _ in range(generations):
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population

    best_individual = min(population, key=lambda x: evaluate_fitness(x, distances))
    best_distance = evaluate_fitness(best_individual, distances)
    return best_individual, best_distance

# Example usage:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
population_size = 100
mutation_rate = 0.01
generations = 1000

best_solution, best_distance = genetic_algorithm(distances, population_size, mutation_rate, generations)
print("Best solution:", best_solution)
print("Best distance:", best_distance)
