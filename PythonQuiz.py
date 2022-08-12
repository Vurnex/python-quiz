import os
from datetime import datetime


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def validateChoice(userChoice):
    
    if userChoice == '':
        return False
    
    val = int(userChoice)

    if val >= 1 and val <= 4:  # ensure
        return True
    else:
        print("\nThe available choices are 1-3.\n")
        return False

def MainMenu():
    cls()
    print("\nWelcome to the Python Quiz.\n")
    print("In this program, we will test your knowledge on Python.\n")
    input('Press enter to continue. . . ')

    print("\n1- Start Test")
    print("2- View Results")
    print("3- Exit\n")
    userChoice = input("Please enter your menu choice: ")

    while validateChoice(userChoice) != True:
        userChoice = input("Please enter your menu choice: ")
        validateChoice(userChoice)

    if int(userChoice) == 1:
        UserID()
    elif int(userChoice) == 2:
        CorrectAnswers()
    elif int(userChoice) == 3:
        if os.path.exists('results.txt'):
            print("\nThank you for taking the quiz. Have a nice day.\n")
            quit()
        else:
            print("\nExiting program. Have a nice day.\n")
            quit()
    elif int(userChoice) == 4:  # hidden choice
        try:
            os.remove("results.txt")
            input("\nFile deleted. Press enter to continue...")
        except:
            print("\nNo file found.")
            input('\nPress enter to continue...')
        MainMenu()

def UserID():
    now = datetime.now()
    time_string = now.strftime('%m/%d/%Y %H:%M:%S')
    name = ''
    studentID = ''
    name = input('Please enter your first and last name: ')

    id_valid: bool = False

    while not id_valid:
        studentID = input('Enter your student ID: ')

        if studentID.isdigit() and len(studentID) <= 10:
            id_valid = True
            print('\nName: ' + name)
            print('Student ID: ' + studentID)
            print('Time: ' + time_string)

            input('\nPress any key to begin the quiz...')
            cls()
            Question()
        else:
            id_valid = False
            print(
                '\nEither the information you have entered is invalid, or your student ID does not meet the requirements.')
            print('Requirements: Numbers Only, 10 Character Limit\n')


def Question():
    # initialize and define all variables

    questions = [
        "A video display is a(n)...",
        "A(n) ___ sets a variable to a specified value.",
        "You ___ the module to execute it.",
        "A(n) ___ expression can be set to either True or False.",
        "A(n) ___ loop has no way of ending and repeats until the program is interrupted."]
    opt_1 = [
        "Output device",
        "Variable declaration",
        "Call",
        "Integer",
        "Infinite"]
    opt_2 = [
        "Input device",
        "Print statement",
        "Infinitely loop",
        "String",
        "For"]
    opt_3 = [
        "Control device",
        "Import library",
        "Create",
        "Double",
        "Do-While"]
    opt_4 = [
        "Cord that you plug into your television",
        "None of the above",
        "Print",
        "Boolean",
        "Try"]
    responses = []

    for i in range(len(questions)):
        response_invalid: bool = True
        print("Question {0}: {1}\n\n".format(i + 1, questions[i]))
        print("1. {0}\n".format(opt_1[i]))
        print("2. {0}\n".format(opt_2[i]))
        print("3. {0}\n".format(opt_3[i]))
        print("4. {0}\n".format(opt_4[i]))

        while response_invalid:
            response = input("\nPlease enter the integer associated with your answer choice: ")
            if not (response.isdigit() and 4 >= int(response) >= 1):
                print("\nResponse Invalid. Please enter a valid integer between 1-4.\n")
                response_invalid = True
            else:
                response_invalid = False
                responses.append(response)
        cls()

    results = open('results.txt', 'w')
    for i in range(len(responses)):
        results.write(str("{0}\n").format(responses[i]))
    results.close()

    CorrectAnswers()


def CorrectAnswers():
    cls()
    try:
        with open("results.txt") as f:

            line = f.readline()
            print("Answers given:\n")
            while line != "":
                print(line)
                line = f.readline()
            f.close()

            print("Correct answers are...")
            print("\n#1- 1. Output Device")
            print("#2- 1. Variable Declaration")
            print("#3- 1. Call")
            print("#4- 4. Boolean")
            print("#5- 1. Infinite")

    except IOError:

        print("\nPlease take the test first.")

    input("\n\n\nPress any key to return to the main menu...")
    cls()
    MainMenu()


MainMenu()