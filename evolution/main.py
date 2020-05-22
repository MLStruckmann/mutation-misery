from population import generate_population, train_population
from selection import evolve_generation
import config

def main():
    print("start algorithm")
    model_parameters = generate_population(config.model_parameter_space)
    data = config.data

    for i in range(0,config.evolution_steps):
        member_fitness = train_population(network_parameters,data)
        evolve_generation()

if __name__ == '__main__':
    main()