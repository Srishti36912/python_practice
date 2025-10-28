import re

pattern= r"(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})(?=[^AEIOUaeiou])"
S = re.findall(pattern, input())

if S:
    print(*S, sep='\n')
else:
    print(-1)