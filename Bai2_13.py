print("nguyễn sỹ lương")
print("245752021610139")
print("#############################")
######################################
import math

a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh co vo so nghiem.")
        else:
            print("Phuong trinh vo nghiem.")
    else:
        x = -c / b
        print("Phuong trinh bac nhat co nghiem: x =", x)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem thuc.")
    elif delta == 0:
        x = -b / (2*a)
        print("Phuong trinh co nghiem kep: x1 = x2 =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phuong trinh co 2 nghiem phan biet:")
        print("x1 =", x1)
        print("x2 =", x2)
