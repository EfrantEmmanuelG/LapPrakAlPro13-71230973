def jumlah_digit(digit):
    if digit < 10:
        return digit
    else:
        return digit % 10 + jumlah_digit(digit // 10)
    
print(jumlah_digit(234))
print(jumlah_digit(123))
print(jumlah_digit(22))