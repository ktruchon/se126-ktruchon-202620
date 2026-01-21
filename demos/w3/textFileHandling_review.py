#Week 3 Demo - Introduction to 1D & Parallel Lists

#---IMPORTS--------------------------------------------------------
import csv      #comma  seperated  value
#---FUNCTIONS------------------------------------------------------

#---MAIN EXECUTING CODE--------------------------------------------
print("\n\tWelcome to Lab #2 - Machine Info Display\t")

total_records = 0

print(f"{'TYPE':10}{'BRAND':10}{'PROC':4}{'RAM':7}{'1st HD':7}{'2nd HD':7}{'OS':5}{'YEAR':5}")
print("-" * 50)
with open("text_files/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1

        #rec[0] --> machine_type
        if rec[0] == "D": 
            machine_type = "Desktop"
        elif rec[0] == "L":
            machine_type = "Laptop"
        else:
            machine_type = "*ERROR*"

        #rec[1] --> brand
        if rec[1] == "DL":
            brand = "Dell"
        elif rec[1] == "GW":
            brand = "Gateway"
        elif rec[1] == "HP":
            brand = "HP"
        else:
            brand = "*ERROR*"

        #rec[2] --> processor
        proc = rec[2]

        #rec[3] --> RAM
        ram = rec[3]

        #rec[4] --> first_hd
        first_hd = rec[4]

        #rec[5] --> KEY TO REST OF THE FIELDS! --> num_hd
        if rec[5] == "1":
            num_hd = rec[5]
            second_hd = "---" #no second hard drive!
            os = rec[6]
            yr = rec[7]
        else:
            num_hd = rec[5]
            second_hd = rec[6]
            os = rec[7]
            yr = rec[8]

        #display machine data
        print(f"{machine_type:10}{brand:10}{proc:4}{ram:7}{first_hd:7}{second_hd:7}{os:5}{yr:5}")
print("-" * 50)
#disconnected from file--------------------
print(f"\nTOTAL RECORDS: {total_records}\n\nThank you for using my program! Goodbye :] \n\n\n")