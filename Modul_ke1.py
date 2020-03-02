#nomer 1
def cetakSiku(x):
    [print("*"*j) for j in range (1,x+1)]

#nomer 2
def gambarlahPersegiEmpat(x,y):
    for i in range (1,x+1):
        if (i==1 or i==x):
            print("@"*y)
        else:
            try:
                y/y
                print ("@"+" "*(y-2)+"@")
            except:
                break

#nomer 3a
def jumlahHurufVokal(StringTest):
    return (len(StringTest),len([i for i in StringTest.lower() if i in ("aiueo")]))

#nomer 3b
def jumlahHurufKonsonant(StringTest):
    return (len(StringTest),len([i for i in StringTest.lower() if i not in ("aiueo")]))

#nomer 4
def rerata(array):
    return sum(array)/len(array)

#nomer 5
from math import sqrt as sq
def apakahPrima(x):
    n =int(x)
    assert n>=0
    if n in [2,3,5,7,11]:
        return True
    elif n in [0,1,4,6,8,9,10]:
        return False
    else:
        for i in range (2,int(sq(n)+1)):
            if n%i==0:
                return False
        return True

#nomer 6
def primeLoader(x,y):
    daftar=list((range(x,y)))
    while(x < int(sqrt(y)+1 )):
        if x in daftar:
            for j in range(x*2, y+1, x):
                if j in daftar:
                    daftar.remove(j)
        x = x+1
    print(daftar)

#noemr 7
def faktorPrima(x):
    Sisa=x
    Hasil=[]
    while Sisa>1:
        temp=len(Hasil)
        for i in range(2,Sisa):
            if Sisa%i==0:
                Sisa=int(Sisa/i)
                Hasil.append(i)
                break
        if temp==len(Hasil):
            Hasil.append(Sisa)
            break
    print(Hasil)

#nomer 8
def apakahTerkandung(check,text):
    return (True if (check.lower() in text.lower()) else False)

#nomer 9
def nomer_9():
    for i in range (1,100):
        if i%3==0 and i%5==0:
            print("Python UMS")
        elif i%5==0:
            print ("UMS")
        elif i%3==0:
            print ("Python")
        else:
            print(i)

#nomer 10
from math import sqrt as akar
def selesaikanABC(a,b,c):
    D=float(b**2 -4*a*c)
    return ("Determinan negatif, Persamaan tidak memiliki akar real" if D<0 else ((-b+akar(D))/(2*a),(-b -akar(D))/(2*a))) 

#nomer 11
def apakahKabisat (tahun):
    if (tahun%4==0):
        if tahun%100==0:
            if tahun%400==0:
                return True
            else:
                return False 
        else:
            return True
    else:
        return False

#Nomer 12
from random import randint
def Game():
    Tebak=randint(1,100)
    print("Permainan Tebak Angka.\nSaya menyimpan sebuah angka bulat antara 1 hingga 100. Coba tebak")
    for i in range (1,8):
        tebakan=int(input("Masukan Tebakan ke-%s dari 7:>"% i))
        if Tebak>tebakan:
            print("Itu terlalu Kecil. Coba lagi")
        elif Tebak<tebakan:
            print("Itu terlalu Besar. Coba lagi")
        else:
            print("Ya. anda benar")
            break

#Nomer 13
def katakan(angka):
    pengkata= {"0":"","1":"satu","2":"dua","3":"tiga","4":"empat","5":"lima","6":"enam","7":"tujuh","8":"delapan","9":"sembilan"}
    pembenah= {"sepuluhsatu":"sebelas","sepuluhdua":"dua belas","sepuluhtiga":"tiga belas","sepuluhempat":"empat belas",
               "sepuluhlima":"lima belas","sepuluhenam":"tujuh belas ","sepuluhtujuh":"tujuh belas ","  ":"","satu ribu":"seribu",
               "satu ratus":"seratus","satu puluh ":"sepuluh","sepuluhdelapan":"delapan belas","sepuluhsembilan":"sembilan belas","sepuluh":"sepuluh"}
    posisi2 = ["","ribu","juta"]
    hasil=[pengkata[i] for i in reversed(str(angka))]
    for i in reversed(range(len(hasil))):
        if (i+1)%3==0:                                                                          #ratusan
            hasil.insert(i,"ratus")
        elif (i+1)%3==2:                                                                        #puluhan
            hasil.insert(i,"puluh")
    for i in reversed(range(len(hasil))):
        if i%5==0:                                                                              #ribu dan juta
            hasil.insert(i,posisi2[int(i/5)])
    hasil=((" ".join(reversed(hasil)).replace("  ratus"," ")).replace("  puluh"," "))           # Hilangkan semua yang kosong / tidak diikuti angka
    for i in pembenah.keys():                                                                   # gunakan semua key pada pembenah untuk ilterasi
        hasil=hasil.replace(i,pembenah[i])                                                      # Benahi kesalahan pengucapan dengan dictionary
    return (hasil[0].upper()+hasil[1:])

#nomer 14
from math import ceil
def formatRupiah(x):
    y=[i for i in reversed(str(x))]
    for t in range(ceil(len(y)/3),1,-1):
        y.insert((t-1)*3,".")
    print("Rp. "+"".join(reversed(y)))
    
###Debugger
##cetakSiku(5)                                                  #Nomer 1
##gambarlahPersegiEmpat(4,5)                                    #Nomer 2
##print ( jumlahHurufVokal("Surakarta") )                       #Nomer 3b
##print ( jumlahHurufKonsonant("Surakarta") )                   #Nomer 3b
##print (rerata([1,2,3,4,5]))                                   #Nomer 4
##print( apakahPrima(17) )                                      #Nomer 5
##print( apakahPrima(97) )                                      #Nomer 5
##print( apakahPrima(123))                                      #Nomer 5
##primeLoader(2,1000)                                           #Nomer 6
##faktorPrima(10050)                                            #Nomer 7
##apakahTerkandung("do","Indonesia tanah air beta")             #Nomer 8
##nomer_9()                                                     #Nomer 9
##print(selesaikanABC(1,2,3))                                   #Nomer 10
##print ("%s\n%s"%(apakahKabisat(1900),apakahKabisat(2004)))    #Nomer 11
##Game()                                                        #Nomer 12
##print(katakan(3125750))                                       #Nomer 13
##formatRupiah(500)                                             #Nomer 14
##formatRupiah(1500)
##formatRupiah(5000000)
##formatRupiah(5000000000000)
