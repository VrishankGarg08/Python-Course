class Vehicle:
    def __init__(self, Company, Top_Speed):
        self.Company = Company
        self.Top_Speed = Top_Speed
    def Show_Detail(self):
        print("Company:", self.Company)
        print("Max Speed:", self.Top_Speed, "Km/h")
class Car(Vehicle):
    def __init__(self, Model,Seats,Company,Top_Speed):
        self.Model = Model
        self.Seats = Seats
        super().__init__(Company, Top_Speed)
    def Show_Detail(self):
        super().Show_Detail()
        print("Seats:", self.Seats)
        print("Model:", self.Model)
    def Fuel_Type(self,Energy_Moving_Resource):
        print(self.Model, "Uses",Energy_Moving_Resource)

M4_COMPETITION =Car("M4_COMPETITION",6,"BMW",240)
M4_COMPETITION.Show_Detail()
M4_COMPETITION.Fuel_Type("Electric Energy(Battery System)")
print("Is Car(M4_COMPETITION) a Child Class of Vehicle a Parent Class ? :", issubclass(Car, Vehicle))
