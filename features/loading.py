import os
import boto3
import zipfile
from PIL import Image
from utils import constants
from utils.schemas import (
    BackgroundContext, CoastlineContext, BorderContext
)
from features.caching import (
    cache_background, cache_coastlines, cache_borders
)

def load_background(cache_dir: str, context: BackgroundContext) -> str:
    """
    Loads pre-rendered background image for the given dataset.
    """
    fname = f"{context.tag}-{context.background_name}.png"
    fpath = os.path.join(cache_dir, fname)
    if os.path.exists(cache_dir) and os.path.exists(fpath):
        return fpath
    else:
        return cache_background(cache_dir, context)

def load_coastlines(cache_dir: str, temp_dir: str, context: CoastlineContext) -> str:
    """
    Loads pre-rendered coastlines for the given dataset.
    """
    fname = f"{context.tag}-coastlines.png"
    fpath = os.path.join(cache_dir, fname)
    if os.path.exists(cache_dir) and os.path.exists(fpath):
        return fpath
    else:
        return cache_coastlines(cache_dir, temp_dir, context)

def load_borders(cache_dir: str, temp_dir: str, context: BorderContext):
    """
    Loads pre-rendered state and country borders for the given dataset.
    """
    fname = f"{context.tag}-borders.png"
    fpath = os.path.join(cache_dir, fname)
    if os.path.exists(cache_dir) and os.path.exists(fpath):
        return fpath
    else:
        return cache_borders(cache_dir, temp_dir, context)

def load_roads():
    """
    Loads pre-rendered roads for the given dataset.
    """
    pass

def load_rivers():
    """
    Loads pre-rendered rivers for the given dataset.
    """
    pass