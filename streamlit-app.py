#######################
# Import libraries
import streamlit as st
import pandas as pd
#import numpy as np
#import altair as alt
#import plotly.express as px
#import matplotlib.pyplot as plt

#######################
# Page configuration

st.set_page_config(
    page_title="World Cities Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")



# Load data
df = pd.read_csv('./data/worldcities.csv')