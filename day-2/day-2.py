print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
peoples_count = int(input("How many people to split the bill?"))

bill_on_people = total_bill / peoples_count
total_tip = bill_on_people / 100 * tip
result = round(bill_on_people + total_tip, 2)

print(f"Each person should pay: ${result}")
