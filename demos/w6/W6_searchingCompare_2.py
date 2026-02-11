#W6 - Searching Algorithms: Binary vs Sequential Search 
import csv  

library_nums = []     #the ONLY ORDERED field
titles = []
authors = []
genres =[]
pages = []

with open("text_files/library_books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: 
        library_nums.append(rec[0])
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pages.append(rec[4])

print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20}  {'PAGES':5}")
print("--------------------------------------------------------------------------------")
for i in range(0, len(library_nums)):
    print(f"{library_nums[i]:5}  {titles[i]:25}  {authors[i]:15}  {genres[i]:20}  {pages[i]:5}")
print("--------------------------------------------------------------------------------\n")

#SEQUENTIAL SEARCH: allow a user to search for a speciifc title 
#       - list we search through does NOT need to be ordered
#       - we can return MULTIPLE (ie non-unique) data using this searching method
#titles[] is NOT ordered
'''
#during demo this is commented out so we can have a direct comparison of sequential search vs binary search in our final counts
found = [] 
search_title = input("Which title are you looking for: ")
seq_count = 0 #just for demo

for i in range(0, len(titles)):
    seq_count += 1

    if search_title.lower() in titles[i].lower():
        #in above allows us to use partial search terms like "tig" or "the" to find all matching results :]
        found.append(i)

print(f"SEARCH ITERATIONS: {seq_count}")

if not found: #"if the list found is empty"
    #found list is still empty, meaning no matches to our search term were found
    print(f"Sorry, your search for {search_title} was NOT found :[")
else:
    print(f"Yay, your search for {search_title} was FOUND :]")

    print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20}  {'PAGES':5}")
    print("--------------------------------------------------------------------------------")
    for i in range(0, len(found)):
        print(f"{library_nums[found[i]]:5}  {titles[found[i]]:25}  {authors[found[i]]:15}  {genres[found[i]]:20}  {pages[found[i]]:5}")
    print("--------------------------------------------------------------------------------\n")
'''

found = [] 
search_num = input("Which LIBRARY NUM ID are you looking for: ")
seq_count = 0 #just for demo

for i in range(0, len(titles)):
    seq_count += 1

    if search_num == library_nums[i]:
        found.append(i)

print(f"SEARCH ITERATIONS: {seq_count}")

if not found: #"if the list found is empty"
    #found list is still empty, meaning no matches to our search term were found
    print(f"Sorry, your search for {search_num} was NOT found :[")
else:
    print(f"Yay, your search for {search_num} was FOUND :]")

    print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20}  {'PAGES':5}")
    print("--------------------------------------------------------------------------------")
    for i in range(0, len(found)):
        print(f"{library_nums[found[i]]:5}  {titles[found[i]]:25}  {authors[found[i]]:15}  {genres[found[i]]:20}  {pages[found[i]]:5}")
    print("--------------------------------------------------------------------------------\n")



#BINARY SEARCH: must be performed on ORDERED lists (library_nums)
#       - list you will search through MUST be ordered
#           ascending (increasing order) A -> Z, 0 - 9 OR descending (decreasing order) Z ->, 9 -> 0 
#           *** the algorithm provided in class is for INCREASING ordered lists***
#       - the data set we search through must have UNIQUE DATA VALUES (ie no repeats!)
#Binary Search Algorithm [from Canvas]:

#BUBBLE SORT----------------------------------------

for i in range(0, len(titles) - 1):#outter loop
    print("OUTER LOOP! i = ", i)

    for index in range(0, len(titles) - 1):#inner loop
        print("\t INNER LOOP! k = ", index)
        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing

        if(titles[index] > titles[index + 1]):
            print("\t\t SWAP! ", titles[index], "<-->", titles[index + 1])
            #if above is true, swap places!

            temp = titles[index]
            titles[index] = titles[index + 1]
            titles[index + 1] = temp

 
            #swap all other values
            temp = genres[index]
            genres[index] = genres[index + 1]
            genres[index + 1] = temp

            temp = authors[index]
            authors[index] = authors[index + 1]
            authors[index + 1] = temp

            temp = pages[index]
            pages[index] = pages[index + 1]
            pages[index + 1] = temp

            temp = library_nums[index]
            library_nums[index] = library_nums[index + 1]
            library_nums[index + 1] = temp

print("---BUBBLE SORTED BY TITLE-------------------")
print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20}  {'PAGES':5}")
print("--------------------------------------------------------------------------------")
for i in range(0, len(library_nums)):
    print(f"{library_nums[i]:5}  {titles[i]:25}  {authors[i]:15}  {genres[i]:20}  {pages[i]:5}")
print("--------------------------------------------------------------------------------\n")
search_num = input("\nWhich TITLE are you looking for: ")
min = 0
max = len(titles) - 1       #can also use len(listName) for 'records' value

mid = int((min + max) / 2)

bin_count = 0 #just for demo
#this is for INCREASING (ascending) order
while (min < max and search_num.lower() != titles[mid].lower() ):
    bin_count += 1
    if search_num.lower()  < titles[mid].lower() :
        max = mid - 1

    else:
        min = mid + 1

    mid = int((min + max) / 2)

if search_num.lower()  == titles[mid].lower() :
    #found them! use 'guess' for index of found search item
    print(f"Yay, your search for {search_num} was FOUND :]")

    print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20}  {'PAGES':5}")
    print("--------------------------------------------------------------------------------")
    print(f"{library_nums[mid]:5}  {titles[mid]:25}  {authors[mid]:15}  {genres[mid]:20}  {pages[mid]:5}")
    ("--------------------------------------------------------------------------------\n")

else:
    #boooo not found - alert your user!
    print(f"Sorry, your search for {search_num} was NOT found :[]")


print(f"\n\nSEQUENTIAL SEARCH COUNT: {seq_count}")
print(f"    BINARY SEARCH COUNT: {bin_count}")