#W2 In Class Lab
#PROGRAM PROMPT:

#VARIABLE DICTIONARY:


#--IMPORTS--------------------------------------------------
import csv
#--FUNCTIONS------------------------------------------------
def difference(people, max_cap):
    '''this function is passed 2 values and returns the difference between them'''
    diff = max_cap - people
    return diff
#--MAIN EXECUTING CODE--------------------------------------

#initialize known or needed values (counting variables!)
total_records = 0       #total records in file (1 room per record) -> 8
rooms_over = 0          #total number of rooms over capacity -> 3

print(f"\n\n{'ROOM NAME':20}   {'MAX':5}   {'PPL':5}   {'! REMOVE !':5}")
print("-" * 50)
#connect to file
with open("classLab2.csv") as csvfile:
    #read text file data into 'file'
    file = csv.reader(csvfile)
    #process each 'record' in 'file' (for loop!)
    for record in file:
        total_records += 1

        #assign each field of data to a variable
        name = record[0]
        max = int(record[1])    #all file data is read in as a string type
        ppl = int(record[2])

        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        if remaining < 0:
            rooms_over += 1
            print(f"{name:20}   {max:5}   {ppl:5}   {remaining * -1:5}")
print("-" * 50)
#disconnect from file
#display final values: total rooms counted, number of rooms over capacity
print(f"\n\nROOMS OVER CAPACITY: {rooms_over}\nTOTAL ROOMS in FILE: {total_records}")