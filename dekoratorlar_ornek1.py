"""
1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. Daha sonra bir tane decorator
fonksiyon kullanarak bu fonksiyona 1'den 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin.

"""
def asal(sayi):
    j=2
    while (j<sayi):
        if sayi%j==0:
            return False
        j+=1
    return True
def asal_generator():
    i=2
    while True:
        if asal(i):
            yield i
        i+=1

for i in asal_generator():
    if i>1000:
        break
    print(i)




