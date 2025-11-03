import numpy as np
from sunpy.image import resample as rs

def resample(data: np.ndarray, shape: tuple, center=True):
    return rs(data, shape, center=center)