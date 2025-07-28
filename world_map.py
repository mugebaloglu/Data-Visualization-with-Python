import numpy as np  
import pandas as pd
import folium
import folium
import webbrowser

world_map = folium.Map()
world_map.save("world_map.html")
webbrowser.open("world_map.html")



#Question: Create a map of Mexico with a zoom level of 4.
mexico_latitude = 23.6345 
mexico_longitude = -102.5528
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=4)
mexico_map.save("mexico_map.html")
webbrowser.open("mexico_map.html")


# create a Cartodb dark_matter map of the world centered around Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Cartodb dark_matter')
world_map.save("world_map_dark.html")
webbrowser.open("world_map_dark.html")



# create a Cartodb positron map of the world centered around Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Cartodb positron')
world_map.save("Cartodb positron.html")
webbrowser.open("Cartodb positron.html")

