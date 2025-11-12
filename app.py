import os
import datetime
import numpy as np
import pandas as pd
import streamlit as st
import earthaccess as ea
import cartopy.crs as ccrs
from yaml import safe_load
from memray import Tracker
from driver import handler
from utils.constants import MIN_DATE, MAX_DATE, VIEWS


st.set_page_config(
    page_title="Numbus",
    page_icon="🌎"
)

st.title("Nimbus")
st.markdown("Visualizing Earth systems")

form = st.form("job-form")

with form:
    with open("observations.yml", "r") as f:
        datasets = safe_load(f)

    dataset = st.selectbox(
        "Choose a dataset",
        datasets.keys()
    )

    st.info(
        "The maximum time delta between start and end dates is 5 days."
    )

    # minimum one day time delta between start and end dates
    offset = datetime.timedelta(days=1)
    
    start = st.date_input(
        "Start date",
        min_value=MIN_DATE,
        max_value=(MAX_DATE - offset)
    )

    end = st.date_input(
        "End date",
        min_value=(MIN_DATE + offset),
        max_value=MAX_DATE
    )

    view = st.selectbox(
        "Choose a view",
        VIEWS.keys()
    )

    zipimg  = st.checkbox("Zip frames")
    video   = st.checkbox("Render video")
    metrics = st.checkbox("Show metrics")
    interp  = st.checkbox("Interpolate frames")
    summary = st.checkbox("Summarize metrics")

    auth_msg = st.info(
        "If your EarthData credentials are not set as environment variables, enter them below. " \
        "Otherwise, leave these following fields blank."
    )

    auth_user = st.text_input(
        "Enter your EarthData username"
    )
    auth_pass = st.text_input(
        "Enter your EarthData password",
        type="password"
    )

    submitted = st.form_submit_button("Submit")

if submitted:
    event = {
        "category": dataset,
        "dataset": datasets[dataset]["short name"],
        "start": start,
        "end": end,
        "zipimg": zipimg,
        "video": video,
        "metrics": metrics,
        "interp": interp,
        "summary": summary,
        "auth_user": auth_user,
        "auth_pass": auth_pass
    }
    handler(event)