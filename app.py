from flask import Flask, request, jsonify, render_template
from helper import save_data_to_csv

app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main HTML page from the templates folder."""
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    """Receives sensor data and a username, then saves it to a CSV file."""
    payload = request.json
    data = payload.get('data', [])
    username = payload.get('username')

    if not data:
        return jsonify({"error": "No data received"}), 400
    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        filename = save_data_to_csv(username, data)
        print(f"Data for user '{username}' saved successfully to {filename}")
        return jsonify({"message": "Data saved successfully", "filename": filename}), 201
    except Exception as e:
        print(f"Error saving data: {e}")
        return jsonify({"error": "Failed to save data on server"}), 500

if __name__ == '__main__':
    # For production, run this with a proper WSGI server like Gunicorn
    app.run(debug=True, host='0.0.0.0', port=8080)

