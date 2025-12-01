print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
# Bài 20: In n dòng đầu tiên của tam giác Pascal
def bai_20():
    try:
        n = int(input("Nhập số dòng n của tam giác Pascal: "))
        
        if n <= 0:
            print("Vui lòng nhập số nguyên dương!")
            return
        
        tam_giac = []
        
        for i in range(n):
            dong = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    dong.append(1)
                else:
                    # Tính giá trị từ 2 số phía trên
                    gia_tri = tam_giac[i-1][j-1] + tam_giac[i-1][j]
                    dong.append(gia_tri)
            tam_giac.append(dong)
        
        # In tam giác Pascal
        print(f"Tam giác Pascal {n} dòng:")
        for i in range(n):
            # Căn giữa các dòng
            khoang_trang = " " * (n - i - 1)
            print(khoang_trang + " ".join(f"{x:3}" for x in tam_giac[i]))
            
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

# Chạy bài 20
bai_20()
