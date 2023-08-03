def greet_friends(friends):
    for friend in friends:
        print("hello " + friend)
greet_friends(["taylor" , "john" , "Mary" , "Mo"])

print("greet_friends('barry') is printed as below")

greet_friends("barry")

print("greet_friends(['barry']) is printed as below")
greet_friends(["barry"])
