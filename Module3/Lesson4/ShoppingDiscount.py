Valid = False
while not Valid :
    try:
        Bill_Amount ,Discount_Persentage ,People = input("Enter Bill Amount,Discount Persentage,People(Seperated by Commas(,)) : ").split(",")
        Bill_Amount = float(Bill_Amount)
        Discount_Persentage =float(Discount_Persentage)
        People = int(People)
        if Bill_Amount <= 0 or Discount_Persentage < 0 or People < 0:
            raise ValueError
        Discount_Amount = Bill_Amount * Discount_Persentage / 100
        Final_Amount = Bill_Amount - Discount_Amount
        Amount_Per_Person = Final_Amount / People
    except ValueError :
        print("Invalid Input! All Number Should be Positive. Enter Numbers Like : 1000 , 25 , 5 ")
    except ZeroDivisionError :
        print(f"Invalid Input! You Should Have Atleast 1 Person(Member) to may the Amount{Final_Amount}")
    else :
        print("------------------------------------------- SUMMARY -------------------------------------------")
        print("Original Amount :",Bill_Amount )
        print("Discount Persentage :", Discount_Persentage)
        print("Discount Amount :", Discount_Amount)
        print("Final Amount :", Final_Amount)
        print("Amount For Each Person :", Amount_Per_Person)
    finally :
        print("Thank You For Shopping .. Please Visit Again..")