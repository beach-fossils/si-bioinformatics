# X = numpy array of shape (n_samples, n_features)
# Y = numpy array of shape (n_samples, 1) uma dimensao
# features = lista de strings com os nomes das features
# label = string com o nome da label

class Dataset:
    def __init__(self, x, y, features, label):
        self.x = x
        self.y = y
        self.features = features
        self.label = label

    def shape(self):
        """Returns the shape of the dataset."""
        return self.x.shape

    def has_labels(self):
        """Returns True if the dataset has labels.
        if true, the dataset is a supervised dataset."""
        return self.y is not None

    def get_classes(self):
        """Possible values in y; returns the classes of the dataset."""
        if self.has_labels():
            return np.unique(self.y)
        else:
            return 'No labels'

    def get_mean(self):
        """Returns the mean of the dataset."""
        return np.mean(self.x, axis=0)

    def get_variance(self):
        """Returns the variance of the dataset."""
        return np.var(self.x, axis=0)

    def get_median(self):
        """Returns the median of the dataset."""
        return np.median(self.x, axis=0)

    def get_min(self):
        """Returns the minimum of the dataset."""
        return np.min(self.x, axis=0)

    def get_max(self):
        """Returns the maximum of the dataset."""
        return np.max(self.x, axis=0)

    def summary(self):
        """Returns a summary of the dataset."""
        #pandas dataframe colum names are features and row mean, median, min, max, variance
        df = pd.DataFrame(columns=self.features)
        df.loc['mean'] = self.get_mean()
        df.loc['median'] = self.get_median()
        df.loc['min'] = self.get_min()
        df.loc['max'] = self.get_max()
        df.loc['variance'] = self.get_variance()
        return df



# testing
import numpy as np
import pandas as pd

if __name__ == '__main__':
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([1, 2])
    features = ['a', 'b', 'c']
    label = 'y'
    dataset = Dataset(x, y, features, label)
    print(dataset.shape())
    print(dataset.has_labels())
    print(dataset.get_classes())
    print(dataset.get_mean())
    print(dataset.summary())
