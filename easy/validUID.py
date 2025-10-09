import re

n = int(input())
reg = r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[A-Za-z0-9]{10}$'

for i in range(n):
    if re.match(reg, input()):
        print("Valid")
    else:
        print("Invalid")