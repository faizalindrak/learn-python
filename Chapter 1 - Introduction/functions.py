def greet(lang):
    if lang == 'jawa':
        print('sugeng rawuh')
    elif lang == 'sunda':
        print('mangga')
    else:
        print('selamat datang')

greet('jawa')
greet('sunda')
greet('id')

def tambah(one,two):
    hasil = one + two
    return hasil

print(tambah(100,1000))