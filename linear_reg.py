__author__ = 'prithvin'

from sklearn import linear_model


class Predictor:
    def __init__(self, features, output):
        self.features = features
        self.output = output
        self.model = linear_model.LinearRegression(fit_intercept=True, normalize=True)

    def fit(self):
        self.model.fit(self.features, self.output)

    def predict(self, features):
        return self.model.predict(features)