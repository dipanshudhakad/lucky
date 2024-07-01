rent=float (input("enter your hostal /float rent="))
food=float(input("enter the amount of food ordered="))
electricity_spend=float(input("enter the total of electricity spend="))
charge_per_unit=float(input("enter your charge per unit="))
persons=float(input("enter your member in float="))

total_bill=electricity_spend * charge_per_unit      

output=(food+rent+total_bill)//persons

print("each person bill pay=", output)
  