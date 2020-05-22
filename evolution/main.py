from population import generate_population, train_population
from selection import evolve_generation
import config

def main():
    print("start algorithm")
    model_parameters = generate_population(config.model_parameter_space)
    data = config.data

    for i in range(0,config.evolution_steps):
        member_fitness = train_population(model_parameters,data)
        model_parameters = evolve_generation(config.selection_parameter,model_parameters,member_fitness)

if __name__ == '__main__':
    main()