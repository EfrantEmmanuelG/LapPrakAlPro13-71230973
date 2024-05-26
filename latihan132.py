def polindrom(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
        return 'Kalimat Polindrom'
    else:
        return 'Bukan Kalimat Polindrom'
    
print(polindrom('KASUR rusak'))
print(polindrom('kodok'))
print(polindrom('Kataks'))
print(polindrom('Aku suka makan'))
