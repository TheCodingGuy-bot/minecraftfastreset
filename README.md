# minecraftfastreset
Start a new minecraft seed as soon as you save and to title with AI detection. 

<img width="1408" height="757" alt="Screenshot 2025-08-27 at 01 50 43" src="https://github.com/user-attachments/assets/38f22e9e-ec70-4a4e-8a28-f62e7d0a52f9" />

You save and quit, it detects the button, clicks them.

might add an option to delete previous world too

ocr can still be a thing

PROJECT COMPLETE AND WORKING ✅

Opencv finds the single player button and takes a screenshot every singular few seconds and searches it, once its confident it found it, we stop taking a lot of screenshot and just take one to click on singleplayer, one to click on create world, and one to click the final create world we need. There has to be a time.sleep for the last one because it takes some time for it to load in and if it takes a screenshot of a loading screen it might think the button is elsewhere.

Pillow and Pyautogui were used for screenshots and pressing buttons.

To run use:
```
python -m pip install --upgrade pip
pip install opencv-python 
pip install pillow
pip install pyautogui
pip install numpy

#INSTALL THE MAINFILES DIRECTORY

python3 main.py

#OR
#First create new world and use
python3 maindelete.py
#as it will delete your previous world
```


#DO NOT MOVE YOUR MOUSE DURING THE PROCESS OF IT CLICKING OR MOVING THE MOUSE, WHEN YOU SAVE AND QUIT TO TITLE MAKE SURE TO LET IT DO WHAT IT HAS TO. 

The program will tell you the confidence score of how confident it thinks it is that, that button is on the screen when you save and quit to title. When its confident enough it will start clicking and creating a new world for you. I am not responsible for any damages this program can cause. By downloading my file you accept all risks and establish you want to install it.
The three buttons are there to find and click and once it finds the first button theres no need for continous screenshot with while true

Main delete file will see when the singleplayer button is there and delete the current world, you just played and start a new one so you save on space.


Thank you for using this software.

