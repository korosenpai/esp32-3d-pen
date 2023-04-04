# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()


print("\n") # separate logs from default messages of editor

from machine import Pin
from time import sleep
import sys
import _thread
from json import dumps

from funcs import *

#sys.exit()

btn = Pin(14, Pin.IN)
led = Pin(13, Pin.OUT)

############## get boot permissions ##############
debug_print("permissions to boot...", end = "")
if is_btn_pressed(btn):
    print_no()

    # flash leds
    blink_led(led, 0.1, 3)
    
    debug_print("cancelling boot...")
    sys.exit()
    
print_ok()

debug_print("starting up...")

starting_up = True
def blink_wait_loop_startup():
    global starting_up
    while starting_up:
        blink_led(led, 0.5, 1)
_thread.start_new_thread(blink_wait_loop_startup, ())


############## start mpu9250 ##############

from mpu import MPU9250

sda = Pin(22)
scl = Pin(21)

mpu9250 = MPU9250(sda, scl)

# start thread to update values
def update_mpu(mpu):
    while True:
        mpu.fusion_update()

        sleep(0.1)
_thread.start_new_thread(update_mpu, (mpu9250,)) # comma is to make it tuple


############## start server ##############


starting_up = False
while True:

    # send data from sensors
    temp_gyr =  mpu9250.gyro
    testdata = {
        "pitch": temp_gyr[0],
        "roll": temp_gyr[1],
        "heading": mpu9250.magn_heading,
    }

    print(dumps(testdata))
    sleep(0.1)

