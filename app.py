import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

st.title("Gracie's Dallas Apartment Tour Map 🏙️")

# Sample data (you’ll replace this later)
data = {
    'Name': ['Apartment A', 'Apartment B'],
    'Latitude': [32.8005, 32.8012],
    'Longitude': [-96.8049, -96.8045],
    'Rent': ['$1600', '$1700'],
    'Sq Ft': [600, 650],
    'Tour Time': ['May 16, 2:15 PM', 'May 16, 3:00 PM'],
    'Notes': ['Nice view', 'Close to gym']
}

df = pd.DataFrame(data)

m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=15)
marker_cluster = MarkerCluster().add_to(m)

for _, row in df.iterrows():
    html = f"""
    <b>Name:</b> {row['Name']}<br>
    <b>Rent:</b> {row['Rent']}<br>
    <b>Sq Ft:</b> {row['Sq Ft']}<br>
    <b>Tour:</b> {row['Tour Time']}<br>
    <b>Notes:</b> {row['Notes']}
    """
    popup = folium.Popup(folium.IFrame(html, width=250, height=150), max_width=300)
    folium.Marker(
        location=(row['Latitude'], row['Longitude']),
        popup=popup,
        tooltip=row['Name']
    ).add_to(marker_cluster)

st_data = st_folium(m, width=700, height=500)
