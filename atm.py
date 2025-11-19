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
withdraw_amount = 500
balance = 2000
pin = 636360


if balance > withdraw_amount:
    print("The transaction is approved")
else:
    print("The transaction is declined")
