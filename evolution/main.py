from population import generate_population, train_population
from selection import evolve_generation
import config

def main():
    print("start algorithm")
    population = generate_population(config.neurons_l1,
                                     config.neurons_l2)
    for i in range(0,config.evolution_steps):
        evolve_generation()
        train_population()

if __name__ == '__main__':
    main()