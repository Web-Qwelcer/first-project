print("=== Trade Calculator ===")

entry = float(input("Entry price: "))
exit_price = float(input("Exit price: "))
size = float(input("Position size: "))

pnl = (exit_price - entry) * size

print("\nResult:")
print("PnL:", round(pnl, 2))