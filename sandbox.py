import pandas as pd
import numpy as np



@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    path = Path(__file__).parent/'data/diaries_premier.csv'
    ddf = pd.read_csv(path, index_col="id")

    return ddf



ddf = get_gdp_data()

st.dataframe(ddf, use_container_width=True)