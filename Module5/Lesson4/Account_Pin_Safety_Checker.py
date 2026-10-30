class Account:
    def __init__(self,Owner,Pin):
        self.Owner = Owner
        self.__Pin = Pin
    def Show_Pin_Status(self):
        print("Account Owner:", self.Owner)
        print("PIN IS STORED WITH SECURITY !!")
    def Set_Pin(self, Updated_Pin):
        if len(Updated_Pin) == 4 :
            self.__Pin = Updated_Pin
            print("PIN updated successfully.")
        else:
            print("ERROR! ERROR! PIN must be exactly 4 digits.")
    def Check_pin(self, entered_pin):
        if entered_pin == self.__Pin:
            print("Access granted.")
        else:
            print("Access denied.")
    def __str__(self):
        return("Account holder: "+ self.Owner)

My_Account = Account("Elon Musk","1234")
print(My_Account)
My_Account.Show_Pin_Status()
My_Account.__Pin = ("9999")
print("Tried changing PIN directly from outside.")
My_Account.Check_pin("9999")
My_Account.Check_pin("1234")
My_Account.Set_Pin("12345")
My_Account.Set_Pin("9999")
My_Account.Check_pin("9999")