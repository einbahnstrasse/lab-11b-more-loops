userinput = int(input("Gimme a number that is greater than 100..."))

while userinput <= 100:
    print(str(userinput) + " is less than or equal to 100, try again...")
    userinput = int(input("Nope, not what I asked for... Gimme a number that is greater than 100..."))

# imagine that the condition has been satisfied... exited the loop...
print(str(userinput) + " is greater than 100! Good job!")
