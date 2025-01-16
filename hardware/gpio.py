from gpiozero import LED, Button
from datetime import datetime

#----------------------------------------------

#ISP bindings
ind_PSC = LED(5)
ind_HV = LED(6)
ind_LongCtrl =LED(13)
ind_LatCtrl = LED(19)
ind_V2X = LED(26)

sw_Regen = Button(12)
sw_LongCtrl = Button(16)
sw_LatCtrl = Button(20)
sw_V2X = Button(21)

#----------------------------------------------

def getSwitchData():
    return [sw_Regen.is_pressed, 
            sw_LongCtrl.is_pressed, 
            sw_LatCtrl.is_pressed, 
            sw_V2X.is_pressed]

def setIndicatorStatus(i, status):
    if status == 0:
        i.off()
    elif status == 1:
        i.on()
    elif status == 2:
        #blink at 1Hz
        if datetime.now().second % 2 == 0:
            i.on()
        else:
            i.off()
            
def refreshIndicatorPanel(switch_data):
    setIndicatorStatus(ind_PSC,       switch_data[0])
    setIndicatorStatus(ind_HV,        switch_data[1])
    setIndicatorStatus(ind_LongCtrl,  switch_data[2])
    setIndicatorStatus(ind_LatCtrl,   switch_data[3])
    setIndicatorStatus(ind_V2X,       switch_data[4])
    
def testIndicatorsSwitches():
    setIndicatorStatus(ind_PSC,       sw_Regen.is_pressed)
    setIndicatorStatus(ind_LongCtrl,  sw_LongCtrl.is_pressed)
    setIndicatorStatus(ind_LatCtrl,   sw_LatCtrl.is_pressed)
    setIndicatorStatus(ind_V2X,       sw_V2X.is_pressed)