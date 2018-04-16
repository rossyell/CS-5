# To repeatedly read numbers until the user enters "done". Once 
#"done" is entered, print out the total, count, and average of the numbers.
# Ensure anything other than numbers is verified
#Set locla variables
count = 0
total = 0
average = 0
#Top of loop
while True:
    character_in = input("> ")
    if character_in == "done":
        break
    #test for number by converting to float 
    try:
        number = float(character_in)
        #increment count and perform other calcs.  count not incremented if error
        count = count + 1
        total = total + number
    except:
    	print("Please only enter a number")
#exits on "done", calculates average and prints
try:
    average = total/count
except:
    print("Note no numbers entered")    
rnd_average = round(average, 2)
print("Total:", total, " Valid numbers:", count, " Average:", rnd_average)