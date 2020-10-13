def fonk(*args):
    for i in args:
        print(i)

fonk(1,2,3,4,5,5,3,5,2,4)

def fonk1(**kwargs): #sozluk seklinde olur
    for i,j in kwargs.items():
        print(i,j)

fonk1(isim="sevda",soyisim="agha")


def ic_ice(*args):
    def toplama(args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    print(toplama(args))

ic_ice(1,2,3,4,5)