import numpy as np
from utils.schemas import BandpassContext
from skimage.restoration import denoise_nl_means, estimate_sigma

def nonlocal_means(data: np.ndarray, fast: bool = False) -> np.ndarray:
    """
    Applies nonlocal means denoising to a 2D array.

    Args:
        data (np.ndarray): The image to denoise
        fast (bool, optional): Whether to use fast mode. Defaults to False.

    Returns:
        np.ndarray: The denoised image
    """
    sigma = np.mean(estimate_sigma(data, channel_axis=-1))
    denoised = denoise_nl_means(data, sigma=sigma, fast_mode=fast)
    return denoised

def bandpass_filter(data: np.ndarray, low: float, high: float, context: BandpassContext) -> np.ndarray:
    """
    Applies a bandpass filter to a 2D array.
    Bandpass filters out frequencies outside of a specific range.
    """
    pass