print("Welcome to the tip calculator.\n")
total = input("What was the total bill? $\n")
total = float(total)
tip_perc = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
hc_o_ppl = int(input("How many people to split the bill?\n"))
total_pay_person = (total + (total / tip_perc)) / hc_o_ppl
print(f"Each person should pay: {total_pay_person}")
