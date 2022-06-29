a=1
b=1
m=int(input("輸入階層值:"))
while(b<m):
    a+=1
    b*=a
print('超過',m,'的最小階層為:',a)