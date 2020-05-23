import random

def mating(best_parameters,lucky_parameters):
    print("mating process")
    all_parameters = best_parameters + lucky_parameters
    new_parameters = []

    for i in range(0,len(all_parameters)): # create as many children as parents
        random_choice = random.sample(all_parameters,k=2) # sample avoids duplicates
        female = random_choice[0]
        male = random_choice[1]
        child = []

        for ii in range(0,len(female)): # iterate over all parameters
            parameter_choices = ((male[ii],) + (female[ii],))
            parameter_choice = random.choice(parameter_choices)
            child.append(parameter_choice)
        new_parameters.append(child)
        
    return new_parameters


