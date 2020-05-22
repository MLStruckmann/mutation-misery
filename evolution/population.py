from itertools import product

def generate_population(neurons_l1,neurons_l2):
    print("generate population")
    # Calculate cartesian product for all possible parameter combinations
    network_parameters = list(product(neurons_l1,
                                      neurons_l2))
    print("population has",str(len(network_parameters)),"members")
    return network_parameters


def train_population():
    print("train population")