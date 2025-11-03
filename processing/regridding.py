import numpy as np
from numba import int64, float64, float32
from numba.experimental import jitclass
from abc import ABC, abstractmethod

spec = []

class Regridder(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def regrid(self):
        pass

@jitclass(spec)
class ConservativeRegridder(Regridder):
    def __init__(self):
        pass

    def regrid(self):
        pass

@jitclass(spec)
class BilinearRegridder(Regridder):
    def __init__(self):
        pass

    def regrid(self):
        pass

@jitclass(spec)
class NearestRegridder(Regridder):
    def __init__(self):
        pass

    def regrid(self):
        pass