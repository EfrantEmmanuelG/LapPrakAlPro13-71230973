def prima(n):
    if n == 2 or n==3 or n==5 or n==7:
        return 'Bilangan prima'
    if n % 2 == 0 or n % 3 == 0 or n%4 == 0 or n % 5 == 0 or n%6==0 or n%7==0 or n%8==0 or n %9==0:
        return 'Bilangan bukan prima'
    else:
        return 'Bilangan prima'
    
print(prima(97))
print(prima(9))
print(prima(7))
print(prima(88))