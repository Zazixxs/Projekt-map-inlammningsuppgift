from flask import Flask, jsonify, render_template, send_from_directory
import pandas as pd
from sklearn.cluster import KMeans


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/geojson/fuel')
def serve_fuel_geojson():
    return send_from_directory('static', 'fuel.geojson')

@app.route('/geojson/supermarket')
def serve_supermarket_geojson():
    return send_from_directory('static', 'supermarket.geojson')

@app.route('/api/schools')
def clustered_schools():
    data = pd.read_csv('static/school_locations.csv')
    kmeans = KMeans(n_clusters=5, random_state=0)
    data['cluster'] = kmeans.fit_predict(data[['ycoord', 'xcoord']])
    return jsonify(data.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)

