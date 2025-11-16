import bubble_sort_module

n = int(input("Nhập số lượng phần tử: "))
nlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    nlist.append(value)

print("Danh sách trước khi sắp xếp:", nlist)
sorted_list = bubble_sort_module.bubble_sort(nlist.copy())
print("Danh sách sau khi sắp xếp:", sorted_list)