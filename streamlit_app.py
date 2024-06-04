import streamlit as st
from pathlib import Path

import pandas as pd
import numpy as np
import gdown


@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """
    
    url = "https://drive.google.com/uc?id=1t_7rVTR7iLV1aYOf4WiT66jgfPMSnLuy"
    output = "data/diaries_premier.csv"
    gdown.download(url, output, quiet=False)

    path = Path(__file__).parent/'data/diaries_premier.csv'
    ddf = pd.read_csv(path, index_col="id")

    return ddf



ddf = get_gdp_data()

st.dataframe(ddf, use_container_width=True)