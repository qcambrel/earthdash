import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from abc import ABC, abstractmethod

class Colormap(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def _map(self):
        pass