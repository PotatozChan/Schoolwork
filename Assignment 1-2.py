print("Pay Check Calculator")
print("===========================================================")
Hours_Worked = float(input("enter hours worked:\t\t"))
Hourly_Pay_Rate = float(input("enter hourly pay:\t\t"))
print()
tax_rate = 18
percentage ="{:.0%}".format(tax_rate / 100)
Gross_Pay = round(Hours_Worked * Hourly_Pay_Rate, 2)
tax_amount = round(Gross_Pay * (tax_rate / 100), 2)
take_home_pay = round(Gross_Pay - tax_amount, 2)
print()
print(f"Gross Pay:{Gross_Pay}")
print(f"tax rate: {percentage}")
print(f"tax_amount:{tax_amount}")
print(f"take home pay:{take_home_pay}")