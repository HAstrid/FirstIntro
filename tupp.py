a=(1,22,3,55,10)
b=('hi','a',"Helllo")
while True:
	print("\nOperations on Tuples\n")
	print("1.Index of a given item")
	print("2.Length of a tuple")
	print("3.Size of tuple")
	print("4.Concatinating two tuple")
	print("5.Minimum and Maximum in a tuple")
	print("6.Counting number of a specific item")
	print("7.Membership operator")
	print("8.Identity operator")
	print("9.Repitation of a tuple")
	print("10.Exit\n")
	ch=int(input("Enter the choice: "))
	if ch==1:
		print("Tuple is: \n")
		n=int(input("Enter the item: "))
		print(a.index(n))
	elif ch==2:
		print("Length of the tuple is:",len(a),"\n")
	elif ch==3:
		print("Size of the tuple is: ",a.__sizeof__())
	elif ch==4:
		print("Concatinating two tuples: \n")
		print(a + b)
	elif ch==5:
		print("Min \n")
		print(min(a))
		print("After switching the case: \n")
		print(max(a))
	elif ch==6:
		print("Counting: \n")
		n=input("Enter the word you want: ")
		print("The word ",n," is present ",b.count(n)," times\n")
	elif ch==7:
		print("The tuple is or not: \n")
		n=int(input("Enter value: "))
		print(n in a)
	elif ch==8:
		print("Identity")
		print(a is a)
	elif ch==9:
		n=int(input("Enter the number of times you want to repeat the string: "))
		print("String: \n")
		print(b*n)
	else:
		break

