from implementations import Implementation
from sklearn import linear_model
import matplotlib.pyplot as plt, mpld3
import math

class LogisticRegression(Implementation):
    """A class for logistic regression"""
    def __init__(self, data):
        self.name = 'logistic-regression'
        self.X = [row[:-1] for row in data]
        self.Y = [row[-1] for row in data]

    def fit(self):
        algorithm = linear_model.LogisticRegression()
        algorithm.fit(self.X, self.Y)

        self.coeff = algorithm.coef_[0][0]
        self.intercept = algorithm.intercept_[0]

    def plot(self):
        fig = plt.figure()
        plt.scatter(self.X, self.Y)
        min_x = min(self.X)[0]
        max_x = max(self.X)[0]
        step = (max_x - min_x) / 100.0 # This needs to be fixed
        x_line = [i * step + min_x for i in range(100)]
        logistic_fit = lambda x: 1.0 / (1.0 + math.exp(-self.intercept - self.coeff*x))
        y_line = [logistic_fit(x) for x in x_line]
        plt.plot(x_line, y_line)
        fig_html = mpld3.fig_to_html(fig) # When we have local mpld3 libraries we will need to tweak this
        return fig_html

    def run(self):
        self.fit()
        return self.plot(), self.coeff, self.intercept
