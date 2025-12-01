print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
def tim_so_chan():
    ket_qua = []
    for so in range(1000, 3001):
        chu_so = str(so)
        if all(int(c) % 2 == 0 for c in chu_so):
            ket_qua.append(str(so))
    
    print(','.join(ket_qua))

tim_so_chan()
