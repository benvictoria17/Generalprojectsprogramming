while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")