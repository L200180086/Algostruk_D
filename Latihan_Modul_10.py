###menjumlahkan bilangan 1 sampai n
##def jumlahkan_cara_1(n):
##    hasilnya = 0
##    for i in range(1, n+1):
##        hasilnya = hasilnya + 1
##    return hasilnya
###debuger
##jumlahkan_cara_1(10)
##jumlahkan_cara_1(100)

##import time
##def jumlahkan_cara_1(n):
##    hasilnya = 0
##    for i in range(1, n+1):
##        hasilnya = hasilnya + 1
##    return hasilnya
##for i in range(5):
##    awal = time.time()
##    h = jumlahkan_cara_1(10000)
##    akhir = time.time()
##    print("jumlahkan adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))
##    
##for i in range(5):
##    awal = time.time()
##    h = jumlahkan_cara_1(1000000)
##    akhir = time.time()
##    print("jumlahkan adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))
    
##import time
##def jumlahkan_cara_2(n):
##    return(n*(n+1))/2
##for i in range(5):
##    awal = time.time()
##    h = jumlahkan_cara_2(10000)
##    akhir = time.time()
##    print("jumlahkan adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))

##import random,time
##def insertionSort(A):
##    n = len(A)
##    for i in range(1,n):
##        nilai = A[i]
##        pos = i
##        while pos >0 and nilai<A[pos - 1]:
##            A[pos]=A[pos-1]
##            pos = pos -1
##        A[pos]=nilai
##        
##for i in range(5):
##    L = list(range(3000))
##    random.shuffle(L)
##    awal = time.time()
##    U = insertionSort(L)
##    akhir = time.time()
##    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))

##import time
##def insertionSort(A):
##    n = len(A)
##    for i in range(1,n):
##        nilai = A[i]
##        pos = i
##        while pos >0 and nilai<A[pos - 1]:
##            A[pos]=A[pos-1]
##            pos = pos -1
##        A[pos]=nilai
##
##for i in range(5):
##    L = list(range(3000))
##    L = L[::-1]
##    awal = time.time()
##    U = insertionSort(L)
##    akhir = time.time()
##    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))

##import time
##def insertionSort(A):
##    n = len(A)
##    for i in range(1,n):
##        nilai = A[i]
##        pos = i
##        while pos >0 and nilai<A[pos - 1]:
##            A[pos]=A[pos-1]
##            pos = pos -1
##        A[pos]=nilai
##        
##for i in range(5):
##    L = list(range(3000))
##    awal = time.time()
##    U = insertionSort(L)
##    akhir = time.time()
##    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), akhir-awal))
##from timeit import timeit
##timeit('sqrt(2)', 'from math import sqrt', number=10000)

##from timeit import timeit
##timeit('sqrt(2)', 'from math import sqrt', number=10000)
##timeit('sqrt(2)', 'from math import sqrt', number=100000)
##timeit('sqrt(2)', 'from math import sqrt', number=1000000)
##
##time("1=2")
##timeit("sin(pi/3)", setup="from math import sin,pi")
##timeit("sin(1.047)", setup="from math import sin")

import timeit
import matplotlib.pyplot as plt

def kalangBersusuh(n):
    for i in range(n):
        for j in range(n):
            i+j

def ujiKalangBersusuh(n):
    ls=[]
    jangkauan = range(1, n+1)
    siap = "from __main__ import kalangBersusuh"
    for i in jangkauan:
        print('i=', i)
        t = timeit.timeit("kalangBersusuh(" + str(i) +")", setup=siap, number=1)
        ls.append(t)
    return ls
n =100
LS = ujiKalangBersusuh(n)

plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1,n+1)])
plt.show()




























