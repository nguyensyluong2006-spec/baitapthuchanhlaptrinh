s = input("Nhap chuoi: ")
result = {}
for char in s:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1
print("Ket qua:", result)