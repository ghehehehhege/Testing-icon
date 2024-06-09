from flask import Flask, send_from_directory, abort, jsonify
import os

app = Flask(__name__)
icon_directory = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['GET'])
def forbidden():
    """Handle requests to the root URL and return 403 Forbidden."""
    return jsonify({"error": "Forbidden"}), 403

@app.route('/api/icon/<filename>', methods=['GET'])
def get_icon(filename):
    """Serve an individual icon by filename if it exists."""
    try:
        file_path = os.path.join(icon_directory, filename)
        if os.path.isfile(file_path) and filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
            return send_from_directory(icon_directory, filename)
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

