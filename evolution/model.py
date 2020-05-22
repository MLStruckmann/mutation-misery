from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def get_result(parameter_setup,data):
    X_train, X_test, y_train, y_test = data
    neurons_l1 = data[0]
    neurons_l2 = data[1]

    # Standardize data
    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.transform(X_test)

    # Create model
    model = sequential()
    n_cols = train_X_std.shape[1]
    model.add(Dense(neurons_l1, activation='relu', input_shape=(n_cols,)))
    model.add(Dense(neurons_l2, activation='relu'))
    model.add(Dense(3))
    model.compile(optimizer='adam', loss='mean_squared_error')
    early_stopping_monitor = EarlyStopping(patience=3)

    # Train model
    model.fit(X_train_std, y_train,
              validation_split=0.2, 
              epochs=30, 
              callbacks=[early_stopping_monitor],
              verbose=0)

    # Test model
    y_test_predict = model.predict(X_test_std)
    model_accuracy = accuracy_score(y_true=y_test,
                                    y_pred=y_test_predict)

    return model_accuracy



