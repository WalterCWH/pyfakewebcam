import pyfakewebcam
import numpy as np
import time
import cv2
import sys

cam = pyfakewebcam.FakeWebcam(sys.argv[1], 1280, 720)

cam.print_capabilities()

jpeg_frame = cv2.imread('doge1.jpg')

while True:
    cam.schedule_frame_jpeg(jpeg_frame)
    time.sleep(1/60)
