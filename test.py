from __future__ import absolute_import
from __future__ import print_function, unicode_literals
from digi.xbee.devices import XBeeDevice
from ncd_sensors import getSensorPacket

import codecs
import os
import sys
import threading
import glob
import time

import serial

from serial.tools.list_ports import comports
from serial.tools import hexlify_codec

port_array = {}
interval = 0
sensorType = 0

from pprint import pprint

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/cu[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/cu.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

print(" +------------------+")
print(" | NCD Sensor Spoof |")
print(" +------------------+\n")

print('Scanning for Serial Ports')
print('Please wait for the scan to complete')
print('Serial Port Options:')

for serial_port in serial_ports():
    sp_key = len(port_array)+1
    port_array.update({str(sp_key): serial_port})

for serial_port in port_array:
    print('[' + serial_port + ']: ' + port_array.get(serial_port))
print('')
target_port_key = input('Please enter the number of the desired Serial Port above: ')
port = port_array.get(target_port_key)

#instanciate object to communicate through
device = XBeeDevice(port, 115200)
try:
    device.open()
except:
    print('Failed to communicate with modem')
    exit(1)

interval = int(input('Enter desired Transmit Interval(in seconds)'))
sensorType = int(input('Enter desired Sensor Type(number)'))

def transmit():
    global interval
    global sensorType
    threading.Timer(interval, transmit).start()
    commandBytes = bytearray(map(int, getSensorPacket(sensorType)))
    device.send_data_broadcast(commandBytes)
    print('Transmit')

transmit()
