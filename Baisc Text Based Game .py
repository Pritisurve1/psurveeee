#defined new game 
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#checked answers of the given question
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

#displaying final score with percetage
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

#If we want to play again then start playing itself
def play_again():

    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


#questions
questions = {
 "Grand Central Terminal, Park Avenue, New York is the world's?: " : "A",
 "Eritrea, which became the 182nd member of the UN in 1993, is in the continent of?:" : "B",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A",
 "The name of the Laccadive, Minicoy and Amindivi islands was changed to Lakshadweep by an Act of Parliament in?: ": "D",
 "The power to decide an election petition is vested in the?:" : "C"
}
#this are options 
options = [["A. Largest railway station","B. highest railway station","C. longest railway station","D. None of the above"],
          ["A. Asia", "B. Africa", "C. Europe", "D. Australia"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"],
          ["A. 1970", "B. 1971", "C. 1972", "D. 1973"],
          ["A. Parliament", "B. Supreme Court", "C. High courts", "D. Election Commission"]]


new_game()

while play_again():
    new_game()

print("GOOD LUCK!")
