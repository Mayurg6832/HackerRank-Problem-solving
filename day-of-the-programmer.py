def leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:    
            return True
    else:   
        return False

yr=int(input())
if yr==1918:
    print('26.09.1918')
    exit()
if yr <1919 and yr%4==0:
    print("12.09."+str(yr))
    exit()
if leap(yr):
    print("12.09."+str(yr))
else:
    print("13.09."+str(yr))
