d1 = int(input("enter the first diget of the GTIN-8 :"))
d2 = int(input("enter the second diget of the GTIN-8 :"))
d3 = int(input("enter the third diget of the GTIN-8 :"))
d4 = int(input("enter the fourth diget of the GTIN-8 :"))
d5 = int(input("enter the fifth diget of the GTIN-8 :"))
d6 = int(input("enter the sixth diget of the GTIN-8 :"))
d7 = int(input("enter the seventh diget of the GTIN-8 :"))

Num1 = d1*3
Num2 = d2*1
Num3 = d3*3
Num4 = d4*1
Num5 = d5*3
Num6 = d6*1
Num7 = d7*3

x = Num1+Num2+Num3+Num4+Num5+Num6+Num7
print (x)
if x % 10 == 0:
    d8 = 0
    print (x)
else:
    d8 = (10 - (x%10))
    print (d8)
     
A = (x + d8)

print (A)

if A % 10 == 0:
    print (" the GTIN-8 code is vaild")
else:
    A % 10 > 0
    print (" the GTIN-8 code is invaild")
    
barcode = [d1,d2,d3,d4,d5,d6,d7,d8]

print (barcode)
