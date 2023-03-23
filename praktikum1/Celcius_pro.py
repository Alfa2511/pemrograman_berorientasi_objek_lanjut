# NAMA  : Agnes Putri Saraswati
# NIM   : 210511104
# KELAS : TI21K/ K

class Suhu:
    @staticmethod
    def celcius_to_kelvin(c):
        k = c + 273
        return k
    
    @staticmethod
    def celcius_to_fahrenheit(c):
        f = (c * 9/5) + 32
        return f
    
    @staticmethod
    def celcius_to_reamur(c):
        r = c * 4/5
        return r
    
#Contoh penggunaan
C = 20
K = Suhu.celcius_to_kelvin(C)
F = Suhu.celcius_to_fahrenheit(C)
R = Suhu.celcius_to_reamur(C)

print("Konversi", C, "derajat Celcius adalah:", K, "derajat Kelvin")
print("Konversi", C, "derajat Celcius adalah:", F, "derajat Fahrenheit")
print("Koversi", C, "derajat Celcius adalah:", R, "derajat Reamur")