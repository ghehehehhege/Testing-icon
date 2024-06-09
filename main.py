from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)
icon_directory = os.path.dirname(os.path.abspath(__file__))

@app.route('/api/icon/<filename>', methods=['GET'])
def get_icon(filename):
    """Serve an individual icon by filename if it exists."""
    file_path = os.path.join(icon_directory, filename)
    if os.path.isfile(file_path) and filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
        return send_from_directory(icon_directory, filename)
    else:
        abort(404, description="Resource not found")

if __name__ == '__main__':
    app.run(debug=True)