class Implementation:
    """
    A class containing the implementation methods, from which each algorithm can inherit from
    """
    def __init__(self):
        """
        Initialises the class
        """
        self.name = 'Unknown'

    def fit_model(self, X, Y):
        """
        Fits the given model to the given data
        """
        pass

    def plot(self):
        """
        Plots the results
        """
        pass

    def __str__(self):
        return self.name

class LinearRegression(Implementation):
    """
    A linear regression model
    """
    def __init__(self):
        """
        Initialises the linear regression model
        """
        self.name = 'Linear Regression'

class LogisticRegression(Implementation):
    """
    A logistic regression model
    """
    def __init__(self):
        """
        Initialises the logistic regression model
        """
        self.name = 'Logistic Regression'
