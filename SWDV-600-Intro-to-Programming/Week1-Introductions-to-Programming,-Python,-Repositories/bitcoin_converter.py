import re

print("As of 1/13/2020 at 9:00 pm, bitcoin is currently trading at $8,546.82 per bitcoin.")

while True:
    bitCointsToDollars = input("Enter the bitcoin amount:")
    if not re.match(r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?', bitCointsToDollars) is None:
        break
    else:
        print("Parsing error, please try again")

print("You'll get", float(bitCointsToDollars) * 8546.82, "us dollars")
