# To repeatedly read numbers until the user enters "done". Once 
#"done" is entered, print out the total, max and minimum of the numbers.
# Ensure anything other than numbers is verified
#Set local variables
count = 0
total = 0
max_num = None
min_num = None
#Top of loop
while True:
    character_in = input("> ")
    if character_in == "done":
        break
    #test for number by converting to float 
    try:
        clean_number = float(character_in)
        #increment count and perform other calcs.  count not incremented if error
        count = count + 1
        total = total + clean_number
        if min_num is None or clean_number < min_num:
        	min_num = clean_number
        if max_num is None or clean_number > max_num:
            max_num = clean_number
    except:
    	print("Please only enter a number")
#exits on "done", prints
print("Total:", total, " Maximum num:", max_num, " Minimum num:", min_num)