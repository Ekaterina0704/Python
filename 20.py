dict= {"AEIOULNSTRАВЕИНОРСТ":1,"DGДКЛМПУ":2, "BCMPБГЕЬЯ": 3,"FNVWYЙЫ":4, "KЖЗХЦЧ": 5, "JXШЭЮ":8, "QZФЩЪ": 10}

a=input("ВВЕДИТЕ СЛОВО ")
summa=0
for i in a:
    for key,value in dict.items():
        if i in key:
            summa+=value
print (summa)            
