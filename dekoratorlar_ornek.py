def ekstra(funk):
    def wrapper(sayilar):
        tek_sayi=0
        tek_sayilar=0
        cift_sayi=0
        cift_sayilar=0

        for i in sayilar:
            if i%2==0:
                cift_sayilar+=i
                cift_sayi+=1
            else:
                tek_sayilar+=i
                tek_sayi+=1
        print("cift sayilarin ortalamasi:",cift_sayilar/cift_sayi)
        print("tek sayilarin ortalamasi:",tek_sayilar/tek_sayi)
        funk(sayilar)
    return wrapper



@ekstra
def ortalama(sayilar):
    toplam=0
    for i in sayilar:
        toplam+=i
    print("Ortalama",toplam/len(sayilar))

ortalama([1,2,4,5,6,78,43,56])
