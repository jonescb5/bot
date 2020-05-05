README for bot.py

Christopher Jones
EGRE347
04/30/20

Dependencies:
    driver.py
    image_processing.py
    motor.py

In the terminal on the Pi run the command
    "python3 bot.py"

*MAKE SURE TO RUN THE SCRIPT WITH PYTHON 3+

The script will prompt you to input the color of the
target that you want to go to:
    "What color target (R, G, or B)?  "

Enter the letter representing the color of the target: Red (R),
Green (G), or Blue (B). Make sure the letter is uppercase.
Press enter and the script will run.

To stop the script use the keyboard interrupt: Ctrl + C (^C)

The bot will search for the target matching the color input by the user
and when identified, go to the target.

Description:

    The code is compartmentalized into one main script (bot.py) and three modules, shown in Dependencies above.
The bot.py script runs the functions defined in driver.py as threads. The main script runs as the main thread and
it runs the vehicle_control function; A state machine which controls the movement of the bot based on position data
given to it by the daemon. The daemon thread runs in the background running the image_processing function. It
handles all of the image processing with openCV and passes the information about the targets to the vehicle_control
thread through a global variable. motor.py has the L298N class definition. This is provides more intuitive motor control
functions which are used in driver.py