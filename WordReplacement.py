# method to replace a word in the message
def messageReplacement():
    message = input("Write the message you want to try: ")
    wordProcessReplacement(message)


# method to start the replacement of the word
def wordProcessReplacement(message):
    # Choose the word to replace
    wordToReplace = input("Which word do you want to replace? ")
    # Check if the word to replace is in the message
    if wordToReplace in message:
        # Choose the word used to replace the last one
        wordChosenReplacement = input("Which is the new word ? ")
        # Replacement after the replace() method
        print(message.replace(wordToReplace, wordChosenReplacement))
    else:
        # Message if the word to replace was not found
        print(f"The word '{wordToReplace}' was not found in the message. Write it again")
        wordProcessReplacement(message)

    # Ask about keeping using
    continue_program = input("Do you want to try again? (yes/no): ").lower()
    if continue_program == 'yes':
        messageReplacement()
    else:
        print("Thanks for using the program!")


# Call the main function
messageReplacement()
