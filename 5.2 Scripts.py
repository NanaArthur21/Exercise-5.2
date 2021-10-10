Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def check_fermat(a,b,c,n):
	if n > 2 and (a**n + b**n == c**n):
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesn't work.")

		
>>> def check_numbers():
	a = int(input("6"))
	b = int(input("70"))
	c = int(input("50"))
	n = int(input("100"))
	return check_fermat(a, b, c, n)

>>> check_numbers
<function check_numbers at 0x000001D8669EC0D0>
>>> print(check_numbers)
<function check_numbers at 0x000001D8669EC0D0>
>>> check_fermat
<function check_fermat at 0x000001D8669EC040>
>>> def check_fermat(a,b,c,n):
	if n <= 2:
		print("Fermat's Last Theorem only holds for n>2")
		return
	else:
		if a**n + b**n == c**n:
			print(Holy smokes, Fermat was wrong!")
			      
SyntaxError: invalid syntax
>>> 
>>> def check_fermat(a,b,c,n):
	if n <= 2:
		print("Fermat's Last Theorem only holds for n>2")
		return
	else:
		if a**n + b**n == c**n:
			print("Holy smokes, Fermat was wrong!")
		else:
			print("No, that doesn't work.")

			
>>> def get_user_input():
	a = int(raw_input("5"))
	b = int(raw_input("6"))
	c = int(raw_input("9090"))
	n = int(raw_input("65"))
	check_fermat(a,b,c,n)

	
>>> if__name__ == "__main__":
	
SyntaxError: invalid syntax
>>> a = int(raw_input('6'))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a = int(raw_input('6'))
NameError: name 'raw_input' is not defined
>>> 
================================ RESTART: Shell ================================
>>> a = int(raw_input('6'))
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a = int(raw_input('6'))
NameError: name 'raw_input' is not defined
>>> 
================================ RESTART: Shell ================================
>>> a = int(input('6'))
6
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a = int(input('6'))
ValueError: invalid literal for int() with base 10: ''
>>> 
================================ RESTART: Shell ================================
>>> def check_fermat(a,b,c,n):
	if n > 2 and (a**n + b**n == c**n):
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesn't work.")

		
>>> a = int (input("Enter value for a"))
Enter value for a5
>>> b = int (input("Enter value for b"))
Enter value for b7
>>> c = int (input("Enter value for c"))
Enter value for c55
>>> n = int (input("Enter value for n"))
Enter value for n12
>>> check_fermat (a,b,c,n)
No, that doesn't work.
>>> 