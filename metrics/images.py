import lpips
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

def infer_channel_axis(image: np.ndarray) -> int:
    """
    Computes the channel axis of an image.
    This is needed to compute SSIM.
    """
    pass

def compute_ssim(image1: Image, image2: Image) -> float:
    """
    Computes the structural similarity index measure between two images.
    """
    pass

def compute_psnr(image1: Image, image2: Image) -> float:
    """
    Computes the peak signal to noise ratio between two images.
    """
    pass

def compute_lpips(image1: Image, image2: Image) -> float:
    """
    Computes the learned perceptual image patch similarity between two images.
    """
    pass