import csv 




menu_choice = 0 
while menu_choice != 8:

    print("\t\tPersonal Library Menu")
    print("1. Show ALL TITLES")
    print("2. Search by TITLE")
    print("3. Search by AUTHOR")
    print("4. Search by GENRE")
    print("5. Search by LIBRARY ID")
    print("6. Show ALL AVAILABLE")
    print("7. Show ALL ON LOAN")
    print("8. EXIT")

    menu_choice = input("Enter your search type choice: ")

    if menu_choice == "1":
        print("1. Show ALL TITLES")
    elif menu_choice == "2":
        print("2. Search by TITLE")
    elif menu_choice == "3":
        print("3. Search by AUTHOR")
    elif menu_choice == "4":
        print("4. Search by GENRE")
    elif menu_choice == "5":
        print("5. Search by LIBRARY ID")
    elif menu_choice == "6":
        print("6. Show ALL AVAILABLE")
    elif menu_choice == "7":
        print("7. Show ALL ON LOAN")
    elif menu_choice == "8":
        print("8. EXIT")
    else:
        print("**ERROR** unsupported choice please try again!")

          