print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
# Bài 17: Tìm số nguyên dương nhỏ hơn n có tổng ước số lớn hơn chính nó
def bai_17():
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n <= 0:
            print("Vui lòng nhập số nguyên dương!")
            return
        
        ket_qua = []
        
        for so in range(1, n):
            # Tính tổng các ước số (không bao gồm chính nó)
            tong_uoc = 0
            for i in range(1, so):
                if so % i == 0:
                    tong_uoc += i
            
            # Kiểm tra nếu tổng ước số lớn hơn chính nó
            if tong_uoc > so:
                ket_qua.append(so)
        
        print(f"Các số nhỏ hơn {n} có tổng ước số lớn hơn chính nó:")
        if ket_qua:
            for so in ket_qua:
                print(so)
        else:
            print("Không có số nào thỏa mãn")
            
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

# Chạy bài 17
bai_17()
