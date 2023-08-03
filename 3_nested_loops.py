#To print all the combinations for dominos tiles:

for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

print("------------------------------------------")
#if no "end" in print statement then it print below
print("if no end  in print statement then it print below")
for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]")
    print()

print("------------------------------------------")
print("if no second print statement then it prints below")
for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]")
    
print("------------------------------------------")

print("if no second print but there is and then it prints below")
for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
