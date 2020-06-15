from data_prep import data_prep

# Evolution config
n_population_start = 9
evolution_steps = 3

# Selection config
survival_ratio = 0.4
mating_best_ratio = 0.3
mating_lucky_ratio = 0.1
n_survival_min = 1
n_mating_best_min = 2
n_mating_lucky_min = 1
selection_parameter = (survival_ratio,
                       mating_best_ratio,
                       mating_lucky_ratio,
                       n_survival_min,
                       n_mating_best_min,
                       n_mating_lucky_min)

# Model config
model_choice = 'model_nn'

if model_choice == 'model_nn': 
    neurons_l1 = (40,50,60)
    neurons_l2 = (10,20,30)
    acitvation_func = ('relu',)
    model_parameter_space = (neurons_l1,
                             neurons_l2,
                             acitvation_func)

# Data config
data = data_prep()