"""
5) create a function named factorial() that takes in a number and displays the factorial of that number 

"""
def factorial(fact):
    if fact == 1:
        return 1
    else:
        return (fact * factorial(fact-1))

num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of", num, "is", result)
