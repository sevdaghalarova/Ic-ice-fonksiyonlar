def ana_fonksiyon(islem):
    def toplama(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    def carp(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    if islem=="toplama":
        return toplama
    else:
        return carp

fonk=ana_fonksiyon("carp")
print(fonk(1,2,3,4,5))