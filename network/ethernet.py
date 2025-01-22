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

    tad_data["PSS"]         = values[0] #in 1
    tad_data["HVSS"]        = values[1] #in 2
    tad_data["CAVLongCS"]   = values[2] #in 3
    tad_data["CAVLatCS"]    = values[3] #in 4
    tad_data["CAVV2XS"]     = values[4] #in 5

    tad_data["InstPF"]              = values[5] #in 6
    tad_data["WheelPF"]             = values[6] #in 7
    tad_data["RESSBattSOC"]         = values[7] #in 8
    tad_data["RESSBattAvgCellTemp"] = values[8] #in 9
    tad_data["EDUDriveTemp"]        = values[9] #in 10
    tad_data["DrvMode"]             = values[10] #in 11

    tad_data["APIndStat"]           = values[11] #in 12
    tad_data["TrafficLightState"]   = values[12] #in 13
    tad_data["IntersectAct"]        = values[13] #in 14
    tad_data["DMSCtrlSw"]          = values[14] #in 15
    tad_data["BusVoltage"]          = values[15] #in 16
    tad_data["startup"]          = values[16] #in 17
    tad_data["EDUCtrl"]          = values[17] #in 18
    tad_data["TACstat"]          = values[18] #in 19
    tad_data["MCUcurrmode"]          = values[19] #in 20
    tad_data["MCUtorque"]          = values[20] #in 21


def send_tad_data(s: socket):
    b = struct.pack(
        'BBBBBBBBB', 
        tad_data["Regen"], #out 1
        tad_data["LongCtrl"], #out 2
        tad_data["LatCtrl"], #out 3
        tad_data["V2X"], #out 4
        tad_data["AutoP_Activate"], #out 5
        tad_data["AutoP_Start"], #out 6
        tad_data["AutoP_Cancel"], #out 7
        tad_data["AutoP_Finish"], #out 8
        tad_data["Cav_Dyno"], #out 9
    )
    
    s.sendto(b, (SPEEDGOAT_IP, SPEEDGOAT_PORT))