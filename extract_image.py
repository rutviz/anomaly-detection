# Program To Read video 
# and Extract Frames 
import cv2 
import numpy
from matplotlib import pyplot as plt

# Function to extract frames 
def FrameCapture(path): 
	
	# Path to video file 
	vidObj = cv2.VideoCapture(path) 

	# Used as counter variable 
	count = 0

	# checks whether frames were extracted 
	success = 1
	image = numpy.ndarray(255)
	length = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
	fps    = vidObj.get(cv2.CAP_PROP_FPS)
	seconds = int(length/fps)
	success, image = vidObj.read() 


	# while success: 
	# 	vidObj.set(cv2.CAP_PROP_POS_MSEC,(count*10000)) 
	# 	if count == 45	:
	# 		cv2.imshow("snap",image)
	# 		cv2.waitKey(0)
	# 	count += 1
		
	print("Total frames: ",seconds)

if __name__ == '__main__': 
 
	FrameCapture("test.mp4") 
