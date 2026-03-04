
#7 rows: 1- 7
#4 seat types: A, B, C, D
seatA = ['A', 'A', 'A', 'A', 'A', 'A', 'A']
seatB = ['B', 'B', 'B', 'B', 'B', 'B', 'B']
seatC = ['C', 'C', 'C', 'C', 'C', 'C', 'C']
seatD = ['D', 'D', 'D', 'D', 'D', 'D', 'D']

#print the seat map!
for i in range(0, 7):
    print(f"{i + 1}  {seatA[i]}  {seatB[i]}     {seatC[i]}  {seatD[i]}")

#ask user for ROW: 1-7
row = int(input("Enter your desired ROW [1-7]: "))

#ask user for SEAT: A, B, C, D
seat = input("Enter your desired SEAT [A/B/C/D]: ")

#check seat and replace with X to reserve, alert user if not
if seat == 'A': #seatA list
    if seatA[row - 1] != "X":
        seatA[row - 1] = "X"
    else:
        print(f"Sorry, seat {row}{seat} is already taken. A")
elif seat == 'B': #seatA list
    if seatB[row - 1] != "X":
        seatB[row - 1] = "X"
    else:
        print(f"Sorry, seat {row}{seat} is already taken. B")
elif seat == 'C': #seatA list
    if seatC[row - 1] != "X":
        seatC[row - 1] = "X"
    else:
        print(f"Sorry, seat {row}{seat} is already taken. C")
elif seat == 'D': #seatA list
    if seatD[row - 1] != "X":
        seatD[row - 1] = "X"
    else:
        print(f"Sorry, seat {row}{seat} is already taken. D")
else:
    print(f"Sorry, seat {row}{seat} is not a valid seat. E")


#reprint seating chart
for i in range(0, 7):
    print(f"{i + 1}  {seatA[i]}  {seatB[i]}     {seatC[i]}  {seatD[i]}")
