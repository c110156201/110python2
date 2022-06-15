m=int(input("輸入月份:"))
d=int(input("輸入日期:"))
s=(m*2+d)%3
l=["普通","吉",'大吉']
print(l[s])