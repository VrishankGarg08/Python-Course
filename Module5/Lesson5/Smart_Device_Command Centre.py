from abc import ABC, abstractmethod
class SmartDevice(ABC):
    def show_device(self, name):
        self.name = name
        print("Device Name:", name)
    @abstractmethod
    def turn_on(self):
        pass
class SmartLight(SmartDevice):
    def turn_on(self):
        print("Light is now WORKING")
 
class SmartFan(SmartDevice):
    def turn_on(self):
        print("Fan is now WORKING")
 
class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Speaker is now WORKING")

Light = SmartLight()
Fan = SmartFan()
Speaker = SmartSpeaker()
Light.show_device("Living Room Light")
Light.turn_on()
Fan.show_device("Bedroom Fan")
Fan.turn_on()
Speaker.show_device("Musical Speaker")
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