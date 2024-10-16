#######################
# Import libraries
import streamlit as st
import pandas as pd
#import numpy as np
#import folium
#from streamlit_folium import st_folium
#import altair as alt
#import plotly.express as px
#import matplotlib.pyplot as plt

#######################
# Page configuration

st.set_page_config(
    page_title="World Cities Population Dashboard",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded")

#######################
# CSS styling
st.markdown("""
<style>

[data-testid="block-container"] {
    padding-left: 2rem;
    padding-right: 2rem;
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-bottom: -7rem;
}

[data-testid="stVerticalBlock"] {
    padding-left: 0rem;
    padding-right: 0rem;
}

</style>
""", 
unsafe_allow_html=True)



# Load data
df = pd.read_csv('./data/worldcities.csv')

# Sidebar
with st.sidebar:
    st.title('🏙️ World Cities Population Dashboard')
    
    country_list = list(df.country.unique())[::-1]
    
    selected_country = st.selectbox('Select a Country', country_list)
    df_selected_country = df[df.country == selected_country]
    df_selected_country_sorted = df_selected_country.sort_values(by="population", ascending=True)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)


# Set up the Streamlit app
st.title('OSM Map with World Cities')
df_mapping = df[['lat', 'lng']]
st.map(df_mapping)

# Create a Folium map centered at an average location (or any other location)
#m = folium.Map(location=[df['lat'].mean(), df['lng'].mean()], zoom_start=2)

# Add points to the map
#for i, row in df.iterrows():
    #folium.Marker([row['lat'], row['lng']], popup=row['city_ascii']).add_to(m)

# Display the map in Streamlit using streamlit-folium
#st_data = st_folium(m, width=700, height=500)
