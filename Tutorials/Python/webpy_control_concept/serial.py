#!/usr/bin/python

# Read from serial with data coming from RFM12PI with RFM12_Demo sketch 
# All Emoncms code is released under the GNU Affero General Public License.

import serial, sys, string

# Set this to the serial port of your emontx and baud rate, 9600 is standard emontx baud rate
ser = serial.Serial('/dev/ttyUSB0', 9600)

while 1:

  # Read in line of readings from emontx serial
  linestr = ser.readline()

  # Remove the new line at the end
  linestr = linestr.rstrip()

  print "DATA RX:"+linestr
