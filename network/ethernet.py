import struct
import socket

from data.tad_data import *

#----------------------------------------------

JETSON_IP       = '0.0.0.0'
JETSON_PORT     = 1234

SPEEDGOAT_IP    = '192.168.10.1'
SPEEDGOAT_PORT  = 1234

PACKET_SIZE     = 256

#----------------------------------------------

def start_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def connect_socket(s: socket):
    s.bind((JETSON_IP, JETSON_PORT))
    s.setblocking(0)

def get_tad_data(s: socket):
    data, addr = s.recvfrom(PACKET_SIZE)
    values = struct.unpack('<BBBBBdBdddBBBBBdBBBBd', data)
                            #012345678901234567891

    tad_data["PSS"]         = values[0]
    tad_data["HVSS"]        = values[1]
    tad_data["CAVLongCS"]   = values[2]
    tad_data["CAVLatCS"]    = values[3]
    tad_data["CAVV2XS"]     = values[4]

    tad_data["InstPF"]              = values[5]
    tad_data["WheelPF"]             = values[6]
    tad_data["RESSBattSOC"]         = values[7]
    tad_data["RESSBattAvgCellTemp"] = values[8]
    tad_data["EDUDriveTemp"]        = values[9]
    tad_data["DrvMode"]             = values[10]

    tad_data["APIndStat"]           = values[11]
    tad_data["TrafficLightState"]   = values[12]
    tad_data["IntersectAct"]        = values[13]
    tad_data["DMSCtrlSw"]          = values[14]
    tad_data["BusVoltage"]          = values[15]
    tad_data["startup"]          = values[16]
    tad_data["EDUCtrl"]          = values[17]
    tad_data["TACstat"]          = values[18]
    tad_data["MCUcurrmode"]          = values[19]
    tad_data["MCUtorque"]          = values[20]


def send_tad_data(s: socket):
    b = struct.pack(
        'BBBB', 
        tad_data["Regen"], 
        tad_data["LongCtrl"], 
        tad_data["LatCtrl"], 
        tad_data["V2X"]
    )
    
    s.sendto(b, (SPEEDGOAT_IP, SPEEDGOAT_PORT))