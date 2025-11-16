import find_min_max

n = int(input("Nhập số lượng phần tử: "))
values = []
for i in range(n):
    value = float(input(f"Nhập phần tử thứ {i+1}: "))
    values.append(value)

min_val, max_val = find_min_max.find_min_max(values)
min_index = values.index(min_val)
max_index = values.index(max_val)

print(f"Phần tử nhỏ nhất: {min_val} tại vị trí: {min_index}")
print(f"Phần tử lớn nhất: {max_val} tại vị trí: {max_index}")