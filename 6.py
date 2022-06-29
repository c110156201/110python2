a=input("輸入值為(以,分隔):")
b=list(a.split(","))
min=sorted(b)
max=sorted(min,reverse=True)
min2=int(''.join(min))
max2=int(''.join(max))

print("最大值數列與最小值數列差為:",(max2-min2))