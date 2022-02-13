print("price comparison")
print("========================================")
print()
sixsize = float(input("Price of 64 oz size:      "))
threesize = float(input("Price of 32 oz size:      "))

price_per_ounce64 = round(sixsize / 64, 2)
price_per_ounce32 = round(threesize / 32, 2)

print(f"price per oz (64 oz): {price_per_ounce64}")
print(f"price per oz (32 oz): {price_per_ounce32}")
