import time
import pyautogui
import PIL
import cv2
import numpy as np 
import os 



def createworldfinalized():
	print("Task completed succesfully, fast reseting")
	time.sleep(0.7)
	screenshot = pyautogui.screenshot()
	screenshot.save("createworldfinalized.png")  # save PIL image
	img = cv2.imread("createworldfinalized.png") # load with OpenCV

	template = cv2.imread("button3.png")

	# Convert to grayscale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

	# Template size
	w, h = template_gray.shape[::-1]

	# Match template
	result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

	# Get best match location
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	top_left = max_loc
	center_x = top_left[0] + w // 2
	center_y = top_left[1] + h // 2

	print(f"Button center at: ({center_x}, {center_y})")

	pyautogui.moveTo(center_x, center_y)
	pyautogui.click()	



def createworld():
	print("Deleting previous world")
	pyautogui.press('down')
	screenshot1 = pyautogui.screenshot()
	screenshot1.save("delete.png")  # save PIL image
	img = cv2.imread("delete.png") # load with OpenCV

	template = cv2.imread("del1.png")

	# Convert to grayscale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

	# Template size
	w, h = template_gray.shape[::-1]

	# Match template
	result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

	# Get best match location
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	top_left = max_loc
	center_x = top_left[0] + w // 2
	center_y = top_left[1] + h // 2

	print(f"Button center at: ({center_x}, {center_y})")

	pyautogui.moveTo(center_x, center_y)
	pyautogui.click()

	print("last delete world button")

	screenshot2 = pyautogui.screenshot()
	screenshot2.save("delete1.png")  # save PIL image
	img = cv2.imread("delete1.png") # load with OpenCV

	template = cv2.imread("del2.png")

	# Convert to grayscale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

	# Template size
	w, h = template_gray.shape[::-1]

	# Match template
	result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

	# Get best match location
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	top_left = max_loc
	center_x = top_left[0] + w // 2
	center_y = top_left[1] + h // 2

	print(f"Button center at: ({center_x}, {center_y})")

	pyautogui.moveTo(center_x, center_y)
	pyautogui.click()

	print("Task completed succesfully, fast reseting")
	screenshot = pyautogui.screenshot()
	screenshot.save("createworld.png")  # save PIL image
	img = cv2.imread("createworld.png") # load with OpenCV

	template = cv2.imread("button2.png")

	# Convert to grayscale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

	# Template size
	w, h = template_gray.shape[::-1]

	# Match template
	result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

	# Get best match location
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	top_left = max_loc
	center_x = top_left[0] + w // 2
	center_y = top_left[1] + h // 2

	print(f"Button center at: ({center_x}, {center_y})")

	pyautogui.moveTo(center_x, center_y)
	pyautogui.click()

	createworldfinalized()

def Singleplayer():
	#start when detected image appears
	print("Task completed succesfully, fast reseting")
	screenshot = pyautogui.screenshot()
	screenshot.save("Singleplayer.png")  # save PIL image
	img = cv2.imread("Singleplayer.png") # load with OpenCV


	# Convert to grayscale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

	# Template size
	w, h = template_gray.shape[::-1]

	# Match template
	result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

	# Get best match location
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	top_left = max_loc
	center_x = top_left[0] + w // 2
	center_y = top_left[1] + h // 2

	print(f"Button center at: ({center_x}, {center_y})")

	pyautogui.moveTo(center_x, center_y)
	pyautogui.click()

	createworld()






while True:
	screenshot = pyautogui.screenshot()
	screenshot.save("temp.png")  # save PIL image
	img = cv2.imread("temp.png") # load with OpenCV

	template = cv2.imread("button1.png")

	# Convert to grayscale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

	# Match template
	result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

	# Get the best match probability (max correlation value)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

	print(f"Match confidence: {max_val:.2f}")

	# Check if confidence is above 90%
	if max_val >= 0.9:
	    print("✅ Button is there!")
	    Singleplayer()
	




"""
If this doesnt go as planned im trying ocr
"""
