print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
# Bài 8: Tìm từ dài nhất trong chuỗi nhập
chuoi = input('Nhập chuỗi các từ: ').split()
if chuoi:
    tu_dai_nhat = max(chuoi, key=len)
    do_dai_max = len(tu_dai_nhat)
    
    print(f"Từ dài nhất: '{tu_dai_nhat}' (độ dài: {do_dai_max})")
    
    # In tất cả các từ có cùng độ dài lớn nhất
    print("Các từ có cùng độ dài lớn nhất:")
    for tu in chuoi:
        if len(tu) == do_dai_max:
            print(f"- {tu}")
else:
    print("Chuỗi rỗng!")
