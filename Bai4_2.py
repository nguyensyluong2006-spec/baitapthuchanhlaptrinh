# Bài 2: Chỉ in ra những ký tự không phải space và tab
S = input('Nhập chuỗi: ')
for ky_tu in S:
    if ky_tu not in [' ', '\t']:  # Bỏ qua space và tab
        print(ky_tu)