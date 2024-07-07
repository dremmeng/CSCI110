def readposint():
    flag = 1
    while flag:
        try:
            num = int(input("Please enter a number: "))
            if num > 0:
                print("That's a Positive Integer.")
                check = input("Do you want to try again? (Y or N):")
                if check == 'Y':
                    flag = 1
                else:
                    flag = 0
            else:   
                print("That's not a Positive Integer")
        except ValueError:
            print("Not an Integer.")

readposint()