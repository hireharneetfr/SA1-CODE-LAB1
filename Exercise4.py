#In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.
question = input("What is the capital of France?") #Asks the user for the capital of france
answer = ("Paris")
if question.lower() == answer.lower(): #This is to make sure the capitalization is ignored
    print("The answer is correct") #If the user has inputed right, the output shows the answer is correct
else: 
    print("The answer is wrong") #If the user has inputed wrong, the output shows the answer is wrong
#In the code above, the question is asked to the user to which only one answer is right (with or without letters being capitalizationed).