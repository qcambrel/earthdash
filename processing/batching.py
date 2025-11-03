import ray
import numpy as np

def batch_process(images: list[np.ndarray], func: callable) -> ray.data.Dataset:
    ds = ray.data.read_images(images).map_batches(func)
    return ds