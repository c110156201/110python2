x=float(input("請輸入x軸座標:"))
y=float(input("請輸入y軸座標:"))
if x!=0 and y!=0:
    if (x>0)and(y>0):
        print("該點位於第一象限，離原點距離為根號"+str((x**2+y**2) ))
    elif (x<0)and(y>0):
        print("該點位於第二象限，離原點距離為根號"+str((-x**2+y**2) ))
    elif (x<0)and(y<0):
        print("該點位於第三象限，離原點距離為根號"+str((-x**2+(-y)**2) ))
    elif (x>0)and(y<0):
        print("該點位於第四象限，離原點距離為根號"+str((x**2+(-y)**2) ))
else:
    if (x!=0):
        print("該點位於第一象限，離原點距離為"+str(abs(x)))
    elif (y!=0):
        print("該點位於第一象限，離原點距離為"+str(abs(y)))
    else:
        print("該點為原點")


