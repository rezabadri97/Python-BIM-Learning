try:
    level_number=int(input("Enter Level Number:"))
    if level_number<1:
        raise ValueError("Level number must be 1 or greater.")

    print(f"Level number saved: {level_number}")
except ValueError as error:
    print(f"Error: {error}")