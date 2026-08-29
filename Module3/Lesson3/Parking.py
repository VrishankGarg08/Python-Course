def calculate_change(paid, price):
    change = paid - price
    return change
ticket_price = 30
print("===== PARKING TICKET PAYMENT HELPER =====")
print(f"This parking ticket costs {ticket_price} ")
print("Accepted coins: 1, 5, 10, 25")
coins_inserted = 0
total_inserted = 0

while True:
    coin = int(input("Insert a coin (1,2, 5, 10, or 25): "))
    if coin not in [1 ,2 ,5 ,10 ,25 ] :
        print("Invalid coim !!Please insert 1, 2, 5, 10, or 20 coin only .")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}")

    if total_inserted >= ticket_price:
        print("Enough money inserted!")
        break
change_due = calculate_change(total_inserted, ticket_price)
print("Printing your parking ticket...")
if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due}")
print("========================================= PAYMENT SUMMARY =================================================")
print("Ticket Price:", ticket_price)
print("Coins Inserted:", coins_inserted)
print("Total Paid:", total_inserted)
print("Change Given:", change_due)
print("===========================")
print("Parking ticket payment complete!")
