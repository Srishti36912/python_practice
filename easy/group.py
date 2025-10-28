import re

if result := re.search(r'([a-zA-Z0-9])\1',input()):
    print(result.group(1))
else:
    print(-1)