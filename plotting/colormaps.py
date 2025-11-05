import os
import pickle
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.interpolate as interp
from utils.schemas import ColormapContext

class Colormap:
    def __init__(self, context: ColormapContext):
        self.rgb      = context.rgb_npy if context.rgb_npy else context.rgb_mpl
        self.levels   = context.levels
        self.ticks    = context.ticks
        self.target   = context.target
        self.vmin     = context.vmin
        self.vmax     = context.vmax
        self.filename = context.filename
        self._map()

    def _map(self):
        match type(self.rgb):
            case np.ndarray:
                self.cmap = mpl.colors.ListedColormap(self.rgb)
            case type(""):
                self.cmap = plt.colormaps[self.rgb]
            case _:
                if self.filename and os.path.exists(self.filename):
                    with open(self.filename, "rb") as pkl:
                        self.cmap = pickle.load(pkl)
                else:
                    raise NotImplementedError
        
        if self.vmin and self.vmax:
            self.norm   = mpl.colors.Normalize(vmin=self.vmin, vmax=self.vmax)
        else:     
            self.levels = interpolate_levels(self.ticks, self.target) if self.target else self.levels
            self.norm   = mpl.colors.BoundaryNorm(self.levels, self.cmap.N)

def interpolate_levels(ticks: np.ndarray, target: np.ndarray) -> np.ndarray:
    """
    Interpolate an array of tick values to target color levels
    """
    func   = interp.interp1d(np.arange(len(ticks)), ticks)
    levels = func(np.linspace(0.0, len(ticks) - 1, len(target)))
    return levels