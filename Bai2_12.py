import re
def kiem_tra_mat_khau(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

chuoi = input("Nhap mat khau (cach nhau bang dau phay): ")
mat_khau = chuoi.split(",")
hop_le = []
for mk in mat_khau:
    if kiem_tra_mat_khau(mk.strip()):
        hop_le.append(mk.strip())
print("Mat khau hop le:", ", ".join(hop_le))