from flask import Flask, send_file, abort
import os

app = Flask(__name__)
current_directory = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_directory, "Icon_Emote_LOL.png")

@app.route('/api/icon/<filename>', methods=['GET'])
def get_icon(filename):
    """Serve the Icon_Emote_LOL.png file."""
    if filename == 'Icon_Emote_LOL.png':
        return send_file(icon_path, mimetype='image/png')
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
