import os
from flask import Flask, render_template, send_from_directory, request
import pandas as pd
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

app = Flask(__name__)

# Path to the directory where the Excel file and generated HTML files are stored
DATA_DIR = os.path.join(app.static_folder, 'data')

# Function to get latitude and longitude from a city name
def geocode_city(city_name):
    geolocator = Nominatim(user_agent="bah_mapper", timeout=10)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    try:
        location = geocode(city_name)
        if location:
            return location.latitude, location.longitude
        else:
            print(f"Location not found for {city_name}")
    except Exception as e:
        print(f"Error geocoding {city_name}: {e}")
    return None, None

# Function to load or geocode data and save it
def load_or_geocode_data(sheet):
    csv_file = os.path.join(DATA_DIR, f'geocoded_data_{sheet}.csv')
    excel_file = os.path.join(DATA_DIR, '2024 BAH Rates.xlsx')

    if os.path.exists(csv_file):
        # Load the data from CSV
        bah_data = pd.read_csv(csv_file)
        print(f"Loaded geocoded data from {csv_file}")
    else:
        # Geocode the data
        bah_data = pd.read_excel(excel_file, sheet_name=sheet)
        bah_data['Latitude'], bah_data['Longitude'] = zip(*bah_data['MHA_NAME'].apply(geocode_city))

        # Save the geocoded data to CSV
        bah_data.to_csv(csv_file, index=False)
        print(f"Geocoded data saved to {csv_file}")

    return bah_data

# Function to create the map and save as HTML file
def create_map(sheet, pay_grade):
    # Load or geocode the data
    bah_data = load_or_geocode_data(sheet)

    # Initialize a Folium map centered around a specific location (e.g., center of the US)
    map_center = [39.8283, -98.5795]
    bah_map = folium.Map(location=map_center, zoom_start=5)

    # Add markers for each location in the BAH data
    marker_count = 0
    for index, row in bah_data.iterrows():
        if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']):
            location = [row['Latitude'], row['Longitude']]
            popup_text = f"Location: {row['MHA_NAME']}<br>BAH Rate ({pay_grade}): ${row[pay_grade]}"
            folium.Marker(location, popup=popup_text).add_to(bah_map)
            marker_count += 1
    print(f"Added {marker_count} markers to the map for sheet '{sheet}' and pay grade '{pay_grade}'")

    # Save the map to an HTML file
    output_file = os.path.join(DATA_DIR, f'bah_interactive_map_{sheet}_{pay_grade}.html')
    bah_map.save(output_file)
    print(f"Map has been created and saved as '{output_file}'")

# Route to serve the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to serve the generated HTML map files
@app.route('/maps/<path:filename>')
def serve_map(filename):
    return send_from_directory(DATA_DIR, filename)

# Route to generate and serve the requested map
@app.route('/generate_map', methods=['POST'])
def generate_map():
    sheet = request.form.get('sheet')
    pay_grade = request.form.get('pay_grade')
    create_map(sheet, pay_grade)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
