# tentukan ordo matriks A
baris_A=int(input("masukkan ukuran baris matriks A= "))
kolom_A=int(input("masukkan ukuran kolom matriks A= "))

#Tentukan ordo matriks B
baris_B=int(input("masukkan ukuran baris matriks B= "))
kolom_B=int(input("masukkan ukuran kolom matriks B= "))

if (kolom_A!=baris_B):
    print ("matriks tidak dapat dikalikan!")
else:
    print ("masukkan elemen matriks A : ")
    A = []
    for i in range (baris_A):
        baris=[]
        for j in range (kolom_A):
            value = int(input("elemen matriks A: "))
            baris.append(value)
            A.append(baris)
            
print("masukkan elemen matriks B ")
B = []
for i in range (baris_B):
    baris=[]
    for j in range (kolom_B):
        value = int(input("elemen matriks B: "))
        baris.append(value)
        B.append(baris)

    print ("matriks A : ", A)
    print ("matriks B : ", B)


hasil_kali = [[0 for _ in range(kolom_B)] for _ in range(baris_A)]
for i in range(baris_A):
    for j in range(kolom_B):
        for k in range(kolom_A):
            hasil_kali[i][j]+=A[i][k]*B[k][j]

print ("hasil perkalian matriks A dengan B adalah ", hasil_kali)



    
  


