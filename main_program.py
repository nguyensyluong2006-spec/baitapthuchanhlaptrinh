import find_min_max

n = int(input("Nhập số lượng phần tử: "))
values = []
for i in range(n):
    value = float(input(f"Nhập phần tử thứ {i+1}: "))
    values.append(value)

min_val, max_val = find_min_max.find_min_max(values)
sorted_list = find_min_max.sort_list(values)

print(f"Danh sách: {values}")
print(f"Phần tử nhỏ nhất: {min_val}")
print(f"Phần tử lớn nhất: {max_val}")
print(f"Danh sách sắp xếp: {sorted_list}")