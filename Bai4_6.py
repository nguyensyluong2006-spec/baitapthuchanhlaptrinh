# Bài 6: Nhập họ tên và tách họ, tên riêng
ho_ten = input('Nhập họ tên: ').split()
if len(ho_ten) >= 2:
    ho = ho_ten[0]
    ten = ho_ten[-1]  # Lấy từ cuối cùng làm tên
    print(f"Họ: {ho}")
    print(f"Tên: {ten}")
else:
    print("Vui lòng nhập đầy đủ họ và tên!")