class DailyMessage:
    def __init__(self):
        self.Message = ""
    def Get_Msg(self):
        self.Message = input("Enter a message: ")
    def Print_Msg(self):
        print("Message in uppercase:", self.Message.upper())
Daily_Text = DailyMessage()
Daily_Text.Get_Msg()
Daily_Text.Print_Msg()

class HelperSession:
    def __init__(self):
        print("Daily Data Helper Is Created With __INIT__")
    def __del__(self):
        print("Daily Data Helper Is Deleted With __DEL__")
def create_session():
    print("Making session..")
    New_Session = HelperSession()
    print("Session is ready...")
    return New_Session
print("")
print("Calling create_session() function...")
Session_Obj = create_session()
print("Program is still running...")
class PairFinder:
    def find_pair(self, Numbers, Target):
        Lookup = {}
        for Index, Number in enumerate(Numbers):
            Needed_Number = Target - Number
            if Needed_Number in Lookup:
                return (Lookup[Needed_Number], Index)
            Lookup[Number] = Index
        return None
Numbers = (10, 20, 30, 40, 50, 60, 70)
print("Find Index Value From Here :",Numbers)
Target_Value = int(input("Enter target sum to search: "))
Pair_Finder = PairFinder()
Result = Pair_Finder.find_pair(Numbers, Target_Value)
if Result is not None:
    print("index1=%f, index2=%f" % Result)
else:
    print("No matching pair found.")
del Session_Obj
print("Program End")
