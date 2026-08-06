Num = int(input("Enter A Number :"))
N = int(input("Enter A Number to which u want to do the power :"))
print("Powers of ",Num)
for i in range(1,N+1):
    power= Num**i 
    print(Num," ^ ",i," = ", power)