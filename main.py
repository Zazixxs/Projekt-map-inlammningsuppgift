from flask import Flask, render_template, send_from_directory

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

# Endpoint for serving 'schools.csv'
@app.route('/csv/schools')
def serve_schools_csv():
    return send_from_directory('static', 'schools.csv')


if __name__ == "__main__":
    app.run(debug=True)
