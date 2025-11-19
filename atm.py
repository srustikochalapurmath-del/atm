import sys



#
if len(sys.argv) == 4:
    withdraw_amount = float(sys.argv[1])
    balance = float(sys.argv[2])
    pin = sys.argv[3]

    print("User-entered values:")
    print(f"ATM withdrawal amount is: {withdraw_amount}")
    print(f"Balance is: {balance}")
    print(f"PIN is: {pin}")

# Else use default values
else:
    
default_withdraw_amount = 500
default_balance = 2000
default_pin = 636360

    print("Default values are used:")
    print(f"ATM withdrawal amount is: {withdraw_amount}")
    print(f"Balance is: {balance}")
    print(f"PIN is: {pin}")

# Transaction condition
if balance > withdraw_amount:
    print("\nThe transaction is approved")
else:
    print("\nThe transaction is declined")
