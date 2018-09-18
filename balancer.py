#!/usr/bin/env python
############################
# Balancer robot main communication controller
# Author: Angel Hernandez
############################

import time
import serial

print "Balancer Serial test"

ser = serial.Serial(
  
   port='/dev/serial0',
   baudrate = 115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
counter=0

ser.flush()

while 1:
   command = input ("Type something to send: ")
   ser.write(str(command))
   
   bytesToRead = ser.inWaiting()
   print "I have " + str(bytesToRead) + " bytes to read"
   received = ser.read(bytesToRead)
   print "Here it is: " + str(received)
