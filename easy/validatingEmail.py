import re
import email.utils

n = int(input())
rex = r"[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}"

for i in range(n):
    mail = email.utils.parseaddr(input())
    
    if re.fullmatch(rex, mail[1]):
        print(email.utils.formataddr((mail[0], mail[1])))