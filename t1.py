from djitellopy import Tello
import time

drone = Tello()
drone.connect()

battery_percentage = drone.get_battery()
print("Battery percentage =", battery_percentage)

drone.takeoff()
time.sleep(5)

# Perform a flip (forward flip)
drone.flip("f")
time.sleep(5)

# Rotate the drone 360 degrees (clockwise)
drone.send_rc_control(0, 0, 0, 30)
time.sleep(12)  # Adjust the sleep time based on the desired rotation speed

# Land the drone
drone.land()