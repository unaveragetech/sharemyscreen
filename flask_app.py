import threading
from flask import Flask
import subprocess

# Initialize Flask App
app = Flask(__name__)

# Flask route for serving the Streamlit app link
@app.route("/")
def serve_streamlit_app():
    return "Visit Streamlit app at: http://localhost:8501"

# Function to run Flask in the background
def run_flask():
    app.run(host='0.0.0.0', port=5000, threaded=True)

# Start Flask server in a separate thread
if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
