from flask import Flask, jsonify, render_template, send_from_directory
import pandas as pd
from sklearn.cluster import KMeans

# Setting up the Flask app
app = Flask(__name__)

# Route for the main page which will load the Leaflet map
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint for serving 'fuel.geojson'
@app.route('/geojson/fuel')
def serve_fuel_geojson():
    return send_from_directory('static', 'fuel.geojson')

# Endpoint for serving 'supermarket.geojson'
@app.route('/geojson/supermarket')
def serve_supermarket_geojson():
    return send_from_directory('static', 'supermarket.geojson')

# Endpoint for serving clustered school data
@app.route('/api/schools')
def clustered_schools():
    # Assuming the school locations CSV is stored under 'static/school_locations.csv'
    data = pd.read_csv('static/school_locations.csv')
    # Assume that the relevant columns are named 'ycoord' and 'xcoord'
    kmeans = KMeans(n_clusters=5, random_state=0)
    data['cluster'] = kmeans.fit_predict(data[['ycoord', 'xcoord']])
    
    # Convert clustered data to JSON
    return jsonify(data.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)

