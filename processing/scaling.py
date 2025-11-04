import numpy as np

def scale(image: np.ndarray, low: float = None, high: float = None) -> np.ndarray:
    """
    Scales an image to the range [0, 1].
    Scaling alpha channels enables intensity based alpha blending.
    """
    if low is None:
        low = np.min(image)
    if high is None:
        high = np.max(image)
        
    scaled_image = (image - low) / (high - low) * 255
    scaled_image = np.clip(scaled_image, 0, 255) / 255
    return scaled_image