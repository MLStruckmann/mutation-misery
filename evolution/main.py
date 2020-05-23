from population import generate_population
from population import train_population
from selection import evolve_generation
import config

def main():
    print("start algorithm")
    population = generate_population(config.model_parameter_space,config.n_population_start)
    data = config.data

    for i in range(0,config.evolution_steps):
        member_fitness = train_population(population,data)
        population = evolve_generation(config.selection_parameter,population,member_fitness)

if __name__ == '__main__':
    main()