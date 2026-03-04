import csv 

dictionary = {}

with open('text_files/words.csv') as csvfile:
    file = csv.reader(csvfile)

    for rec in file: 
        dictionary.update({rec[0] : rec[1]})
        #rec[0] -> word = KEY, rec[1] -> definition = VALUE

menu_choice = 0 

while menu_choice != "4":
    print("\n\t~My Programming Dictionary Menu~")
    print("\t1. SHOW all words") #Show all words and their definitions stored to the dictionary
    print("\t2. SEARCH for a word") #Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if the word is not in the dictionary)
    print("\t3. ADD a word") #Allow a user to add a word and its definition to the dictionary if it does not already exist
    print("\t4. EXIT")

    menu_choice = input("\tEnter your choice [1-4]: ")

    #Show all words and their definitions stored to the dictionary
    if menu_choice == "1":
        for key in dictionary:
            print(f"\t{key.upper():15}: \n\t{dictionary[key]}")
    #Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if the word is not in the dictionary)
    elif menu_choice == "2":
        found = 0 
        search = input("\tEnter the WORD you are looking for: ")

        for key in dictionary:
            if key.upper() == search.upper():
                found = key
        if found != 0: 
            print(f"\t{found.upper():15}: \n\t{dictionary[found]}")
        else:
            print(f"\tSorry, your search for {search} came up empty :[")
    #Allow a user to add a word and its definition to the dictionary if it does not already exist
    elif menu_choice == "3":
        word = input("\tEnter the word you woud like to add: ")

        found = 0 

        for key in dictionary:
            if key.upper() == word.upper():
                found = key
        if found == 0: 
            print(f"\tOkay, I will add {word} to the dictionary.")
            definition = input(f"\tPlease enter the definition for {word}: ")

            dictionary.update({word : definition})
        else:
            print(f"\tSorry, {word} already exists in the dictionary and cannot be added :[")

        
    #EXIT
    elif menu_choice == "4":
        print("\n\nThank you for using my program! Goodbye :]\n")
    else:
        print(f"\n\tSorry, {menu_choice} is not a valid menu option. Please try again.\n")