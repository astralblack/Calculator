# Astral's Calcultor 
# Date: 9.27.18

# Menu
print("Hello welcome to my calculator!\n")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division\n")

# Functions
def addition():
    num1 = int(input ("What is the first number?"))
    num2 = int(input ("What is the second number?"))
    sum = num1 + num2
    print("The total is : " + str(sum))

def subtraction():
    num1 = int(input ("What is the first number?"))
    num2 = int(input ("What is the second number?"))
    sum = num1 - num2
    print("The total is : " + str(sum))

def multiplication():
    num1 = int(input ("What is the first number?"))
    num2 = int(input ("What is the second number?"))
    sum = num1 * num2
    print("The total is : " + str(sum))

def division():
    num1 = int(input ("What is the first number?"))
    num2 = int(input ("What is the second number?"))
    sum = num1 / num2
    print("The total is : " + str(sum))


# Used for selecting the operation the user wants to use
choice = input("What operation would you like?")

if choice == "1":
    addition()

elif choice == "2":
        subtraction()

elif choice == "3":
        multiplication()

elif choice == "4":
        division()
