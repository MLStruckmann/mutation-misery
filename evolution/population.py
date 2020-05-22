from itertools import product
from model import get_result
import sklearn

def generate_population(model_parameter_space):
    print("generate population")
    # Calculate cartesian product for all possible parameter combinations
    model_parameters = list(product(model_parameter_space))
    print(model_parameters)
    print("population has",len(model_parameters),"members")
    return model_parameters

def train_population(network_parameters,data):
    print("train population")
    member_fitness = []
    for idx, parameter_setup in enumerate(model_parameters):
        print("train model",idx,"of",len(model_parameters))
        fitness_measure = get_result(parameter_setup,data)
        member_fitness.append(fitness_measure)
