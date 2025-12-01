print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
# Bài 16: Nhập chuỗi số nhị phân phân tách bởi dấu phẩy
def bai_16():
    nhap = input("Nhập chuỗi các số nhị phân phân tách bởi dấu phẩy: ")
    so_nhi_phan_list = nhap.split(',')
    
    print("Các số nhị phân được nhập:")
    for so in so_nhi_phan_list:
        so = so.strip()  # Loại bỏ khoảng trắng thừa
        print(f"- {so}")

# Chạy bài 16
bai_16()
