def kombinasi(m,n):
    if n==0 or n==m:
        return 1
    
    return kombinasi(m-1, n-1) + kombinasi(m-1, n)
    
print(kombinasi(5,2))
print(kombinasi(4,2))
print(kombinasi(8,3))