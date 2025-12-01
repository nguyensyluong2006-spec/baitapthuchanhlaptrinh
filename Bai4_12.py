print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
# Bài 12: Xóa phần tử khỏi list
ds = ['abc', '123', 'xyz', 'def', '123', 'abc']  # Danh sách mẫu

print("Danh sách ban đầu:")
for ch in ds:
    print(ch)

# Xóa phần tử 'abc' (chỉ xóa lần xuất hiện đầu tiên)
ds.remove('abc')

print("\nDanh sách sau khi xóa 'abc':")
for ch in ds:
    print(ch)

# Xóa phần tử '123'
ds.remove('123')

print("\nDanh sách sau khi xóa '123':")
for ch in ds:
    print(ch)
