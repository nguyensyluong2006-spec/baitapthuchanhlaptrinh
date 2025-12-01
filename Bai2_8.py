print("nguyễn sỹ lương")
print("245752021610139")
print("#############################")
######################################
a, b = 1, 2
total = 0
print("Fibonacci sequence less than 4,000,000:")
while a < 4000000:
    print(a, end=" ")
    if a % 2 == 0:
        total += a
    a, b = b, a + b
print("\nSum of even numbers:", total)
