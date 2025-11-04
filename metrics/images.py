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
    if image.ndim == 2:
        return None
    
    if image.ndim == 3:
        for ax, size in enumerate(image.shape):
            if size in (3, 4):
                return ax
        return -1
    
    raise ValueError(f"Unexpected image ndim={image.ndim}; SSIM expects 2D or 3D (H,W[,C]).")

def compute_ssim(image1: Image, image2: Image) -> float:
    """
    Computes the structural similarity index measure between two images.
    """
    image1 = np.array(image1)
    image2 = np.array(image2)

    channel_axis = infer_channel_axis(image1)

    H, W, _ = image1.shape
    window = max(3, min(7, (min(H + W) if min(H, W) % 2 else min(H, W) - 1)))

    image1 = image1.astype(np.float32)
    image2 = image2.astype(np.float32)

    data_range = float(image1.max() - image1.min()) or 1.0

    return ssim(image1, image2, window_size=window, channel_axis=channel_axis, data_range=data_range)

def compute_psnr(image1: Image, image2: Image) -> float:
    """
    Computes the peak signal to noise ratio between two images.
    """
    image1 = np.array(image1)
    image2 = np.array(image2)

    data_range = float(image1.max() - image1.min()) or 1.0

    return psnr(image1, image2, data_range=data_range)

def compute_lpips(image1: Image, image2: Image) -> float:
    """
    Computes the learned perceptual image patch similarity between two images.
    """
    loss_fn_alex = lpips.LPIPS(net="alex")
    return loss_fn_alex(np.array(image1), np.array(image2))