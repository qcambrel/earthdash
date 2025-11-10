import numpy as np
from utils.schemas import BandpassContext
from skimage.restoration import denoise_nl_means, estimate_sigma

def nonlocal_means(data: np.ndarray, fast: bool = False) -> np.ndarray:
    """
    Applies nonlocal means denoising to a 2D array.
    """
    pass

def bandpass_filter(data: np.ndarray, low: float, high: float, context: BandpassContext) -> np.ndarray:
    """
    Applies a bandpass filter to a 2D array.
    Bandpass filters out frequencies outside of a specific range.
    """
    pass