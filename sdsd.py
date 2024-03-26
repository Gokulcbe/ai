import numpy as np
import random
import math

def fitness_function(x):
    return np.sin(x) * np.cos(0.5 * x)

def genetic_algorithm(pop_size, generations, mutation_rate):
    population = [random.uniform(-10, 10) for _ in range(pop_size)]
    for _ in range(generations):
        fitness = [fitness_function(x) for x in population]
        parents = sorted(zip(population, fitness), key=lambda x: x[1], reverse=True)[:2]
        offspring = []
        for _ in range(pop_size):
            parent1, parent2 = random.choices(parents, k=2)
            child = (parent1[0] + parent2[0]) / 2.0
            if random.random() < mutation_rate:
                child += random.uniform(-0.1, 0.1)
            offspring.append(child)
        population = offspring
    best_solution = sorted(zip(population, fitness), key=lambda x: x[1], reverse=True)[0]
    return best_solution

def simulated_annealing(initial_solution, max_iterations, initial_temperature, cooling_rate):
    current_solution = initial_solution
    current_fitness = fitness_function(current_solution)
    best_solution = current_solution
    best_fitness = current_fitness
    temperature = initial_temperature
    for _ in range(max_iterations):
        neighbor = current_solution + random.uniform(-0.1, 0.1)
        neighbor_fitness = fitness_function(neighbor)
        if neighbor_fitness > current_fitness or random.random() < math.exp((neighbor_fitness - current_fitness) / temperature):
            current_solution = neighbor
            current_fitness = neighbor_fitness
        if current_fitness > best_fitness:
            best_solution = current_solution
            best_fitness = current_fitness
        temperature *= cooling_rate
    return best_solution, best_fitness

if __name__ == "__main__":
    best_genetic_solution, best_genetic_fitness = genetic_algorithm(pop_size=100, generations=100, mutation_rate=0.1)
    print("Genetic Algorithm:")
    print("Best solution:", best_genetic_solution)  
    print("Best fitness:", best_genetic_fitness)

    initial_solution = random.uniform(-10, 10)
    best_sa_solution, best_sa_fitness = simulated_annealing(initial_solution, max_iterations=1060, initial_temperature=10.0, cooling_rate=0.95)
    print("\nSimulated Annealing:")
    print("Best solution:", best_sa_solution)
    print("Best fitness:", best_sa_fitness)
