print("welcome to the tip calculator")
total = float(input("what is the total bill? "))
tip = float(input("what is the tip? 10, 12, or 15? "))
people = int(input("how many people are there? "))

tip_total = total * (tip / 100)
total_with_tip = total + tip_total
total_per_person = total_with_tip / people

print(f"the total bill is {total_with_tip}")
print(f"the total per person is {total_per_person}")