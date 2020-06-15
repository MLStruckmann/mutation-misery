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

    results_dict = {}
    for i in range(0,len(population)):
        key = "model_" + str(i)
        results_dict[key] = [member_fitness[i],population[i]]
    results_list = sorted(results_dict.values())[::-1]
    parameters_list_sorted = [x[1] for x in results_list]
    print(results_list)
    population_size = len(population)
    new_population = []

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

    print("survival parameters: {}".format(survival_parameters))
    print("new parameters: {}".format(new_parameters))
    print("population size changed from {} to {}".format(len(population),len(new_population)))
    print("the {} best and {} lucky individuals reproduced and {} survived".format(n_mating_best,
                                                                                   n_mating_lucky,
                                                                                   n_survival))
    
    return new_population, results_list


