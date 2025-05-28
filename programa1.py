import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [28.6353, -106.0889],
    columns=["lat", "lon"],
)
st.map(df)
