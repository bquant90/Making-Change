# This program will calculate the amount of change a person would get for a
# given amount of money. Higher denominations of money are preferred.
from decimal import Decimal, InvalidOperation

def main():
    denominations = {
        100: "hundred",
        50: "fifty",
        20: "twenty",
        10: "ten",
        5: "five",
        1: "one",
        0.25: "quarter",
        0.1: "dime",
        0.05: "nickel",
        0.01: "penny"
    }
    while True:
        try:
            change = Decimal(input("Enter an amount of money to be converted to change: $"))
            if change == 0:
                print("Invalid input. Please enter a valid change amount.")
                continue
            elif change < 0:
                raise ValueError("Negative change not allowed.")
            elif change.as_tuple().exponent < -2:
                raise ValueError("Input amount should have at most 2 decimals.")
            break
        except ValueError as e:
            if "Negative" in str(e):
                print("Negative change not allowed. Please enter a valid change amount.")
            elif "at most 2 decimals" in str(e):
                print("Input amount should have at most 2 decimals. Please enter a valid change amount.")
            else:
                print("Invalid input. Please enter a valid change amount.")
        except InvalidOperation:
            print("Invalid input. Please enter a valid change amount.")

    change_in_cents = int(change * 100)
    print("Hand the customer the following amounts of each:")
    for denom in denominations:
        num_denom = change_in_cents // int(denom * 100)
        change_in_cents %= int(denom * 100)
        if num_denom > 0:
            if denom >= 1:
                print(f"${int(denom):d} x {num_denom}")
            else:
                print(f"{denom:.2f}¢ x {num_denom}")

main()
