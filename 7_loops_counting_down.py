for n in range(11, 0, -2):
    if n % 2 != 0:
        print(n, end = " ")

print("----------------------------------------------")
starting_number = 18
# The while loop will continue to loop until it reaches 0.
# end =" " is to print in one line instead of new line character
while starting_number >= 0:
    print(starting_number, end=" ")
    
    # Decrement the "starting_number" variable by -3.
    starting_number -= 3
print("------------------------------Below is option 3----------------")

#the below does not print 0 if tange(18, 0, -3)
for n in range(18, -1, -3):
   print(n, end=" ")
