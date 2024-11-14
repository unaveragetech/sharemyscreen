#!/bin/bash

echo "Setting up the Screen Streaming Application environment..."

# Step 1: Check if Python and pip are installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 and rerun this script."
    exit
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed. Please install pip3 and rerun this script."
    exit
fi

# Step 2: Install required Python packages
echo "Installing required Python packages..."
pip3 install -r requirements.txt

# Step 3: Create necessary directories and files
echo "Setting up necessary files..."
touch verified_users.txt
touch unverified_users.txt

# Step 4: Generate documentation (README.md)
echo "Generating documentation..."

cat > README.md <<EOL
# Screen Streaming Application

This application allows users to stream their PC screen in real-time through a Streamlit web interface. It includes user authentication, settings management, and adjustable screen streaming.

## How to Use
### Registration
- Users register with email, username, and password.
- To verify, manually add usernames to \`verified_users.txt\`.

### Starting the Application
- Run:
  \`\`\`
  streamlit run app.py
  \`\`\`

## Dependencies
- **Streamlit**
- **Werkzeug**
- **PyAutoGUI**
- **OpenCV**
EOL

echo "Setup complete. Run the application with: streamlit run app.py"
