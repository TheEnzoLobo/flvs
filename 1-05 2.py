def main():
    print("Hi, I am Enzo!")
    name = input("What is your first name? : ")
    print("Hi, " + (name))
    guess = input("Can you guess my favorite animal? : ")
    if guess == "wolf":
        print("you are right")
    print("Bye, it was nice talking with you " + (name) + ". Bye" )

main()