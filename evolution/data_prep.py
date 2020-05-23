from sklearn import datasets
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelBinarizer

def data_prep():
    data_dict = datasets.load_iris()
    X,y = data_dict["data"], data_dict["target"]
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, 
                                                                        y, 
                                                                        test_size=0.3,
                                                                        random_state=0)
    sc = StandardScaler() # Standardize input data
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.transform(X_test)

    encoder = LabelBinarizer() # One hot encode target data for training
    y_train_hot = encoder.fit_transform(y_train)

    data = (X_train_std, 
            X_test_std, 
            y_train_hot, 
            y_test)

    return data