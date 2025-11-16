# Bài 4: Nhập một danh sách trên một dòng, các phần tử cách nhau bởi space hoặc tab
danh_sach = input('Nhập danh sách (cách nhau bởi space/tab): ').split()
for phan_tu in danh_sach:
    print(phan_tu)