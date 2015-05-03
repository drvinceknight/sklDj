from implementations import Implementation
from sklearn import linear_model
import matplotlib.pyplot as plt, mpld3

class LinearRegression(Implementation):
    """A class for linear regression"""
    def __init__(self, data):
        self.name = 'linear-regression'
        self.X = [row[:-1] for row in data]
        self.Y = [row[-1] for row in data]

    def fit(self):
        algorithm = linear_model.LinearRegression()
        algorithm.fit(self.X, self.Y)

        self.coeff = algorithm.coef_
        self.intercept = algorithm.intercept_

    def plot(self):
        fig = plt.figure()
        plt.scatter(self.X, self.Y)
        min_x = min(self.X)[0]
        max_x = max(self.X)[0]
        line = lambda x: self.coeff * x + self.intercept
        plt.plot([min_x, max_x], [line(min_x), line(max_x)])
        fig_html = mpld3.fig_to_html(fig) # When we have local mpld3 libraries we will need to tweak this
        return fig_html

    def run(self):
        self.fit()
        return self.plot(), self.coeff, self.intercept
