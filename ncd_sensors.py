import random

interval = 0
batteryLevel = 3.3
transmitCounter = 0
nodeID = 0
firmwareVersion = 1

def convert16Bit(variable, packet):
    packet.append(int((int(variable)>>8)&255))
    packet.append(int(int(int(variable)&255)))

def convert24Bit(variable, packet):
    packet.append((int(variable)>>16)&255)
    packet.append((int(variable)>>8)&255)
    packet.append(int(variable&255))

def convert32Bit(variable, packet):
    packet.append((int(variable)>>24)&255)
    packet.append((int(variable)>>16)&255)
    packet.append((int(variable)>>8)&255)
    packet.append(int(variable&255))

def getSensorPacket(sensorType):
    sensorPacket = []
    global transmitCounter
    global batteryLevel
    global nodeID
    global firmwareVersion

    if transmitCounter < 255:
        transmitCounter +=1
    else:
        transmitCounter = 1

    if batteryLevel > 2.7:
        batteryLevel -=0.1
    else:
        batteryLevel = 3.3

    sensorPacket = [127, nodeID, firmwareVersion, int((int(batteryLevel/0.00322))>>8), int((int(batteryLevel/0.00322))&255),transmitCounter, int(sensorType>>8), int(sensorType&255), 0]

    if sensorType == 1:
        # Temperature Humidity
        convert16Bit(int((random.uniform(-40.0, 85.00))*100.00), sensorPacket)#temperature
        convert16Bit(int((random.uniform(0.00, 100.00))*100.00), sensorPacket)#humidity
        return sensorPacket

    if sensorType == 2:
        sensorPacket.append(random.random(0,1))#input 1
        sensorPacket.append(random.random(0,1))#input 2
        return sensorPacket

    if sensorType == 3:
        convert16Bit(random.random(0,65535), sensorPacket)#input 1
        convert16Bit(random.random(0,65535), sensorPacket)#input 2
        return sensorPacket

    if sensorType == 4:
        convert16Bit(int(random.uniform(-40.0, 85.00)*100.00), sensorPacket)#temperature
        return sensorPacket

    if sensorType == 5:
        min = -1000.00
        max = 1000.00
        convert24Bit(int(random.uniform(min,max)*100.00), sensorPacket)#accel_x
        convert24Bit(int(random.uniform(min,max)*100.00), sensorPacket)#accel_y
        convert24Bit(int(random.uniform(min,max)*100.00), sensorPacket)#accel_z
        convert24Bit(int(random.uniform(min,max)*100.00), sensorPacket)#magneto_x
        convert24Bit(int(random.uniform(min,max)*100.00), sensorPacket)#magneto_y
        convert24Bit(int(random.uniform(min,max)*100.00), sensorPacket)#magneto_z
        convert24Bit(int(random.uniform(min,max)*100.00), sensorPacket)#gyro_x
        convert24Bit(int(random.uniform(min,max)*100.00), sensorPacket)#gyro_y
        convert24Bit(int(random.uniform(min,max)*100.00), sensorPacket)#gyro_z
        convert16Bit(random.random(0,85), sensorPacket)#temperature
        return sensorPacket

    if sensorType == 6:
        convert16Bit(random.random(0,85), sensorPacket)#temperature
        convert16Bit(int((random.uniform(-1000,1000))*1000.00), sensorPacket)#absolute_pressure
        convert16Bit(int((random.uniform(-1000,1000))*1000.00), sensorPacket)#relative_pressure
        convert16Bit(int((random.uniform(-1000,1000))*1000.00), sensorPacket)#altitude_change

    if sensorType == 40:
        min = -100.00
        max = 100.00
        convert16Bit(int((random.uniform(min,max))*100.00), sensorPacket)#rms_x
        convert16Bit(int((random.uniform(min,max))*100.00), sensorPacket)#rms_y
        convert16Bit(int((random.uniform(min,max))*100.00), sensorPacket)#rms_z
        convert16Bit(int((random.uniform(min,max))*100.00), sensorPacket)#max_x
        convert16Bit(int((random.uniform(min,max))*100.00), sensorPacket)#max_y
        convert16Bit(int((random.uniform(min,max))*100.00), sensorPacket)#max_z
        convert16Bit(int((random.uniform(min,max))*100.00), sensorPacket)#min_x
        convert16Bit(int((random.uniform(min,max))*100.00), sensorPacket)#min_y
        convert16Bit(int((random.uniform(min,max))*100.00), sensorPacket)#min_z
        convert16Bit(int((random.uniform(0.00,85.00))), sensorPacket)#temperature

    if sensorType == 44:
        convert24Bit(int(random.uniform(300.00,2000.00)*100.00), sensorPacket)#co2
        convert16Bit(int((random.uniform(0.00, 100.00))*100.00), sensorPacket)#humidity
        convert16Bit(int((random.uniform(-40.0, 85.00))*100.00), sensorPacket)#temperature
        return sensorPacket

    if sensorType == 53:
        convert32Bit((int(random.uniform(0.00,20.00)*100.00)), sensorPacket)#mass_concentration_pm_1_0
        convert32Bit((int(random.uniform(0.00,20.00)*100.00)), sensorPacket)#mass_concentration_pm_2_5
        convert32Bit((int(random.uniform(0.00,20.00)*100.00)), sensorPacket)#mass_concentration_pm_4_0
        convert32Bit((int(random.uniform(0.00,20.00)*100.00)), sensorPacket)#mass_concentration_pm_10_0
        convert32Bit((int(random.uniform(0.00,20.00)*100.00)), sensorPacket)#number_concentration_pm_0_5
        convert32Bit((int(random.uniform(0.00,20.00)*100.00)), sensorPacket)#number_concentration_pm_1_0
        convert32Bit((int(random.uniform(0.00,20.00)*100.00)), sensorPacket)#number_concentration_pm_2_5
        convert32Bit((int(random.uniform(0.00,20.00)*100.00)), sensorPacket)#number_concentration_pm_4_0
        convert32Bit((int(random.uniform(0.00,20.00)*100.00)), sensorPacket)#number_concentration_pm_10_0
        convert32Bit((int(random.uniform(0.00,20.00)*100.00)), sensorPacket)#typical_particle_size
        convert16Bit((int(random.uniform(0.00, 100.00)*100.00)), sensorPacket)#humidity
        convert16Bit((int(random.uniform(-40.0, 85.00)*100.00)), sensorPacket)#temperature
        convert24Bit((int(random.uniform(0.00,20.00)*100.00)), sensorPacket)#co2
        return sensorPacket
