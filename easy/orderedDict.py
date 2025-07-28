from collections import OrderedDict

N = int(input())
ordered = OrderedDict()

for i in range(N):
    line = input().rsplit(" ", 1)
    item_name = line[0]
    net_price = int(line[1])
    
    if item_name not in ordered.keys():
        ordered[item_name] = net_price
    else:
        ordered[item_name] += net_price
        
for k,v in ordered.items():
    print(k,v)