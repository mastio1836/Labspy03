modal = 10000000                                            ## Nilai modal
laba = 0                                                    ## Nilai laba 0
untung = 0                                                  ## Nilai gambar
for i in range (1,9,1):                                     ## Perulangan 1 dengan nilai awal 1, nilai akhir 9 dan step 1
 if(i<3):                                                   ## Kondisi apabila belum bulan ke-3 laba masih 0%
     laba = 0
     untung = untung + laba
 elif(i<5):                                                 ## Kondisi apabila belum memasuki bulan ke-5, mendapat laba sebesar
    laba = modal*1/100
    untung = untung + laba
 elif(i<8):                                                 ## Kondisi apabila belum memasuki bulan ke-8, Mendapat laba sebesar
    laba = modal*5/100
    untung = untung + laba
 else:                                                      ## Pada bulan ke-8 laba menurun 2%, sehingga laba bulan ke-8 sebesar
    laba = modal*2/100
    untung = untung + laba
print("Laba Bulan Ke-",i," Sebesar ",laba)                  ## Mencetak laba per bulan
print("\nTotal Laba adalah: ",untung)                       ## Menghitung total laba selama 8 bulan







