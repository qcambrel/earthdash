import numpy as np
import scipy.signal as signal
from scipy.fft import fftshift, ifftshift, fftn, ifftn
from utils.schemas import BandpassContext

def savitzky_golay2d(z: np.ndarray, window_size: int, order: int, derivative: str = None) -> np.ndarray:
    """
    Applies a Savitzky-Golay filter to a 2D array.
    Savitzky-Golay reduces noise while preserving important features.
    """
    pass

def bandpass_filter(data: np.ndarray, low: float, high: float, context: BandpassContext) -> np.ndarray:
    """
    Applies a bandpass filter to a 2D array.
    Bandpass filters out frequencies outside of a specific range.
    """
    pass