from collections import defaultdict

#----------------------------------------------

tad_data = {
    # Inputs from Speedgoat
    "PSS":                  0,
    "HVSS":                 0,
    "CAVLongCS":            0,
    "CAVLatCS":             0,
    "CAVV2XS":              0,
    "InstPF":               0.0,
    "WheelPF":              0,
    "RESSBattSOC":          0.0,
    "RESSBattAvgCellTemp":  0.0,
    "EDUDriveTemp":         0.0,
    "DrvMode":              0,
    "APIndStat":            0,
    "TrafficLightState":    0,
    "IntersectAct":         0,
    "DMSCtrlSw":            0,

    # New fields from Speedgoat (v.4)
    "ctrlswBool":           0,
    "BusVoltage":           0.0,
    "startup":              0,
    "EDUCtrl":              0,
    "TACstat":              0,
    "MCUcurrmode":          0,
    "MCUtorque":            0.0,

    # New fields from Speedgoat (v.5)
    "MILReq":               0,
    "MILARC":               0,
    "FCM":                  0,
    "LRR":                  0,
    "SRR_FR":               0,
    "SRR_LF":               0,
    "CAV_EBCM":             0,
    "CAV_EPS":              0,
    "CAV_PSC":              0,
    "CAV_Cohda":            0,
    "CSC_ADAS":             0,
    "C-ACC_Mileage":        0,
    "C-ACC_System":         0,
    "Lead_Distance":        0.0,
    "Lead_count":           0,
    "UDP_data":             0,
    "Dyno_Mode":            0,
    "Object_Injection":     0,
    "Lead_Headway":         0.0,



    # Outputs to Speedgoat
    "Regen":        0,
    "LongCtrl":     0,
    "LatCtrl":      0,
    "V2X":          0,
    "APActivate":   0,
    "APStart":      0,
    "APCancel":     0,
    "APFinish":     0
}

def map_WheelPF(packed):
    wheels = ["FL", "FR", "RL", "RR"]
    out_str = ""
    for i in range(0, 4):
        if packed % 2 == 1: out_str = wheels[3-i] + " " + out_str
        else: out_str = "-- " + out_str
        packed /= 2
    return out_str[:-1]

map_DrvMode = defaultdict(lambda : "Error")
map_DrvMode[0] = "Normal"
map_DrvMode[1] = "One-Pedal"
map_DrvMode[2] = "Performance"
map_DrvMode[3] = "Regen Paddle"

map_APIndStat = defaultdict(lambda : "Error")
map_APIndStat[0] = "Searching"
map_APIndStat[1] = "Error"
map_APIndStat[2] = "Ready"
map_APIndStat[3] = "In-Progress"
map_APIndStat[4] = "Complete"

map_TrafficLightState = defaultdict(lambda : "Error")
map_TrafficLightState[0] = "None Detected"
map_TrafficLightState[1] = "Red Next"
map_TrafficLightState[2] = "Yellow Next"
map_TrafficLightState[3] = "Green Next"

map_IntersectAct = defaultdict(lambda : "Error")
map_IntersectAct[0] = "Straight"
map_IntersectAct[1] = "Stop"
map_IntersectAct[2] = "Left"
map_IntersectAct[2] = "Right"

map_DMSCtrlSw = defaultdict(lambda : "Error")
map_DMSCtrlSw[0] = "Off"
map_DMSCtrlSw[1] = "On"


map_MCUcurrmode = defaultdict(lambda : "Error")
map_MCUcurrmode[0] = "Initilaization"
map_MCUcurrmode[1] = "LV Ready"
map_MCUcurrmode[2] = "Standby - ASC"
map_MCUcurrmode[3] = "Reserved"
map_MCUcurrmode[4] = "Torque Mode"
map_MCUcurrmode[5] = "Speed Control"
map_MCUcurrmode[6] = "Reserved"
map_MCUcurrmode[7] = "Internal Inverter Error"
map_MCUcurrmode[8] = "Reserved"
map_MCUcurrmode[9] = "Service Job"
# All the other ones are suppose to be explain!!!!
# Values from A to F ?????

#----------------------------------------------

def getIndicatorPanelValues():
    return [
        tad_data["PSS"], 
        tad_data["HVSS"], 
        tad_data["CAVLongCS"], 
        tad_data["CAVLatCS"], 
        tad_data["CAVV2XS"],
        tad_data["BusVoltage"],
    ]

def updateSwitchData(switch_val):
    tad_data["Regen"]       = switch_val[0]
    tad_data["LongCtrl"]    = switch_val[1]
    tad_data["LatCtrl"]     = switch_val[2]
    tad_data["V2X"]         = switch_val[3]

def updateButtonData(button_name):
    # Toggle the boolean (True/False) for button press
    tad_data[button_name] = not tad_data[button_name]