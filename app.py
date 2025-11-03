import os
import datetime
import numpy as np
import pandas as pd
import streamlit as st
import earthaccess as ea
import cartopy.crs as ccrs
from yaml import safe_load
from memray import Tracker

st.title("EarthDash")
st.markdown("A simple dashboard for visualizing Earth systems")