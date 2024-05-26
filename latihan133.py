def deret_ganjil(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return deret_ganjil(n - 1)
    else:
        return n + deret_ganjil(n - 2)
    
print(deret_ganjil(5))
print(deret_ganjil(7))