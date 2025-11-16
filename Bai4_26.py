def tinh_tien_ngan_hang():
    print("Nhập nhật ký giao dịch (D cho gửi, W cho rút). Nhập 'done' để kết thúc:")
    tong_tien = 0
    
    while True:
        giao_dich = input().strip()
        if giao_dich.lower() == 'done':
            break
        if not giao_dich:
            continue
            
        parts = giao_dich.split()
        if len(parts) != 2:
            print("Định dạng không hợp lệ. Sử dụng: D 100 hoặc W 200")
            continue
            
        loai, so_tien = parts
        try:
            so_tien = int(so_tien)
            if loai.upper() == 'D':
                tong_tien += so_tien
            elif loai.upper() == 'W':
                tong_tien -= so_tien
            else:
                print(f"Loại giao dịch không hợp lệ: {loai}")
        except ValueError:
            print(f"Số tiền không hợp lệ: {so_tien}")
    
    print(f"Số tiền thực: {tong_tien}")

# Chạy chương trình
tinh_tien_ngan_hang()