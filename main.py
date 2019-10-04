# Jordan Tatum
# This program will be a self grading quiz based on basic Algebra 1 arethmatic functions, due to it still being in a trial stage the first
# Equation is simple in order for me to figure out how to structure the quiz and deal with the bugs

name = input("Hello User welcome to the Algebra 1 Knowledge Quiz, please start by entering your name\n")

#Starts the test, the list is a joke if the user tries to be funny and input something besides the varied versions of start in the list
print("Hello,", name, "please type start to begin the test, Answer the questions as best as you can.")
List = ("Start", "start", "START", "sTART", "StArT", "sTaRt", "sTART", "StART", "STaRT", "STArT", "STARt")
start = input()
if start in List:
    print("Good Luck!")
else:
    print("Too bad, start anyway!")
#If the user inputs anything other than one of the versions of start within the list it will print the line above

answerOne = input("what is 1 + 1?\n")
if answerOne == 2:
    print("Correct!")
else:
    print("Incorrect.")
while loop for if then
that why this that if then updating my ripository to show actifity bla bla bla
