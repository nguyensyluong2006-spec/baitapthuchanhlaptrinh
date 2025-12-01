print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
# Bài 14: Sắp xếp các phần tử trong list
ds = ['banana', 'apple', 'cherry', 'date', '123', 'ABC', 'abc']

print("Danh sách ban đầu:")
for ch in ds:
    print(ch)

# Sắp xếp danh sách
ds.sort()

print("\nDanh sách sau khi sắp xếp:")
for ch in ds:
    print(ch)

# Sắp xếp theo độ dài
ds.sort(key=len)
print("\nDanh sách sắp xếp theo độ dài:")
for ch in ds:
    print(ch)

# Sắp xếp giảm dần
ds.sort(reverse=True)
print("\nDanh sách sắp xếp giảm dần:")
for ch in ds:
    print(ch)
