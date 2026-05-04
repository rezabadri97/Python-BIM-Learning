try:
    num1=int(input("Enter First Number:"))
    num2=int(input("Enter Second Number: "))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("You cannot Enter Zero")
except ValueError:
    print("Just Enter Numbers,Pleas!!!!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("End Of The Process")