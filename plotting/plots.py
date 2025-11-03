import os
import numpy as np
from PIL import Image
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class Plotter(ABC):
    def __init__(self):
        pass

class WindPlotter(Plotter):
    def __init__(self):
        pass

class TempPlotter(Plotter):
    def __init__(self):
        pass

class WeatherPlotter(Plotter):
    def __init__(self):
        pass

class CAPEPlotter(Plotter):
    def __init__(self):
        pass

class SLPPlotter(Plotter):
    def __init__(self):
        pass

class AerosolPlotter(Plotter):
    def __init__(self):
        pass

class LWIRPlotter(Plotter):
    def __init__(self):
        pass

class RadarPlotter(Plotter):
    def __init__(self):
        pass

class AccRainPlotter(Plotter):
    def __init__(self):
        pass

class AccSnowPlotter(Plotter):
    def __init__(self):
        pass

class TPWPlotter(Plotter):
    def __init__(self):
        pass

class VorticityPlotter(Plotter):
    def __init__(self):
        pass