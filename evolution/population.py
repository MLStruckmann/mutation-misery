import random
import config
if config.model_choice == 'model_nn':
    from model_nn import get_result

def generate_population(model_parameter_space,n_population_start):
    print("generate random population of size {}".format(n_population_start))
    # Choose random subset from parameter space for each individual
    population = []
    for i in range(0,n_population_start):
        individual = [random.choice(x) for x in model_parameter_space]
        population.append(individual)
    return population

def train_population(population,data):
    print("train population")
    member_fitness = []
    for idx, parameter_setup in enumerate(population):
        print("train model {} of {}".format(idx+1,len(population)))
        fitness_measure = get_result(parameter_setup,data)
        member_fitness.append(fitness_measure)
    return member_fitness
