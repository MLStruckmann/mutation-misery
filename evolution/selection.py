
def evolve_generation(selection_parameter,model_parameters,member_fitness):
    print("evolve generation")
    survival_ratio, mating_best_ratio, mating_lucky_ratio = selection_parameter

    initial_population = len(model_parameters)

    results_dict = dict(zip(model_parameters,member_fitness))

    new_population = len(model_parameters)
    print("population size changed from {} to {}".format(initial_population,new_population))
    return(model_parameters)


