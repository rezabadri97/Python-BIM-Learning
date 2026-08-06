try:
    number=int(input("Enter the number:"))
    result=200/number
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")