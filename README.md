# Face-Recognition Automator

This Python project uses facial recognition to automatically open a personalized set of Google Chrome tabs depending on who is in front of the camera. 

## Features

- **Facial Recognition**: Uses the `face_recognition` library and OpenCV to identify people from the webcam feed.
- **Personalized Workspaces**: Configures different URLs for different users.
- **Smart Tab Opening**: Uses AppleScript to check if target URLs are already open in Chrome, preventing duplicate tabs.
- **Real-Time Display**: Draws a bounding box around detected faces and displays their identified names.

## Prerequisites

- macOS (the script uses AppleScript to check Chrome tabs).
- Python 3.x
- Google Chrome installed.
- A webcam.

## Required Python Packages

Install the following packages using pip:

```bash
pip install face_recognition opencv-python numpy
```

*Note: `face_recognition` may require CMake and dlib to be installed on your system.*

## Setup

1. Clone or download the repository.
2. In the same directory as `main.py`, place your reference images. For the default code, you need:
   - `abhi.jpeg`
   - `adarsh.jpeg`
3. Modify the code if you want to use different names, images, or URLs. The variables to change are:
   - Image loading sections (`face_recognition.load_image_file()`)
   - `known_face_names` list
   - The URL lists in the `if` and `elif` blocks.

## Usage

Simply run the script from your terminal:

```bash
python3 main.py
```

The script will turn on your webcam, detect faces, and if a known face is matched, it will open their specific set of URLs in Google Chrome. If the URLs are already open, it will skip opening them again. The program will exit automatically once the tabs have been processed. You can also press `q` on your keyboard while focusing the video window to exit manually.