import time
def zaman(func):
    def wrapper(sayilar):
        baslama=time.time()
        sonuc=func(sayilar)
        bitis=time.time()
        print(func.__name__ + " " + str(bitis-baslama)+ "saniye surdu")
        return sonuc
    return wrapper

@zaman
def kare(sayilar):
    sayi=[]
    for i in sayilar:
        sayi.append(i**2)
    return sayi

def kup(sayilar):
    sayi3=[]
    for i in sayilar:
        sayi3.append(i**3)
    return sayi3

kare(range(100))