import numpy as np
from sunpy.image import resample as rs

def resample(data: np.ndarray, shape: tuple, center=True):
    """
    Resamples an image to the given shape.
    """
    return rs.resample(data, shape, center=center)