n=int(input("Masukan Nilai N"))       ## Memperkenalkan Variable n sebagai integer, Kemudian menginputkan nilai

from random import random             ## Mengimport fungsi random
a=random()                            ## Memperkenalkan variable a sebagai random

jumlah=n+1                            ## jumlah = variable n + 1
start=1                               ## Dimulai dari angka 1
stop=jumlah                           ## Berhenti ketika variable jumlah sesuai
step=1                                ## Step angka 1

for i in range(start,stop,step):      ## Perulangan 1 dengan nilai awal variable start, nilai akhir variable
    print("data ke : ",i,"=",(a))     ## Mencetak hasil
    print("\nDone")