from abc import ABC, abstractmethod
class SmartDevice(ABC):
    def Show_Device(self, Name):
        self.Name = Name
        print("Device Name:", Name)
    @abstractmethod
    def turn_on(self):
        pass
class SmartLight(SmartDevice):
    def turn_on(self):
        print("Smart Light is now in WORKING")
 
class SmartFan(SmartDevice):
    def turn_on(self):
        print("Smart Fan is now in WORKING")
 
class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Smart Speaker is now in WORKING")

Light = SmartLight()
Fan = SmartFan()
Speaker = SmartSpeaker()
Light.Show_Device("Living Room Light")
Light.turn_on()
Fan.Show_Device("Bedroom Fan")
Fan.turn_on()
Speaker.Show_Device("Musical Speaker")
Speaker.turn_on()

class SecurityCamera:
    def check_status(self):
        print("Security Camera is Recording")
class DoorLock:
    def check_status(self):
        print("Doors are Locked Safely")
Devices = [SecurityCamera(), DoorLock()]
print("===== SMART DEVICE STATUS =====")
for Device in Devices:
    Device.check_status()