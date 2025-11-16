def sap_xep_tu():
    nhap = input("Nhập các từ tiếng Anh cách nhau bởi dấu cách: ")
    tu_list = nhap.split()
    tu_list.sort()
    
    for tu in tu_list:
        print(tu)

sap_xep_tu()