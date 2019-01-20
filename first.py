def translate(x):   

    summa = 0
    dop2 = ["IIII", "VVVV", "XXXX", "LLLL", "CCCC", "DDDD", "IIX", "IIV", "IIL", "IIC", "IID", "IIM", "VVX","VVL", "VVC", "VVD", "VVM", "CCM","CCD"]
    p1 = 0
    for i in dop2:
        li = x.find(i)
        if li != -1:
            p1 = 1

    if p1 == 0:
    



    
        figures = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        n = "" #те цифры которые уже посмотрели
        k = "" #те цифры которые идут по циклу
        h = len(x)
        if len(x) >= 3:
            for i in range(0,len(x)-2):
                m = i
                k += x[i]
                e = n.find(k)
                if e == -1:
                
                
                    

                        
                    
                    if x[i]+x[i+1] == "IX":
                        summa += 9
                        n += (x[i]+x[i+1])
                    elif x[i]+x[i+1] == "IV":
                        summa += 4
                        n += (x[i]+x[i+1])
                    elif x[i]+x[i+1] == "XL":
                        summa += 40
                        n += (x[i]+x[i+1])
                    elif x[i]+x[i+1] == "XC":
                        summa += 90
                        n += (x[i]+x[i+1])
                    elif x[i]+x[i+1] == "CD":
                        summa += 400
                        n += (x[i]+x[i+1])
                    elif  x[i]+x[i+1] == "CM":
                        summa += 900
                        n += (x[i]+x[i+1])
                    else:
                        summa += figures[x[i]]
                        n += x[i]
                        
            if m+3 == len(x): #2 цифры осталось
                i=m+1
                if x[i]+x[i+1] == "IX":
                    summa += 9
                        
                elif x[i]+x[i+1] == "IV":
                    summa += 4
                        
                elif x[i]+x[i+1] == "XL":
                    summa += 40
                        
                elif x[i]+x[i+1] == "XC":
                    summa += 90
                        
                elif x[i]+x[i+1] == "CD":
                    summa += 400
                        
                elif  x[i]+x[i+1] == "CM":
                    summa += 900
                        
                else:
                    summa += (figures[x[i]]+figures[x[i+1]])
            
                
            if m+2 == len(x): # 1 цифра осталась
                summa += figures[x[m+1]]

                
           

                    


                


                
        elif len(x) == 1:
            summa = figures[x]
            
        else:
            dop = ["IL", "IC", "ID", "IM", "VL", "VC", "VD", "VM", "XD", "XM", "LD", "LM","DM"]
            p = 1
            for i in dop:
                if x == i:
                    p = 0
            if p != 0:
                if x[0] == x[1]:
                    summa += 2*figures[x[0]]
                else:
                        i=0
                        if x[i]+x[i+1] == "IX":
                            summa += 9
                            
                        elif x[i]+x[i+1] == "IV":
                            summa += 4
                            
                        elif x[i]+x[i+1] == "XL":
                            summa += 40
                            
                        elif x[i]+x[i+1] == "XC":
                            summa += 90
                            
                        elif x[i]+x[i+1] == "CD":
                            summa += 400
                            
                        elif  x[i]+x[i+1] == "CM":
                            summa += 900
                            
                        else:
                            summa += (figures[x[i]]+figures[x[i+1]])       
                        
    if summa != 0:      
        print(summa)
    else:
        print("Неправильная запись числа в римской системе")
        
            
translate("MMMDI")



