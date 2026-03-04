#W9 - SE126 Review + Dictionaries in Python
#this demo uitilizes: dictionary_file.csv [W8 + W9 Canvas]

#DICTIONARIES: another collection type in Python (like lists)

import csv 

#dictionary -> {}
library = {
    #indexes are STRINGS set by the developer
    #'KEY' : value,
    '1230' : "Red Rising",
    '1231' : "The Little Prince"
}
print(f"library['1230']: {library['1230']}")


#list -> []
library_nums = []
    #'1234', #-->[0]
    #'1235'  #-->[1]
#]

#print(f"library_nums[0]: {library_nums[0]}") #--> '1234' 

titles = []

with open('text_files/dictionary_file.csv') as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        library_nums.append(rec[0])
        titles.append(rec[1])

        #add each record's data as a new KEY + VALUE pair from the text file
        #key --> rec[0], value --> rec[1]
        library.update({rec[0] : rec[1]})
#disconnect from file-------------------------------------

print("\n---PRINTING FROM LISTS-------------------------")
print(f"{'LIBRARY NUM'}\t{'TITLE'}")
print("-" * 50)

for i in range(0, len(titles)):
    print(f"{library_nums[i]:11}\t{titles[i]}")

print("-" * 50)

print("\n---PRINTING FROM DICTIONARY----------------------")
print(f"{'KEY':6}\t{'VALUE'}")
print("-" * 50)

for key in library:
    #for every key in our library dictionary
    print(f"{key:6}\t{library[key]}")

print("-" * 50)

#SEQUENTIAL SEARCH FOR A TITLE - using DICTIONARY
search = input("\nEnter the TITLE you are looking for: ")
found = 0 #bc we're using a dictionary!, keys will never be numbers! always strings!


if search.lower() in library:
    #store the found title's 'location' (KEY!) 
    found = key
if found != 0:
    print(f"\nKEY: {found} \t TITLE: {library[found]}")
else:
    print(f"\nYour search for {search} came up empty :[")




#BINARY SEARCH for a LIBRARY NUM - using LISTS!
min = 0 #reps the first possible index
max = len(titles) - 1 #reps the last possible index
mid = int((min + max) / 2) #middle index between min & max


search = input("\nEnter the LIBRARY NUM you are looking for: ")

while min < max and search != library_nums[mid]:
    if search < library_nums[mid]:
        max = mid - 1
    else: 
        min = mid + 1

    mid = int((min + max) / 2)
if search == library_nums[mid]:
    print(f"\nINDEX: {mid} \t TITLE: {titles[mid]}")
else:
    print(f"\nYour search for {search} came up empty :[")