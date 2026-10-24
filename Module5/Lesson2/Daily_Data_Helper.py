class DailyMessage:
    def __init__(self):
        self.Message = ""
    def GetMessage(self):
       self.Message = input("Enter A Message: ")
    def print_Message(self):
        print(" Your Message in Uppercase:", self.Message.upper())

Daily_Text = DailyMessage()
Daily_Text.GetMessage()
Daily_Text.print_Message()
class HelperSession:
    def __init__(self):
        print("Daily Data Helper Session Created")
    def __del__(self):
        print("Daily Data Helper Session Deleted")

def create_session():
    print("Making HelperSession...")
    Session = HelperSession()
    print("Session is ready...")
    return Session
print("")
print("Calling create_session() function...")
Session_Obj = create_session()
print("Program is still running...")
class PairFinder:
    def find_pair(self,Numbers,target):
        lookup = {}
        for index, number in enumerate(Numbers):
            needed_number = target - number 
            if needed_number in lookup:
                return (lookup[needed_number], index)
            lookup[number] = index
        return None
Numbers = (10, 20, 30, 40, 50, 60, 70)
Target = int(input("Enter target sum to search: "))
Result = PairFinder().find_pair(Numbers, Target)
if Result is not None:
    print("index1=%d, index2=%d" % Result)
else:
    print("No matching pair found.")
del Session_Obj
print("Program End")