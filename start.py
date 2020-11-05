from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 60
camera.start_preview()

while True:
    sleep(1)