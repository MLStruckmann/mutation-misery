from reproduction import mating
import random

def evolve_generation(selection_parameter,population,member_fitness):
    print("evolve generation")

    (survival_ratio, 
    mating_best_ratio, 
    mating_lucky_ratio,
    n_survival_min,
    n_mating_best_min,
    n_mating_lucky_min) = selection_parameter

    population_size = len(population)
    new_population = []
    results_dict = dict(zip(member_fitness,population))
    # print(results_dict)
    parameters_list_sorted = [results_dict[i] for i in sorted(results_dict)][::-1]
    # print(parameters_list_sorted)

    # Calculate integer values for survival and mating
    n_survival = max(n_survival_min,round(population_size*survival_ratio))
    n_mating_best = max(n_mating_best_min,round(population_size*mating_best_ratio))
    n_mating_lucky = max(n_mating_lucky_min,round(population_size*mating_lucky_ratio))

    # Best individuals to survive
    survival_parameters = parameters_list_sorted[:n_survival]

    # Divide into best individuals for reproduction and rest
    best_parameters = parameters_list_sorted[:n_mating_best]
    worst_parameters = parameters_list_sorted[n_mating_best:]

    # Pick randomly chosen reproduction individuals from rest
    lucky_parameters = random.sample(worst_parameters,k=n_mating_lucky) # sample avoids duplicates

    # Reproduce from best and lucky individuals
    new_parameters = mating(best_parameters,lucky_parameters)

    new_population.extend(survival_parameters)
    new_population.extend(new_parameters)
    new_population.extend(lucky_parameters)

    print("population size changed from {} to {}".format(len(population),len(new_population)))
    print("The {} best and {} lucky individuals reproduced and {} survived".format(n_mating_best,
                                                                                   n_mating_lucky,
                                                                                   n_survival))
    
    return new_population


