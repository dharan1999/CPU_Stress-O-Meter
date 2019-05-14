import psutil
from boltiot import Bolt

API_KEY = "YOUR API KEY"
DEVICE_ID = "YOUR BOLT DEVICE NAME"

threshold_limit = 0.1
mybolt= Bolt(API_KEY, DEVICE_ID)


interval= 5

def green_led(pin, value):
    response = mybolt.digitalWrite(pin, value)

def red_led(pin, value):
    response = mybolt.digitalWrite(pin, value)

while True:
    cpu_usage = psutil.cpu_percent(interval = interval)
    print ("CPU USAGE is:-")
    if cpu_usage > threshold_limit:
        green_led('0','LOW')
        red_led('1', 'HIGH')
        red_led('2', 'LOW')
    else:
        green_led('0', 'HIGH')
        red_led('1', 'LOW')
