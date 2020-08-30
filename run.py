# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm

import pytesseract

# importing OpenCV
import cv2

from PIL import ImageGrab

import keyboard

import time

numConversion = {
	'zero': 0,
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9
}

def imToString():

	# Path of tesseract executable
	pytesseract.pytesseract.tesseract_cmd ='D:\\Programs\\TesseractOCR\\tesseract.exe'
	while(True):

		# ImageGrab-To capture the screen image in a loop.
		# Bbox used to capture a specific area.
		cap = ImageGrab.grab(bbox =(2003, 1156, 2550, 1212))
		cap = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)
		ret, cap = cv2.threshold(cap, 125, 255, cv2.THRESH_BINARY)
		cap = cv2.bitwise_not(cap)

		# Converted the image to monochrome for it to be easily
		# read by the OCR and obtained the output String.
		text = pytesseract.image_to_string(cap)
		nums = text.replace('\n', '').replace('\x0c', '').replace('o@', '').split(' ')
		print(nums)

		for num in nums:
			if num == '69':
				keyboard.write('And a good 420 to you sir.')
				keyboard.press("enter")
				time.sleep(10)

# Calling the function
imToString()
