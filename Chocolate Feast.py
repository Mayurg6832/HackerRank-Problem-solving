for i in range(int(input())):
	money,cost,exg=map(int,input().split())
	items=money//cost
	if items<exg:
		print(items)
	else:
		count=items
		while items>=exg:
			moreitems=items//exg
			rem=items%exg
			count+=moreitems
			items=rem+moreitems
		print(count)
