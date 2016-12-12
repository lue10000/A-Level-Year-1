import csv

BarcodeDic = { '34512340',
               '98981236',
               '56756777',
               '90673412',}


end = False

while end == False:
    product = int(input("Please enter the GTIN-8 code here:"))
    
    if product == 34512340:
        x = 0.50
        print (x)
    elif product == 98981236:
        print("prodcut not found")
        end = True
    elif product == 56756777:
        x = 0.20
        print (x)
    elif product == 90673412:
        x = 1.20 
        print (x)
    quantity = int(input("Please enter the quantity of the product you wish to purchase:"))


    value = (x * quantity) 
    print(value)

    

    
