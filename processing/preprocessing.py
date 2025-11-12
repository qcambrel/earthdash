import numpy as np
from netCDF4 import Dataset

def preprocess_wind_data(dataset: Dataset) -> np.ndarray:
    """
    Preprocesses wind data from a netCDF4 dataset.

    Args:
        dataset (Dataset): The netCDF4 dataset containing wind data

    Returns:
        np.ndarray: The preprocessed wind data
    """
    uwnd = dataset.variables["uwnd"][0].data
    vwnd = dataset.variables["vwnd"][0].data
    fill = -9999.0
    u    = np.ma.masked_where(uwnd == fill, uwnd)
    v    = np.ma.masked_where(vwnd == fill, vwnd)
    w    = np.sqrt(u ** 2 + v ** 2)
    return w

def preprocess_weather_types(dataset: dict[str, Dataset]) -> tuple[np.ndarray, ...]:
    """
    Preprocesses weather type data from a netCDF4 dataset.

    Args:
        dataset (Dataset): The netCDF4 dataset containing weather type data

    Returns:
        np.ndarray: The preprocessed weather type data
    """
    data = {}
    asm  = dataset["asm"]
    flx  = dataset["flx"]
    slv  = dataset["slv"]

    wxtypes = ("PHIS", "PRECSNO", "PRECTOT", "T2M", "H1000", "H500", "SLP")

    for wxtype in wxtypes:
        if wxtype in asm.variables.keys():
            data[wxtype] = asm.variables[wxtype][0].data
        elif wxtype in flx.variables.keys():
            data[wxtype] = flx.variables[wxtype][0].data
        elif wxtype in slv.variables.keys():
            data[wxtype] = slv.variables[wxtype][0].data
    
    phis  = data["PHIS"]
    snow  = data["PRECSNO"]
    rain  = data["PRECTOT"]
    t2m   = data["T2M"]
    h1000 = data["H1000"]
    h500  = data["H500"]
    slp   = data["SLP"]

    scale_factors = {
        "PHIS": 1 / 9.81,
        "PRECSNO": 3600 / 25.4,
        "PRECTOT": 3600 / 25.4,
        "T2M": 1,
        "H1000": 1,
        "H500": 1,
        "SLP": 1 / 100
    }

    for wxtype in data:
        data[wxtype] *= scale_factors[wxtype]

    ice         = snow * 0
    frzr        = snow * 0
    thick       = h500 - h1000
    elev_factor = (phis - 305) / 915

    elev_factor[np.where(elev_factor < 0)] = 0.0
    elev_factor[np.where(elev_factor > 1)] = 1.0

    elev_factor = elev_factor * 100
    low         = 5400 + elev_factor

    ice[np.where((thick.any() >= low.any()) and (snow > 0))]  = snow[np.where((thick.any() >= low.any()) and (snow > 0))]
    snow[np.where((thick.any() >= low.any()) and (snow > 0))] = 0.0

    rain[np.where(snow >= 0.1)] = 0.0
    rain[np.where(ice >= 0.1)]  = 0.0

    return snow, ice, frzr, rain, t2m, slp