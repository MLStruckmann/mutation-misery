from data_prep import data_prep

# Evolution config
n_population_start = 150
evolution_steps = 3

# Selection config
survival_ratio = 0.9
mating_best_ratio = 0.8
mating_lucky_ratio = 0.15
n_survival_min = 0
n_mating_best_min = 0
n_mating_lucky_min = 0
selection_parameter = (survival_ratio,
                       mating_best_ratio,
                       mating_lucky_ratio,
                       n_survival_min,
                       n_mating_best_min,
                       n_mating_lucky_min)

# Model config
model_choice = 'model_nn'

if model_choice == 'model_nn': 
    neurons_l1 = [i for i in range(30,131)]
    neurons_l2 = [i for i in range(10,71)]
    acitvation_func = ('relu',)
    model_parameter_space = (neurons_l1,
                             neurons_l2,
                             acitvation_func)

# Data config
data = data_prep()