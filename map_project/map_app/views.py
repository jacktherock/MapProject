from django.shortcuts import render
import json


def index(request):
    # Open the GeoJSON file containing village data
    with open("map_app/static/geojson/Pune_prj 1.geojson") as f:
        geojson_data = json.load(f)  # Load the GeoJSON data into a Python dictionary

    villages = []  # Initialize an empty list to store village names

    # Iterate through each feature in the GeoJSON data
    for feature in geojson_data["features"]:
        village = feature["properties"].get(
            "Village"
        )  # Get the village name from the properties, if it exists
        if village:  # Check if the village name is not None
            villages.append(village)  # Add the village name to the list

    villages = sorted(
        set(villages)
    )  # Remove duplicates and sort the list of village names

    # Render the index.html template with the list of villages and GeoJSON data
    return render(
        request,
        "index.html",
        {
            "villages": villages,
            "geojson_data": json.dumps(geojson_data),
        },  # Pass villages and geojson_data to the template
    )
