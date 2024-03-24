import math
import keyboard
from pynput.mouse import Button, Controller as MouseController
import time

# Set the center point of the circle
center_x = 820
center_y = 448

# Set the radius of the circle
radius = 350

drawing = False  # Flag to indicate whether the circle is being drawn

def draw_circle():
    mouse = MouseController()
    
    # Calculate the points along the circle
    num_points = 100
    points = [(center_x + int(radius * math.cos(2 * math.pi / num_points * i)),
               center_y + int(radius * math.sin(2 * math.pi / num_points * i)))
              for i in range(num_points)]
    
    # Start drawing
    mouse.press(Button.left)
    
    # Move the cursor along the circle
    for point in points:
        mouse.position = point
        time.sleep(0.001)  # Adjust sleep time as needed for speed
        
        # Check if drawing is toggled off
        if not drawing:
            break
    
    # Stop drawing
    mouse.release(Button.left)

# Listen for the "]" key to toggle drawing
keyboard.add_hotkey("]", lambda: toggle_drawing())

def toggle_drawing():
    global drawing
    drawing = not drawing
    
    # Draw circle only if toggled on
    if drawing:
        draw_circle()
    else:
        # Reset the drawing state after completing one circle
        drawing = False

# Continuously check for mouse clicks and toggle drawing
while True:
    pass  # This loop will keep the program running until it's interrupted or closed
