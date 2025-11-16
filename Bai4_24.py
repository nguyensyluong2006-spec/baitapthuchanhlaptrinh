def dem_chu_hoa_thuong():
    cau = input("Nhập một câu: ")
    chu_hoa = 0
    chu_thuong = 0
    
    for ky_tu in cau:
        if ky_tu.isupper():
            chu_hoa += 1
        elif ky_tu.islower():
            chu_thuong += 1
    
    print(f"Chữ hoa: {chu_hoa}")
    print(f"Chữ thường: {chu_thuong}")

# Chạy chương trình
dem_chu_hoa_thuong()