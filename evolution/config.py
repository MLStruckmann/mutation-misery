from sklearn import datasets, model_selection

# Data config
data_dict = datasets.load_iris()
X,y = data_dict["data"], data_dict["target"]
data = model_selection.train_test_split(X, 
                                        y, 
                                        test_size=0.3,
                                        random_state=0)

# Experiment config
evolution_steps = 5

# Network config
neurons_l1 = [10,20,30]
neurons_l2 = [10,20,30]