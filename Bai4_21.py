print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
def kiem_tra_chia_het_5():
    nhap = input("Nhập các số nhị phân 4 chữ số cách nhau bởi dấu phẩy: ")
    so_nhi_phan = nhap.split(',')
    ket_qua = []
    
    for so in so_nhi_phan:
        so = so.strip()
        if len(so) == 4 and all(bit in '01' for bit in so):
            so_thap_phan = int(so, 2)
            if so_thap_phan % 5 == 0:
                ket_qua.append(so)
    
    print(','.join(ket_qua))

kiem_tra_chia_het_5()
