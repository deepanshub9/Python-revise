#Total food ordered for snacking
#Electricity units spend
# Charges per unit
# Persons living in room/flat

# Output 
# Total amount you've to pay is

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the electricity units consumed = "))
charge_per_unit = int(input("Enter the charge per unit of the electricity = "))
persons = int(input("Enter the number of persons living in the room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person has to pay = ", output)
