h=int(input())
m=int(input())
dic={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty"}
if m==00:
    print("{} o' clock".format(dic[h]))

elif m<10:
	print("{} minute past {}".format(dic[m],dic[h]))

elif m>=10 and m<30 and m!=15:
	if m not in dic:
		frst=(m//10)*10
		scnd=m%10
		print("{} {} minutes past {}".format(dic[frst],dic[scnd],dic[h]))
	else:
		print("{} minutes past {}".format(dic[m],dic[h]))

elif m==15:
    print("quarter past {}".format(dic[h]))

elif m>30 and m!=45:
	m=60-m
	h+=1
	if m not in dic:
		frst=(m//10)*10
		scnd=m%10
		print("{} {} minutes to {}".format(dic[frst],dic[scnd],dic[h]))
	else:
		print("{} minutes to {}".format(dic[m],dic[h]))

elif m==45:
	h+=1
	print("quarter to {}".format(dic[h]))

elif m==30:
	print("half past {}".format(dic[h]))
