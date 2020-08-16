def repeat():
    first_Number = int(input('Number: '))
    second_number = int(input("Another Number: "))
    operation = input("Operation|(D)ivision,(M)ultipacation,(A)ddition,(S)ubtraction,(E)xponets: ")
    if operation.upper() == "D":
        print(first_Number / second_number)
    elif operation.upper() == "M":
        print(first_Number * second_number)
    elif operation.upper() == "A":
        print(first_Number + second_number)
    elif operation.upper() == "S":
        print(first_Number - second_number)
    elif operation.upper() == "E":
        print(first_Number ** second_number)
    R = input("enter any key to rerun program or press ENTER to Quit: ")