min_age = 0
max_age = 100
print("Welcome to Age Finder")
for i in range(6):
    guess_value = (max_age+min_age)//2
    print("Guess",i+1,":",guess_value)
    opt=int(input("1. Your age is greater than the guessed value \n2. Your age is the same as guessed value \n3. Your age is lesser than the guessed value\n"))
    if opt == 1:
        min_age = guess_value
    elif opt == 2:
        print("Your age is ",guess_value)
        break
    elif opt == 3:
        max_age = guess_value
    if i == 5:
        print("Your age is", min_age+1)
        
print("Thank you, I hope you found your age 😊")

