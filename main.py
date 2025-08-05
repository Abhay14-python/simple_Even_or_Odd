'''This is a programme to find if a number is even or odd'''
print("This is a programme to find if a number is odd or even")
while True:
    try:
        n = int(input("Enter the number : "))
        break
    except ValueError :
        print("Invalid input \n Please enter  an integer")

if n % 2 == 0:
    print(f"The number {n} is Even.")
else :
    print("The number is Odd.")