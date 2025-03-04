"""Autograding script."""


def load_data():

    import pandas as pd

    dataset = pd.read_csv("files/input/auto_mpg.csv")
    dataset = dataset.dropna()
    dataset["Origin"] = dataset["Origin"].map(
        {1: "USA", 2: "Europe", 3: "Japan"},
    )
    y = dataset.pop("MPG")
    x = dataset.copy()

    return x, y


def load_estimator():

    import os
    import pickle

    if not os.path.exists("homework/estimator.pickle"):
        return None
    with open("homework/estimator.pickle", "rb") as file:
        estimator = pickle.load(file)

    return estimator


from sklearn.metrics import r2_score


def test_01():
    x, y = load_data()
    estimator = load_estimator()

    r2 = r2_score(y_true=y, y_pred=estimator.predict(x))

    assert r2 > 0.83  # Ajusta este valor según el rendimiento esperado
