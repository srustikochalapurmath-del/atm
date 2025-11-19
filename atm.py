import sys
if len(sys.argv) != 4:
    print("Usage: python file.py <withdraw_amount> <balance> <pin>")
    sys.exit()

withdraw_amount = float(sys.argv[1])
balance = float(sys.argv[2])
pin = sys.argv[3]

print(f"ATM withdrawal amount is: {withdraw_amount}")
print(f"Balance is: {balance}")
print(f"PIN is: {pin}")


if balance > withdraw_amount:
    print("The transaction is approved")
else:
    print("The transaction is declined")
