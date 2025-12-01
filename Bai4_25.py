print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
def loc_so_le():
    nhap = input("Nhập các số cách nhau bằng dấu phẩy: ")
    danh_sach = nhap.split(',')
    so_le = []
    
    for so in danh_sach:
        so = so.strip()  # Loại bỏ khoảng trắng thừa
        if so.isdigit() and int(so) % 2 != 0:
            so_le.append(so)
    
    ket_qua = ','.join(so_le)
    print(ket_qua)

# Chạy chương trình
loc_so_le()
