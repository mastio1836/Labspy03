x = int()                                       ## Memperkenalkan variable x sebagai integer, kemudian menginputkan nilainya
y = 0                                           ## Memperkenalkan variable y dengan nilai 0
while x >= 0:                                   ## Looping while apabila nilai x tidak sama dengan 0
    x = int(input("Masukan Bilangan: "))        ## Program yang akan di looping
    if x > y:                                   ## if kondisi apabila nilai x lebih besar dari nilai y
     y = int(x)                                 ## Nilai y sama dengan nilai x
    if x == 0:                                  ## if kondisi apabila nilai x sama dengan 0
     break                                      ## Fungsi yang menghentikan operasi dibawahnya  jika suatu kondisi yang di tentukan
print("\nAngka Terbesar Adalah ",y)             ## Mencetak bilangan terbesar

