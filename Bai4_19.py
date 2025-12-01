print("nguyễn sỹ lương")
print("245752021610139")
print("##############################")
#######################################
def is_prime(num):
    """Kiểm tra số nguyên tố"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def bai_19():
    print("Đang tạo tuple số nguyên tố nhỏ hơn 1 triệu...")
    
    # Tạo list số nguyên tố
    primes = []
    for num in range(2, 1000000):
        if is_prime(num):
            primes.append(num)
    
    # Chuyển thành tuple
    P = tuple(primes)
    
    print(f"Đã tạo xong tuple P")
    print(f"Số lượng số nguyên tố: {len(P)}")
    print(f"5 số nguyên tố đầu tiên: {P[:5]}")
    print(f"5 số nguyên tố cuối cùng: {P[-5:]}")
    
    return P
