def dem_chu_cai_va_so():
    cau = input("Nhập một câu: ")
    chu_cai = 0
    chu_so = 0
    
    for ky_tu in cau:
        if ky_tu.isalpha():
            chu_cai += 1
        elif ky_tu.isdigit():
            chu_so += 1
    
    print(f"Số chữ cái là: {chu_cai}")
    print(f"Số chữ số là: {chu_so}")

dem_chu_cai_va_so()