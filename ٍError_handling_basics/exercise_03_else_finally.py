try:
    door_count = int(input("Enter door count: "))
except ValueError:
    print("Invalid door count.")
else:
    print(f"Door count saved: {door_count}")
finally:
    print("Door count check finished.")
