from flask import Flask, request, jsonify

app = Flask(__name__)

# Store locations in a list
locations = []

@app.route('/track', methods=['POST'])
def track():
    data = request.json
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    
    if latitude and longitude:
        locations.append({"latitude": latitude, "longitude": longitude})
        print(f"New location: {latitude}, {longitude}")
        return jsonify({"status": "success", "message": "Location received"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify(locations), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
