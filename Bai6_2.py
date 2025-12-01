print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
class Hinhchunhat:
    def __init__(self, dai, rong):
        self.chieu_dai = dai
        self.chieu_rong = rong
    
    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

# Sử dụng
hcn = Hinhchunhat(5, 3)
print(hcn.dien_tich())
