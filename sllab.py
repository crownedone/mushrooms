"""
Packages:
    numpy as np
    matplotlib.pyplot as plt
    pandas as pd

Functions:
    plotXY
    plot_frontiere
"""

print(__doc__)

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import (KNeighborsClassifier,
                               NeighborhoodComponentsAnalysis)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn import preprocessing as pp
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline


def plotXY(X, Y, legend=True):
    """
        Scatter points with a color for each class.
        Input:
            X and Y may be:
            - two numpy arrays with two columns; each array is the data matrix for a class (works only for
            two classes).
            - a (n,2)-numpy array with two columns (the data matrix) and the (n,)-vector of labels (works for many classes).
    """    
    if Y.ndim > 1:
        X1 = X
        X2 = Y
        print(X)
        print(Y)
        XX = np.concatenate((X, Y), axis=0)
        YY = np.concatenate((np.ones(X.shape[0]), -np.ones(Y.shape[0])))
    else:
        XX = X
        YY = Y
    for icl, cl in enumerate(np.unique(YY)):
        plt.scatter(XX[YY==cl, 0], XX[YY==cl, 1], label='Class {0:d}'.format(icl+1))
    plt.axis('equal')
    if legend:
        plt.legend()


def plot_frontiere(clf, data=None, num=500, label=None):
    """
        Plot the frontiere f(x)=0 of the classifier clf within the same range as the one
        of the data.
        Input:
            clf: binary classifier with a method decision_function
            data: input data (X)
            num: discretization parameter
    """
    xmin, ymin = data.min(axis=0)
    xmax, ymax = data.max(axis=0)
    x, y = np.meshgrid(np.linspace(xmin, xmax, num), np.linspace(ymin, ymax))
    z = clf.decision_function(np.c_[x.ravel(), y.ravel()]).reshape(x.shape)
    cs = plt.contour(x, y, z, [0], colors='g')
    if label is not None:
        cs.levels = [label]
        plt.gca().clabel(cs)
    return cs
