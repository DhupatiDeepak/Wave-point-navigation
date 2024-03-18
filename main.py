from djitellopy import Tello
import time
import os
import cv2

dir = 'C:/Users/dhupa/OneDrive/Desktop/DroneImg/wavepointproject'
os.chdir(dir)

drone = Tello()

drone.connect()

drone.streamon()

BatteryValue = drone.get_battery()
print("Battery percentage = ", BatteryValue)

Height = drone.get_attitude()
print=("height of drone:",Height)

drone.takeoff()

drone.send_rc_control(0, 40, 0, 0)
time.sleep(5)

drone.send_rc_control(0, 0, 0, 0)
time.sleep(1)
feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)

drone.send_rc_control(30, 0, 0, 0)
time.sleep(5)

drone.send_rc_control(0, 0, 0, 35)
time.sleep(1)
feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)

drone.send_rc_control(0, 0, 0, -35)
time.sleep(4)

drone.send_rc_control(-30, 0, 0, 0)
time.sleep(5)


feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)

drone.send_rc_control(0, 0, 0, 0)
time.sleep(4)

drone.send_rc_control(-30, 0, 0, 0)
time.sleep(5)

drone.send_rc_control(0, 0, 0, -35)
time.sleep(1)
feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)

drone.send_rc_control(0, 0, 0, 35)
time.sleep(1)

drone.send_rc_control(30, 0, 0, 0)
time.sleep(5)

drone.send_rc_control(0, 0, 0, 0)
time.sleep(1)
feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)

drone.send_rc_control(0, 30, 0, 0)
time.sleep(5)

drone.send_rc_control(0, 0, 0, 0)
time.sleep(1)
feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)

drone.send_rc_control(-30, 0, 0, 0)
time.sleep(5)

drone.send_rc_control(0, 0, 0, -35)
time.sleep(1)
feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)
drone.send_rc_control(0, 0, 0, 35)
time.sleep(1)

drone.send_rc_control(30, 0, 0, 0)
time.sleep(5)

drone.send_rc_control(0, 0, 0, 0)
time.sleep(1)
feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)

drone.send_rc_control(30, 0, 0, 0)
time.sleep(5)

drone.send_rc_control(0, 0, 0, 35)
time.sleep(1)
feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)
drone.send_rc_control(0, 0, 0, -35)
time.sleep(1)

drone.send_rc_control(-30, 0, 0, 0)
time.sleep(5)

drone.send_rc_control(0, 0, 0, 0)
time.sleep(1)
feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)


drone.send_rc_control(0, -40, 0, 0)
time.sleep(5)

drone.send_rc_control(0, 0, 0, 88)
time.sleep(1)
feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)

drone.send_rc_control(0, -30, 0, 0)
time.sleep(5)

drone.send_rc_control(0, 0, 0, 55)
time.sleep(1)
feed = drone.get_frame_read().frame
imgresize = cv2.resize(feed, (720, 480))
cv2.imwrite(f'{time.time()}.jpg', imgresize)
time.sleep(2)


drone.send_rc_control(0, 0, 0, -55)
time.sleep(1)


drone.land()


