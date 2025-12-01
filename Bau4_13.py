print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
# Bài 13: Tìm kiếm phần tử trong list
ds = ['abc', '123', 'xyz', 'def', 'abc', '789']

print("Danh sách:", ds)

# Tìm vị trí của chuỗi 'abc'
try:
    vi_tri = ds.index('abc')
    print(f"Vị trí đầu tiên của chuỗi 'abc': {vi_tri}")
except ValueError:
    print("Không tìm thấy 'abc' trong danh sách")

# Tìm tất cả vị trí của 'abc'
vi_tri_tat_ca = [i for i, item in enumerate(ds) if item == 'abc']
print(f"Tất cả vị trí của 'abc': {vi_tri_tat_ca}")

# Kiểm tra phần tử có tồn tại không
if 'xyz' in ds:
    print("'xyz' có tồn tại trong danh sách")
else:
    print("'xyz' không tồn tại trong danh sách")
