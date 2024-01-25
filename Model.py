import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
from keras.utils import plot_model
import keras
import numpy as np


class Model:

    def __init__(self, x, y, seed: int = 42):
        plt.rcParams["figure.figsize"] = (10, 5)
        tf.random.set_seed(seed)
        self.model = keras.Sequential()
        self.dataset_init(x, y)

    def dataset_init(self, x, y):
        self.x_train = x["train"]
        self.y_train = y["train"]
        self.x_test = x["test"]
        self.y_test = y["test"]
        ...

    def new_model(self, *hidden_units: int):
        # Input Layer
        input_shape = self.x_train.shape[1:]
        if input_shape is not None:
            self.model.add(keras.layers.InputLayer(input_shape=input_shape))
        else:
            self.model.add(keras.layers.InputLayer())
        # Hidden Layers
        for key in hidden_units:  # More flexible units and layers imporves the odel
            self.model.add(keras.layers.Dense(key, activation="relu"))
        # Output Layer
        self.model.add(keras.layers.Dense(1))

    def train(self,
              lr: float = 0.001,
              epochs: int = 100,
              verbose: int = 0):
        self.model.compile(loss=keras.losses.mae,
                           optimizer=keras.optimizers.Adam(learning_rate=lr),
                           metrics=["mae"])
        history = self.model.fit(self.x_train, self.y_train,
                                 epochs=epochs, verbose=verbose)
        return history

    def predict(self):
        self.pred = self.model.predict(self.x_test)
        return self.pred

    def plot(self, generic: bool = False):
        self.predict()
        plot_model(model=self.model)
        if generic:
            self.metric = np.array([self.x["test"][i][0]
                                    for i in range(len(self.x["test"]))])
            print(self.metric.shape, self.y_train.shape,
                  self.y_test.shape, self.pred.shape)
        else:
            self.metric = self.y_test
        # plt.scatter(self.metric, self.y_train, label="Trained")
        plt.scatter(self.metric, self.y_test, label="Expected")
        plt.scatter(self.metric, self.pred, label="Predicted")
        plt.legend()
        plt.show()

    def eval_metric(self):
        print(self.model.evaluate(self.x_test, self.y_test))
        y_test_ = tf.squeeze(self.y_test)
        pred_ = tf.squeeze(self.predict())
        huber = keras.losses.Huber()
        mae = keras.metrics.MAE(y_test_, pred_).numpy()
        mse = keras.metrics.MSE(y_test_, pred_).numpy()
        h = huber(y_test_, pred_).numpy()
        # print(f"MAE: {mae}\nMSE: {mse}\nHuber: {h}")
        return {
            "mae": mae,
            "mse": mse,
            "huber": h
        }

    def plot_compare(self):
        a = self.y_test
        b = self.pred.reshape(1, -1)[0]
        fig, ax = plt.subplots()
        ax.scatter(np.arange(len(a)), a, label='Expected')
        ax.scatter(np.arange(len(b)), b, label='Predicted')
        for i in range(len(a)):
            ax.plot([i, i], [a[i], b[i]], color='gray')
        ax.legend()
        plt.show()


class View:
    def __init__(self):
        self.df = []

    def compare(self, *metrics: dict) -> pd.DataFrame:
        cols = []
        for i in metrics:
            res = [v for v in i.values()]
            cols = [k for k in i.keys()]
            self.df.append(res)
        return pd.DataFrame(self.df, columns=cols).sort_values(by=["mae", "huber"], ascending=True)

    def loss_plot(self, history):
        return pd.DataFrame(history.history).plot()
        ...


class Create:
    def __init__(self, epochs: int = 10,
                 hidden_layers: int = ...,
                 hidden_units: int = ...,
                 verbose: int = 0,
                 lr: float = 0.01):
        self.model = Model()
        self.view = View()
        self.model.new_model(*(hidden_units for i in range(hidden_layers)))
        self.history = self.model.train(lr=lr, epochs=epochs, verbose=verbose)

    def visualise(self, generic: bool = False):
        self.model.predict()
        self.model.model.summary()
        self.model.plot_compare()
        self.model.plot(generic=generic)
        self.view.loss_plot(self.history)

    def get_data(self):
        return self.history, self.model.eval_metric()
        ...
