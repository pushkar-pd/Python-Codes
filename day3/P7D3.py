"""
7) create a function that takes in a number from the user and returns a tuple of all Odd numbers from 1 to that number 
"""

def odd_numbers(list, n=0):
	if n==len(list):
		exit()
	if list[n]%2!=0:
		print(list[n])
	odd_numbers(list, n+1)
list = [10,23,4,34,2]
print("Odd numbers in the list:", end=" ")
odd_numbers(list)