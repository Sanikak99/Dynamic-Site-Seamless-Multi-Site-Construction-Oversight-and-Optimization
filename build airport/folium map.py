import tkinter as tk
from tkinter import ttk
import folium
import pandas as pd
import os
from webbrowser import open as webopen

def generate_map():
    # Read the dataset containing latitude, longitude, and vehicle numbers
    df = pd.read_excel(r'''C:\Users\Sanika\Documents\InternshipRocktech\Dashbord Rocktech infrastructre (1) (1) (1).xlsx''')

    # Create a folium map centered at the first location
    map_center = folium.Map(location=[df['Latitude'].iloc[0], df['Longitude'].iloc[0]], zoom_start=10)

    # Filter out rows with missing latitude or longitude values
    df = df.dropna(subset=['Latitude', 'Longitude'])

    # Add markers for each location in the dataset
    for index, row in df.iterrows():
        # Change marker color here, 'blue' is an example
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['Vehicals (No.)'], icon=folium.Icon(color='orange')).add_to(map_center)

    # Save the map as an HTML file
    map_path = "map.html"
    map_center.save(map_path)

    # Open the map HTML file in the default web browser
    webopen("file:///" + os.path.abspath(map_path))

# Create a Tkinter window


# Call the generate_map function to generate the map immediately
generate_map()

