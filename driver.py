import os
import ray
import zipfile
import numpy as np
from PIL import Image
import earthaccess as ea
from netCDF4 import Dataset
from processing import preprocessing
from utils import schemas, constants
from plotting import plots, colormaps
from processing.batching import batch_regrid, batch_resample, batch_plot 

def handler(event: dict):
    if (event["end"] - event["start"]).days > 5:
        raise ValueError(
            "Your time delta is too large. Reduce it to 5 days or less."
        )
    
    if "EARTHDATA_USERNAME" not in os.environ:
        os.environ["EARTHDATA_USERNAME"] = event["auth_user"]
    
    if "EARTHDATA_PASSWORD" not in os.environ:
        os.environ["EARTHDATA_PASSWORD"] = event["auth_pass"]

    ea.login()

    if event["category"] == "weather types":
        datasets = []
        for short_name in event["dataset"]:
            results = ea.search_data(
                short_name=short_name,
                temporal=(event["start"], event["end"])
            )
            path = short_name[-3:].lower()
            ea.download(results, local_path=path)

        asm_paths = sorted(os.listdir("asm"))
        flx_paths = sorted(os.listdir("flx"))
        slv_paths = sorted(os.listdir("slv"))

        for i in range(len((asm_paths))):
            datasets.append({
                "asm": Dataset(asm_paths[i]),
                "flx": Dataset(flx_paths[i]),
                "slv": Dataset(slv_paths[i])
            })
    else:
        results = ea.search_data(
            short_name=event["dataset"],
            temporal=(event["start"], event["end"])
        )
        ea.download(results, local_path="data")

        datapaths = os.listdir("data")
        datasets  = [Dataset(datapath) for datapath in datapaths]

    preprocessed = []
    for dataset in datasets:
        match event["category"]:
            case "10m winds":
                dataset = preprocessing.preprocess_wind_data(dataset)
            case "weather types":
                dataset = preprocessing.preprocess_weather_types(dataset)
            case _:
                continue
        preprocessed.append(dataset)
