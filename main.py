# define a function to check if a number is prime
def prime():
    n = int(input("Enter the number? "))
    if n / n == 1:
        print("The number", n, "is a prime number")
    prime()
