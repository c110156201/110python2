a=input("輸入一串序列(以空格隔開):")
b=a.split(" ")
max=max(b,key=b.count)

if b.count(max)>=len(b)/2:
    print("過半元素為:",max)
else:
    print("過半元素為:NO")