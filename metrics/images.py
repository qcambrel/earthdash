import lpips
import torch
import numpy as np
from PIL import Image
from skimage.metrics import mean_squared_error as mse
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

    Args:
        image1 (Image): The first image
        image2 (Image): The second image

    Returns:
        float: The structural similarity index
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

    Args:
        image1 (Image): The first image
        image2 (Image): The second image

    Returns:
        float: The peak signal to noise ratio
    """
    image1 = np.array(image1)
    image2 = np.array(image2)

    data_range = float(image1.max() - image1.min()) or 1.0

    return psnr(image1, image2, data_range=data_range)

def compute_lpips(image1: Image, image2: Image) -> float:
    """
    Computes the learned perceptual image patch similarity between two images.

    Args:
        image1 (Image): The first image
        image2 (Image): The second image

    Returns:
        float: The LPIPS score
    """
    loss_fn_alex = lpips.LPIPS(net="alex")
    
    imgs = [image1, image2]
    for i in range(2):
        arr = np.array(imgs[i])
        if arr.ndim == 2:
            arr = np.repeat(arr[..., None], 3, axis=2)
        t = torch.from_numpy(arr).permute(2, 0, 1).unsqueeze(0).float() / 255
        t = t * 2 - 1
        imgs[i] = t
    
    image1, image2 = imgs
    return loss_fn_alex(image1, image2)
   

def compute_mse(image1: Image, image2: Image) -> float:
    """
    Computes the mean squared error between two images.

    Args:
        image1 (Image): The first image
        image2 (Image): The second image

    Returns:
        float: The mean squared error
    """
    return mse(np.array(image1), np.array(image2))