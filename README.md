# Exercise-5.2
GIS 6345 assignment 5.2

def check_fermat(a,b,c,n):
	if n > 2 and (a**n + b**n == c**n):
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesn't work.")

		
a = int (input("Enter value for a"))
Enter value for a5
b = int (input("Enter value for b"))
Enter value for b7
c = int (input("Enter value for c"))
Enter value for c55
n = int (input("Enter value for n"))
Enter value for n12
check_fermat (a,b,c,n)
No, that doesn't work.
