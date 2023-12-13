# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:06:04 2023

@author: Gwen 06400230047
"""
class mahasiswa:
    mhsCount = 0
    
    def __init__(self, name, nim, angkatan):
        self.name = name
        self.nim = nim
        self.angkatan = angkatan
        mahasiswa.mhsCount += 1
        
    def tampilkanjumlah(self):
        print("TOtal Mahasiswa %d" % mahasiswa.mhsCount)
    
    def tampilkanmahasiswa(self):
        print("Nama: ", self.name)
        print("Nim: ", self.nim)
        print("Angkatan: ", self.angkatan)

name = input("masukin namamu: ")
nim = input("masukin NIM kamu: ")
angkatan = input("masukin Tahun angkatan kamu: ")

print("\n")
mhs1 = mahasiswa(name, nim, angkatan)
mhs1.tampilkanmahasiswa()

print("\n")
print("total mahasiswa %d" % mahasiswa.mhsCount)