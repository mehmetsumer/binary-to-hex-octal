# -*- coding: utf-8 -*-

def octal(octal):
        sonuc = 0
        cevir = ""
        arr = []
        octal = str(octal)
        uz = len(octal)
        don = int(uz/3)
        if(uz % 3 != 0): don += 1
        uz -= 1 
        for j in range(don):
             carp = 1
             sonuc = 0
             for i in range(uz,(uz-3),-1):
                if( i >= 0): sonuc += int(carp * int(octal[i]))
                else: sonuc += 0
                carp *= 2
             arr.append(sonuc)
             uz -= 3
        for i in range(len(arr)-1,-1,-1): cevir += str(arr[i])
        return "Octal kodu: " + cevir
         
def hex(binary):
        hexx = ['A' , 'B' , 'C' ,'D' , 'E' , 'F']
        sonuc = 0
        cevir = ""
        arr = []
        binary = str(binary)
        uz = len(binary)
        don = int(uz/4)
        if(uz % 4 != 0): don += 1
        uz -= 1 
        for j in range(don):
             carp = 1
             sonuc = 0
             for i in range(uz,(uz-4),-1):
                if( i >= 0): sonuc += int(carp * int(binary[i]))
                else: sonuc += 0
                carp *= 2
             arr.append(sonuc)
             uz -= 4
        for i in range(len(arr)-1,-1,-1):
            if(arr[i] >= 10): cevir += hexx[arr[i] - 10]
            else: cevir += str(arr[i])
        return "Hex kodu: " + cevir

print (hex(11101100101001))    # 3B29
print (octal(10011011))    # 233