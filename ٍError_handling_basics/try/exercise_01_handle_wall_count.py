try:
    wall_count = int(input("Enter the number of walls: "))
    print(f"Wall count recorded: {wall_count}")
except ValueError:
    print("Invalid wall count! Please enter a whole number.")
