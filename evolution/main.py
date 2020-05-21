from population import generate_population, train_population
from selection import evolve_generation
import config

def main():
    print("start algorithm")
    generate_population()
    for i in range(0,config.evolution_steps):
        evolve_generation()
        train_population()

if __name__ == '__main__':
    main()