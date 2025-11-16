# Bài 5: In danh sách theo thứ tự ngược với thứ tự nhập
danh_sach = input('Nhập danh sách các từ: ').split()
# In theo thứ tự ngược
for i in range(len(danh_sach)-1, -1, -1):
    print(danh_sach[i])

# Hoặc cách khác:
# danh_sach_dao_nguoc = danh_sach[::-1]
# for phan_tu in danh_sach_dao_nguoc:
#     print(phan_tu)