# Jordan Tatum
# This program will be a self grading quiz. I learned how to use classes, constructors, lists, and methods in order to condense this program
# I still plan to add a lot more, the questions are basic for now so I can work on formatting the test as well as creating responses from user input errors.
# I spent a lot of time researching, reading, and discussing concepts with my peers. ALL OF THIS CODE WAS WRITTEN BY ME. My peers only helped me conceptualize.
# Here are some of the sources I used:
# https://docs.python.org/3/tutorial/classes.html
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

# Defines the question class (Blueprint for an object)
class Question:
    answer = 0
    option = []
    question = ''
    # Constructor (Allows you to build an object)
    def __init__(self, a, o, q):
        self.answer = a
        self.option = o
        self.question = q
    # Printing object data (question / option) for user
    def question_print(self):
        print(self.question)
        print(self.option)


if __name__ == '__main__':

    # Used later on for quiz grade & percentage.
    total = 0

    # The question list will be created before the first user prompt
    # creates a list (Container) of question objects (questions, options, answers)
    questions = []

    q1 = Question(a = 15, o =[7, 18, 20, 15], q = "What is 90 divided by 6?")
    # adds question one into the list.
    questions.append(q1)

    q2 = Question(a = 6, o =[4, 3, 6, 8], q = "What is the square root of 36?")
    # adds question two into the list.
    questions.append(q2)

    q3 = Question(a = 870, o =[560, 870, 300, 2], q = "What is 145 times 6?")
    # adds question three into the list.
    questions.append(q3)

    q4 = Question(a = 5320, o =[4523, 3452, 8423, 5320], q = "What is 56 times 95?")
    # adds question four into the list.
    questions.append(q4)

    q5 = Question(a = 16384, o =[16384, 12560, 90000, 14435], q = "What is 128 squared?")
    # adds question five into the list.
    questions.append(q5)

    name = input("Hello! \n Welcome to the General Knowledge Practice Test.\n Please start by entering your Name:\n")

    #Starts the test, the list is a joke if the user tries to be funny and input something besides the varied versions of start in the list
    print("Hello", name + "!", "\nAnswer the following questions as best as you can. \n Please type start to begin the test.")
    #list of different syntax of start
    List = ("Start", "start", "START", "sTART", "StArT", "sTaRt", "sTART", "StART", "STaRT", "STArT", "STARt")
    start = input()
    if start in List:
        print("Good Luck!\n")
    #fun little easter egg if someone thinks they will break the code
    else:
        print("Too bad, start anyway!")
    #Declares a total in order to add up the amount of correct questions for a final score.

    for x in questions:
        x.question_print()
        user_input = int(input())
        if user_input == x.answer:
            print("Correct!\n")
            total += 1
        else:
            print("Incorrect.", "the Correct answer was:\n", x.answer, "\n")

    print("You scored a", total, "out of 5!",)
