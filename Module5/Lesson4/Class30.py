# PRIVATTE ATTRIBUTE: IS A VARIABLE INSIDE A CLASS THAT YOU WANT TO KEEP HIDDEN FROM THE OUTSIDE WORLD. YOU MAKE AN ATTTRIBUTE PRIVATE BY PUTTING __(2 UNDERSCORES(__)) BEFORE IT'S NAME.
# Encapsulation : Bundling data together with the methods that are allowed to change it so that nothing outside the class can modify it...
# EXAMPLE:
class BankAccount:
    def __init__(self,owner,balance,currency):
        self.owner = owner
        self.__balance = balance
        self.currency = currency
    def GetBalance(self):
        return(f"{self.owner} has a Balance of {self.__balance}{self.currency}")
    def SetBalance(self,Amount):
        if Amount < 0 :
            print("INVALID! INVALID ! BALANCE NOT FOUNDBALANCE NOT FOUND !!")
        else :
            self.__balance = Amount
            print("Balance Updated ")
ACCOUNT = BankAccount("Elon Musk",0.01,"$")
ACCOUNT.GetBalance()
print("Owner:",ACCOUNT.owner)
print("Balance:",ACCOUNT.GetBalance())