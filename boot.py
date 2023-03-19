# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

print("\n") # separate logs from default messages of editor

from machine import Pin
import time
import sys
import _thread
import usocket as socket
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

connect_to_wifi("FASTWEB-B7135F", "34NNG8GFEZ")


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5) # max 5 socket connections // max possible should be 16

starting_up = False
while True:
    conn, addr = s.accept()

    # recieve data
    response = None
    request = str(conn.recv(1024))
    #print('Content = %s' % str(request))

    # parse data
    update = request.find("/getUpdate")

    if update == 6:
        # send data from sensors
        temp_gyr =  mpu9250.gyro
        testdata = {
            "pitch": temp_gyr[0],
            "roll": temp_gyr[1],
            "heading": mpu9250.magn_heading,
        }
        response = dumps(testdata)
        
    else:
        print_notification('Got a connection from %s' % str(addr)) # first time connection
        # send default webpage
        response = create_web_page()

    
    # Create a socket reply and close
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()


