import lpips
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

def infer_channel_axis(image: np.ndarray) -> int:
    pass

def compute_ssim(image1: Image, image2: Image) -> float:
    pass

def compute_psnr(image1: Image, image2: Image) -> float:
    pass

def compute_lpips(image1: Image, image2: Image) -> float:
    pass