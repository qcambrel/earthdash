import numpy as np
from processing.resampling import resample

def test_resample():
    data      = np.random.rand(100, 100)
    resampled = resample(data, (50, 50))
    assert resampled.shape == (50, 50)