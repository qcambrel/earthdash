import ray
import numpy as np

def batch_process(images: list[np.ndarray], func: callable) -> ray.data.Dataset:
    """
    Batches a list of images and applies a function to each batch.
    Batching with Ray Data improves performance.
    """
    ds = ray.data.read_images(images).map_batches(func)
    return ds