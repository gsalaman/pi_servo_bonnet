from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16) 

while True:
  kit.servo[0].angle = 10
  time.sleep(1)
  kit.servo[0].angle = 90
  time.sleep(1)
  kit.servo[0].angle = 170
  time.sleep(1)
