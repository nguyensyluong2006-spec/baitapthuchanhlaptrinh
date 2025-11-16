# Bài 7: Kiểm tra chuỗi có phải là số và in ra
chuoi = input('Nhập chuỗi: ')
if chuoi.isdigit():  # Kiểm tra nếu chuỗi chỉ chứa số
    print(f"Chuỗi '{chuoi}' là số")
else:
    print(f"Chuỗi '{chuoi}' không phải là số thuần túy")