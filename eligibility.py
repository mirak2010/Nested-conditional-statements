mc=input("Enter Y if you have a medical cause, or enter N if you don't ")
attendance=int(input("Please enter your attendance "))
if mc=="Y":
    print("You are allowed for the exam")

elif attendance>=75:
    print("You are allowed for the exam")
else:
    print("You are not allowed for the exam!")
