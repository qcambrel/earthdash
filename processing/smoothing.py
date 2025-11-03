import numpy as np
import scipy.signal as signal
from scipy.fft import fftshift, ifftshift, fftn, ifftn
from utils.schemas import BandpassContext

def savitzky_golay2d(z: np.ndarray, window_size: int, order: int, derivative: str = None) -> np.ndarray:
    pass

def bandpass_filter(data: np.ndarray, low: float, high: float, context: BandpassContext) -> np.ndarray:
    pass