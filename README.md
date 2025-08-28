# Invisibility Cloak using OpenCV

## How it Works
Capture background without cloak.
Convert each frame to HSV color space
Detect cloak color (red) using HSV ranges.
Replace cloak pixels with background.
Display final output in real-time.

## Run the Project

Install dependencies:
pip install opencv-python numpy

Run:
python cloak.py


## Controls:
ESC → Exit
b → Recapture background



## Example
Without cloak → background captured.
With red cloak → cloak disappears, background shows.
