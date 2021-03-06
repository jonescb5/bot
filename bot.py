# ******************************************************************
# Program: bot.py
#
# Programmer: Christopher Jones
#
# Due Date: April 30, 2020
#
# EGRE 347, Spring 2020       Instructor: Robert Klenke
#
# Pledge: I have neither given nor received unauthorized aid on this program.
#
# Description: Main script. Runs a RPi based bot which targets a given color target.
#
# ******************************************************************
import time
import driver
import threading


res = (1280, 720)  # Set desired RPi camera resolution
frame_rate = 90  # Set desired RPi camera frame rate
centroid_x = -1  # Initialize x coordinate variable to the no-target state

# Prompt the user for the target color
target_color = input("What color target (R, G, or B)?  ")

# Initialize the image_processor function as a daemon thread which runs in the background updating the target
# position asynchronously. This thread is automatically killed when main is killed
im_proc = threading.Thread(target=driver.image_processor, args=target_color, daemon=True)

time.sleep(10)
# Start the image_processing thread
im_proc.start()

# Start the vehicle_control thread
# This is the main thread
driver.vehicle_control()

