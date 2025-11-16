import search_module

n = int(input("Nhập số lượng phần tử: "))
dlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(value)

item = int(input("Nhập phần tử cần tìm: "))

result, index = search_module.sequential_search(dlist, item)
if result:
    print(f"Phần tử {item} được tìm thấy tại vị trí {index}")
else:
    print(f"Phần tử {item} không được tìm thấy")