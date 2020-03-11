s=input() 
if s[-2:] == "AM" and s[:2] == "12":
    print("00"+s[2:-2])
elif s[-2:] == "AM":
    print(s[:-2])
elif s[-2:] == "PM" and s[:2] == "12":
    print(s[:-2])
elif s[-2:] == "PM":
    print(str(int(s[0:2])+12)+s[2:-2])
