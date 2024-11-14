import os
import subprocess
import pyautogui
import cv2
import numpy as np
import streamlit as st
from werkzeug.security import generate_password_hash, check_password_hash
import webbrowser

# File paths for storing user data
VERIFIED_USERS_FILE = "verified_users.txt"
UNVERIFIED_USERS_FILE = "unverified_users.txt"

# Initialize user files if they don't exist
for file_path in [VERIFIED_USERS_FILE, UNVERIFIED_USERS_FILE]:
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('')

# Check for headless environment and handle imports accordingly
try:
    SCREEN_CAPTURE_AVAILABLE = True
except Exception as e:
    st.warning("Screen capture is unavailable in a headless environment.")
    SCREEN_CAPTURE_AVAILABLE = False

# Helper functions
def save_user_info(username, email, password, file_path):
    """Save user credentials to a file"""
    with open(file_path, "a") as file:
        hashed_password = generate_password_hash(password)
        file.write(f"{username},{email},{hashed_password}\n")

def is_user_verified(username):
    """Check if a user is verified by searching the verified users file."""
    with open(VERIFIED_USERS_FILE, "r") as file:
        return any(line.split(",")[0] == username for line in file.readlines())

def capture_screen(fps, quality, grayscale):
    """Capture the screen at the specified FPS, quality, and color mode."""
    if SCREEN_CAPTURE_AVAILABLE:
        screenshot = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        if grayscale:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, buffer = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, quality])
    else:
        # Mock image for headless environments
        img = np.zeros((480, 640, 3), dtype=np.uint8)
        img[:] = (0, 0, 255)  # Red background as a placeholder
        if grayscale:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, buffer = cv2.imencode('.jpg', img)
    return buffer.tobytes()

# Streamlit UI components
def streamlit_app():
    st.title("Screen Streaming Application")

    # Registration and Login System
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    # Registration Page
    def register():
        st.header("Sign Up")
        email = st.text_input("Email")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Sign Up"):
            save_user_info(username, email, password, UNVERIFIED_USERS_FILE)
            st.success("Registration successful. Please wait for verification.")
            
            # Link to request verification
            st.markdown("If you want to request verification, please fill out [this form](https://formsubmit.co/el/sumuhu).")
            
            # Button to open verification request link in a new tab
            if st.button("Request Verification"):
                webbrowser.open("https://formsubmit.co/el/sumuhu")

            # Embedded HTML form for direct request submission
            st.markdown("""
            <h2>Request Verification</h2>
            <form target="_blank" action="https://formsubmit.co/cyberslueth@consultant.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <div class="form-group">
                    <input type="text" name="name" class="form-control" placeholder="Full Name" required><br>
                    <input type="email" name="email" class="form-control" placeholder="Email Address" required><br>
                    <textarea placeholder="Why do you want access to view my screen?" class="form-control" name="message" rows="5" required></textarea><br>
                    <button type="submit" class="btn btn-lg btn-dark btn-block">Submit Request</button>
                </div>
            </form>
            """, unsafe_allow_html=True)

    # Login Page
    def login():
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Log In"):
            with open(UNVERIFIED_USERS_FILE, "r") as file:
                for line in file.readlines():
                    registered_username, _, hashed_password = line.strip().split(',')
                    if username == registered_username and check_password_hash(hashed_password, password):
                        if is_user_verified(username):
                            st.session_state['logged_in'] = True
                            st.session_state['username'] = username
                            st.success(f"Welcome back, {username}!")
                        else:
                            st.error("User not verified. Please request verification.")
                    else:
                        st.error("Invalid username or password.")

    # Settings Page
    def settings():
        st.header("Settings")
        fps = st.slider("Frames per Second (FPS)", min_value=1, max_value=60, value=10)
        quality = st.slider("Screen Quality (JPEG Compression)", min_value=10, max_value=100, value=70)
        grayscale = st.checkbox("Grayscale Mode", value=False)
        custom_message = st.text_input("Custom Message on Stream", "Streaming Live")
        
        # Store settings in session state
        st.session_state['fps'] = fps
        st.session_state['quality'] = quality
        st.session_state['grayscale'] = grayscale
        st.session_state['custom_message'] = custom_message
        
        st.success("Settings saved successfully.")

    # Screen Stream Page
    def stream():
        st.header("Screen Stream")
        fps = st.session_state.get('fps', 10)
        quality = st.session_state.get('quality', 70)
        grayscale = st.session_state.get('grayscale', False)
        custom_message = st.session_state.get('custom_message', "Streaming Live")
        
        st.write(f"Streaming at {fps} FPS with quality {quality}%")
        st.write(custom_message)
        
        frame_placeholder = st.empty()
        while st.session_state['logged_in']:
            frame_placeholder.image(
                capture_screen(fps, quality, grayscale),
                channels="BGR" if not grayscale else "GRAY",
                use_container_width=True  # Updated to `use_container_width`
            )

    # Navigation based on login status
    if st.session_state['logged_in']:
        st.sidebar.title("Menu")
        choice = st.sidebar.radio("Navigation", ["Settings", "Screen Stream", "Log Out"])
        if choice == "Settings":
            settings()
        elif choice == "Screen Stream":
            stream()
        elif choice == "Log Out":
            st.session_state['logged_in'] = False
            st.session_state['username'] = None
            st.info("Logged out successfully.")
    else:
        action = st.sidebar.radio("Navigation", ["Login", "Register"])
        if action == "Login":
            login()
        elif action == "Register":
            register()

# Run the Streamlit app
if __name__ == "__main__":
    streamlit_app()
