# ShareMyScreen 📱💻

Welcome to **ShareMyScreen**, a web application that allows users to stream their computer screen in real-time to a web interface. The application also includes a user verification system, settings customization (like FPS adjustment), and the ability to request access to view screens from users who aren't yet verified. 

🚀 This app is designed for **streaming your screen securely** and allowing trusted individuals to watch your screen remotely.

---

## Table of Contents 📑

1. [Overview](#overview)
2. [Features ✨](#features)
3. [Setup Instructions 🛠️](#setup-instructions)
4. [User Flow](#user-flow)
5. [Technologies 🛠️](#technologies)
6. [Contributing 🤝](#contributing)
7. [License 📄](#license)

---

## Overview 👀

**ShareMyScreen** enables easy screen sharing by streaming your desktop directly to a web page. It also features a simple **user verification** process that ensures only authorized viewers can access the screen stream. With built-in settings, users can **customize their streaming experience**, including adjusting the **frames per second (FPS)** for the stream. The app is built with **Streamlit** for a clean, user-friendly interface.

- 🔒 **Verified Users Only:** Users need to request verification to stream their screen, and only verified users are allowed access.
- 🎥 **Live Streaming:** You can share your screen with live streaming to the web interface.
- ⚙️ **Custom Settings:** Set FPS for screen streaming to match your preferences or system capabilities.

---

## Features ✨

### 🖥️ **Screen Streaming**:
- Capture your desktop and stream it live to a web interface.
- **Adjustable FPS:** Customize the FPS to optimize performance based on your system's capabilities.

### 🔒 **User Verification System**:
- Users can **request verification** to gain access to screen streaming.
- **Email Verification**: New users can fill out a request form for verification.

### ⚙️ **Settings**:
- Easily adjust **FPS** using a slider for smooth streaming.
  
### 🔑 **Login & Registration**:
- **Register** with an email and password.
- **Login** securely with username and password.
- **Unverified users** are given a message to request access through the form.

### 📝 **Request Verification**:
- If you're not yet verified, you can easily submit a request by clicking a button to open a form or using the embedded form within the app.

---

## Setup Instructions 🛠️

### Prerequisites 🔑
Before you start, make sure you have the following tools installed:
- **Python** 3.7+ (Download from [python.org](https://www.python.org/downloads/))
- **Streamlit** (Install with `pip install streamlit`)
- **pyautogui** (Install with `pip install pyautogui`)
- **Werkzeug** (Install with `pip install werkzeug`)
- **OpenCV** (Install with `pip install opencv-python-headless`)

### Step-by-Step Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/unaveragetech/sharemyscreen.git
    cd sharemyscreen
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:

    Start the Streamlit app by running:

    ```bash
    streamlit run app.py
    ```

    This will open the app in your browser where you can sign up, log in, and start streaming your screen.

4. **Create the necessary files**:
    The app will create `verified_users.txt` and `unverified_users.txt` files when you first run it. Make sure these files are properly set up for the app to store users.

---

## User Flow

### Step 1: **Registration**
- Go to the registration page to sign up.
- Enter your email, username, and password to register an account.
- After registering, users must request verification by filling out a form (either manually or directly through an embedded form).

### Step 2: **Login**
- Once verified, you can log in using your username and password.
- If you're not verified yet, you'll see a message prompting you to request verification.

### Step 3: **Start Streaming**
- After logging in, you can begin streaming your screen.
- **Adjust FPS** settings in the settings menu to optimize streaming quality.

### Step 4: **Request Verification**
- If you're a new user, click the button to open a verification form in your browser or fill out the embedded form directly within the app.

---

## Technologies 🛠️

- **Streamlit**: For building the interactive web interface.
- **OpenCV**: For capturing the screen and compressing images for streaming.
- **pyautogui**: To capture the screen and handle screen input.
- **Werkzeug**: For securely handling passwords.

---

## Contributing 🤝

We welcome contributions to improve ShareMyScreen! If you have suggestions, improvements, or bug fixes, feel free to fork the repo and create a pull request.

### How to Contribute:
1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch: `git checkout -b feature-name`
4. Make your changes and commit them: `git commit -m 'Add new feature'`
5. Push to your branch: `git push origin feature-name`
6. Open a pull request with a detailed description of the changes.

---

## License 📄

This project is licensed under the **MIT License** - see the [LICENSE]((https://gist.github.com/unaveragetech/a29c048c8b1ccad062066507bf183d9e) file for details.

---

### 💬 **Support & Feedback**
If you need help or want to give feedback, feel free to open an issue or reach out directly through the GitHub discussions page.

---

