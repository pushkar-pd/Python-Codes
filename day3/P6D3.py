"""
6) create a function that  take a number from the user and returns a list of  even numbers from 1 to that number.     

"""

def even_numbers(list, n=0):
	if n==len(list):
		exit()
	if list[n]%2==0:
		print(list[n])
	even_numbers(list, n+1)
list = [10,23,4,34,2]
print("Even numbers in the list:", end=" ")
even_numbers(list)

