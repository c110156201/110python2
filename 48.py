b=int(input("輸入筆數:"))
d={}
for i in range(b):
    d[str(input("英文:"))]=str(input("中文:"))

##d={"dog":"狗","cat":"貓","bear":'熊','snake':"蛇"}
a=str(input("輸入欲查詢單字:"))
if a in d:
    print(d[a])
else:
    print("未有此單字")

print(d)