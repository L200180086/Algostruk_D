####Latihan Modul 5
##Nama : Huan Wendy Ariono
##Nim : l200180086
##Kelas : D
##Swap
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
##Debuger
#K = [50,20,70,10]
#swap(K,1,3)
#K
    
##cariPosisiTerkecil
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil
##Debuger
#A = [18,13,44,25,66,107,78,89]
#j = cariPosisiYangTerkecil(A,2,len(A))
#j

##BubbleSort
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                for i in range(len(A)):
                    print(A[i])
                break
        break

##SelectionSort
def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)


##InsertionSort
def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos >0 and nilai<A[pos - 1]:
            A[pos]=A[pos-1]
            pos = pos -1
        A[pos]=nilai
P=[10,51,2,18,4,31,13,5,23,64,29]
