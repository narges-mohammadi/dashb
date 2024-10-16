#######################
# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
#import altair as alt
#import plotly.express as px
#import matplotlib.pyplot as plt

#######################
# Page configuration
'''
st.set_page_config(
    page_title="World Cities Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")


#######################
# Load data
df = pd.read_csv('./data/worldcities.csv')
'''



# Title of the dashboard
st.title('Basic Dashboard with Streamlit')

# Sidebar for user input
st.sidebar.header('User Input')

# Slider for user to select a range of data
number_of_points = st.sidebar.slider('Number of data points', 10, 1000, 100)

# Random Data
data = pd.DataFrame({
    'x': np.random.randn(number_of_points),
    'y': np.random.randn(number_of_points)
})

# Display Data
st.subheader('Randomly Generated Data')
st.write(data.head())

# Plotting the data
st.subheader('Scatter Plot')
fig, ax = plt.subplots()
ax.scatter(data['x'], data['y'], alpha=0.5)
st.pyplot(fig)

# Interactive elements: A checkbox
if st.sidebar.checkbox('Show Summary'):
    st.subheader('Data Summary')
    st.write(data.describe())



