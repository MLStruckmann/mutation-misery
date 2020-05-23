from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from sklearn.metrics import accuracy_score

def get_result(parameter_setup,data):
    X_train_std, X_test_std, y_train_hot, y_test = data
    neurons_l1 = parameter_setup[0]
    neurons_l2 = parameter_setup[1]
    activation_func = parameter_setup[2]

    # Create model
    model = Sequential()
    n_cols = X_train_std.shape[1]
    model.add(Dense(neurons_l1, activation=activation_func, input_shape=(n_cols,)))
    model.add(Dense(neurons_l2, activation=activation_func))
    model.add(Dense(3, activation='softmax'))
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
    early_stopping_monitor = EarlyStopping(patience=3)

    # Train model
    model.fit(X_train_std, y_train_hot,
              validation_split=0.2, 
              epochs=30, 
              callbacks=[early_stopping_monitor],
              verbose=0)

    # Test model
    y_test_predict = model.predict_classes(X_test_std)
    model_accuracy = accuracy_score(y_true=y_test,
                                    y_pred=y_test_predict)
    print("model has accuracy of {}".format(model_accuracy))
    return model_accuracy



