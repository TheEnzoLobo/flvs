'''
1. Decide on an interactive conversation someone could have with a computer.
2. Your program should include at least three interactive prompts.
3. Input from the user should be assigned to variables and used throughout the conversation.
4. At least once, use the indexing or slicing technique.
5. Use concatenation to join string literals and string values.
6. Write the pseudocode for this program. Be sure to include any input and output needed.
'''

def main ():
    first = input("first name: ")
    last = input ("last name: ")
    print("Nice to meet you " + (first + " " + last))
    age = input("How old are you? ")
    sport = input("what is your favorite sport? ")
    if sport == "tennis":
        print("me too")

main()