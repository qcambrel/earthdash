import matplotlib as mpl
import cartopy.crs as ccrs
from pydantic import BaseModel
import matplotlib.pyplot as plt

class BandpassContext(BaseModel):
    ideal: bool = False
    butterworth: bool = False
    gaussian: bool = False

class PlotterContext(BaseModel):
    projection: ccrs.Projection = ccrs.PlateCarree()
    transform: ccrs.Projection = ccrs.PlateCarree()
    cmap: str | mpl.colors.Colormap = plt.cm.viridis
    norm: mpl.colors.Normalize = None
    vmin: float = None
    vmax: float = None