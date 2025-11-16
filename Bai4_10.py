# Bài 10: Cắt list - lấy list nhưng bỏ phần tử đầu và cuối
ds = input('Nhập danh sách (các phần tử cách nhau bởi space/tab): ').split()

if len(ds) > 2:
    # Cách 1: Sử dụng slicing [1:-1] để bỏ phần tử đầu (index 0) và cuối (index -1)
    x = ds[1:-1]
    print("Danh sách sau khi bỏ phần tử đầu và cuối:")
    for c in x:
        print(c)
    
    # Cách 2: Hiển thị kết quả để so sánh
    print(f"\nDanh sách gốc: {ds}")
    print(f"Danh sách sau khi cắt: {x}")
elif len(ds) == 2:
    print("Danh sách chỉ có 2 phần tử, sau khi bỏ đầu và cuối sẽ rỗng: []")
    print("Kết quả: []")
else:
    print("Danh sách quá ngắn, không thể bỏ phần tử đầu và cuối!")