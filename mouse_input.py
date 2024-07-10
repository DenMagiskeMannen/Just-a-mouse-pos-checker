# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:13:35 2023

@author: teodo
"""

from pynput import mouse

yey=False

# Function to handle mouse movement events
def on_move(x, y):
    #print(f"Mouse moved to ({x}, {y})")
    pass

# Function to handle mouse click events
def on_click(x, y, button, pressed):
    action = "pressed" if pressed else "released"
    print(f"Mouse {button} {action} at ({x}, {y})")
  

# Create mouse listener objects
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)

# Start the mouse listener in a separate thread
mouse_listener.start()

# Keep the script running to continue listening for mouse events
try:
    while True:
        if yey== True:
            print("Yey")
        pass
except KeyboardInterrupt:
    # Stop the mouse listener when Ctrl+C is pressed
    mouse_listener.stop()
    
    
