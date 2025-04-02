#
# Tip Calculator
print("Welcome to the tip calculator")
total_bill_amount = int(input("What is the total bill amount?"))
tip = int(input("How much tip would you like to give? 10,12,15"))
persons = int(input("How many persons would split the bill?"))
total_tip =round((((total_bill_amount * (tip/100))+total_bill_amount)/5),2)
print(f"Each person should pay: ${total_tip}")
