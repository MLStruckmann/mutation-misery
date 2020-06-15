from population import generate_population
from population import train_population
from selection import evolve_generation
import config
import write_results

def main():
    print("start algorithm")
    population = generate_population(config.model_parameter_space,config.n_population_start)
    data = config.data
    results = []

    for i in range(0,config.evolution_steps):
        member_fitness = train_population(population,data)
        population, new_results = evolve_generation(config.selection_parameter,
                                                    population,
                                                    member_fitness)
        results.append(new_results)

    print(results)
    write_results.log_write(results)

if __name__ == '__main__':
    main()