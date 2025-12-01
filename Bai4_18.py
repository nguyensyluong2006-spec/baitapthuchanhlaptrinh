print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
# Bài 18: Tạo list số Fibonacci nhỏ hơn n
def bai_18():
    try:
        n = int(input("Nhập số nguyên n: "))
        
        if n <= 0:
            print("Vui lòng nhập số nguyên dương!")
            return
        
        fibonacci_list = []
        
        if n >= 1:
            a, b = 0, 1
            while a < n:
                fibonacci_list.append(a)
                a, b = b, a + b
        
        print(f"Các số Fibonacci nhỏ hơn {n}:")
        print(fibonacci_list)
        
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

# Chạy bài 18
bai_18()
