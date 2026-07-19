print("Library Visit Planner")
print("Answer 3 Questions and I will plan your Library visit!")
print("")
day=input("What Day is It?(MONDAY TO SUNDAY) :").upper()
weather=input("What Weather is It?(SUNNY/RAINY/CLOUDY) :").upper()
book=input("Is your book returned?(Yes/No)").upper()
if day=="MONDAY" or day=="TUESDAY" or day=="WEDNESDAY":
    print