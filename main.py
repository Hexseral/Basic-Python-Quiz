# Jordan Tatum
# This program will be a self grading quiz. I learned how to use classes, constructors, lists, and methods
# in order to condense this program
# I added a user input error catcher that allows the program to not be broken by strings or bad input
# I spent a lot of time researching, reading, and discussing concepts with my peers. ALL OF THIS CODE WAS WRITTEN BY ME.
# My peers only helped me conceptualize.
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
    def isInteger(i):
        try:
            int(i)
            return True
        except ValueError:
            return False
    # Checking if variable is a string in order to make the program not crash
if __name__ == '__main__':

    # Used later on for quiz grade & percentage.
    total = 0

    # The question list will be created before the first user prompt
    # creates a list (Container) of question objects (questions, options, answers)
    questions = []

    q1 = Question(a = 15, o =[7, 18, 20, 15], q = "What is 90 divided by 6?\n")
    # adds question one into the list.
    questions.append(q1)

    q2 = Question(a = 6, o =[4, 3, 6, 8], q = "What is the square root of 36?\n")
    # adds question two into the list.
    questions.append(q2)

    q3 = Question(a = 870, o =[560, 870, 300, 2], q = "What is 145 times 6?\n")
    # adds question three into the list.
    questions.append(q3)

    q4 = Question(a = 5320, o =[4523, 3452, 8423, 5320], q = "What is 56 times 95?\n")
    # adds question four into the list.
    questions.append(q4)

    q5 = Question(a = 16384, o =[16384, 12560, 90000, 14435], q = "What is 128 squared?\n")
    # adds question five into the list.
    questions.append(q5)

    q6 = Question(a = 160, o =[160, 340, 124, 185], q = "If y = 16x + 32, and x = 8 what is y?\n")
    # adds question six into the list.
    questions.append(q6)

    q7 = Question(a = 156, o =[143, 112, 205, 156], q = "x + 156 = 312, what is x?\n")
    # adds question seven into the list.
    questions.append(q7)

    q8= Question(a = 11, o =[5, 16, 23, 11], q = "13x - 72 = 71, what is x? \n")
    # adds question eight into the list.
    questions.append(q8)

    q9 = Question(a = 56, o =[16, 52, 46, 23], q = " 3x = 156, what is x?\n")
    # adds question nine into the list.
    questions.append(q9)

    q10 = Question(a = 36, o =[14, 42, 36, 7], q = "y = 2(x + 6), x = 12, what is y?\n")
    # adds question ten into the list.
    questions.append(q10)

    name = input("Hello! \n Welcome to the Basic Algebra Practice Test.\n Please start by entering your Name:\n")

    # Starts the test, the list is a joke if the user tries to be funny and input something besides the varied versions
    # of start in the list
    print("\nHello", name + "!", "\nAnswer the following questions as best as you can. \n Please type start to begin the test.")
    #list of different syntax of start
    List = ("Start", "start", "START", "sTART", "StArT", "sTaRt", "sTART", "StART", "STaRT", "STArT", "STARt")
    start = input()
    if start in List:
        print("Good Luck!\n")
    # fun little easter egg if someone thinks they will break the code
    else:
        print("Too bad, start anyway!\n")
    # Declares a total in order to add up the amount of correct questions for a final score.

    # declared variable for incrementation
    i = 0

    while i < questions.__len__():
        x = questions[i]
        x.question_print()
        user_input = input()
        if Question.isInteger(user_input):
            un = int(user_input)
            if un == x.answer:
                print("Correct!\n")
                total += 1
                i += 1
                # increments the question for a total average and allows the loop to pass to prevent input error
            else:
                if un not in x.option:
                    print("The answer you input is not an option, please try again."
                          # Allows for input error to not be a possibility to break the program
                else:
                    print("Incorrect.")
        else:
            print("The answer you input is not a number\n")


    print("You scored a", total, "out of 10!",)
