import streamlit as st
from werkzeug.security import generate_password_hash, check_password_hash
import pyautogui
import cv2
import numpy as np
import os

# File paths for storing users
VERIFIED_USERS_FILE = "verified_users.txt"
UNVERIFIED_USERS_FILE = "unverified_users.txt"

# Initialize user files if they don't exist
for file_path in [VERIFIED_USERS_FILE, UNVERIFIED_USERS_FILE]:
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('')

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

def capture_screen(fps):
    """Capture the screen at the specified FPS."""
    screenshot = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    _, buffer = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 70])
    return buffer.tobytes()

# Streamlit UI components
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
                        st.error("User not verified. Please contact the administrator.")
                    return
        st.error("Invalid username or password.")

# Settings Page
def settings():
    st.header("Settings")
    fps = st.slider("Frames per Second (FPS)", min_value=1, max_value=60, value=10)
    st.session_state['fps'] = fps
    st.success(f"FPS set to {fps}")

# Screen Stream Page
def stream():
    st.header("Screen Stream")
    fps = st.session_state.get('fps', 10)
    st.write(f"Streaming at {fps} FPS.")
    frame_placeholder = st.empty()
    while st.session_state['logged_in']:
        frame_placeholder.image(capture_screen(fps), channels="BGR", use_column_width=True)

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