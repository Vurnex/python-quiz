import os
from datetime import datetime

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def validateChoice(userChoice):
    try:
        val = int(userChoice)
        if val >= 1 or val <= 3: #ensure 
            return val
    except ValueError:
        print("\nThe availiable choices are 1-3.\n")
    False
	

def chWindow(argument):
    cases = {
    1: "Starting Test",
    2: "View Results",
    3: "Exit",
    }
    print(cases)

def MainMenu():
    print("\nWelcome to the ITS-140 Quiz.\n")
    print("In this program, we will test your knowledge on Python.\n")
    print("Press any key to continue...\n")
    print("\n1- Start Test")
    print("2- View Results")
    print("3- Exit\n")
    userChoice = input("Please enter your menu choice:\n")
    if int(userChoice) == 1:
        UserID()
    if int(userChoice) == 2:
        ViewResults()
    while not validateChoice(userChoice):
        userChoice = input("Please enter your menu choice:\n")
        validateChoice(userChoice)
        #grab userChoice for input
        print(userChoice)


def UserID():
    now = datetime.now()
    time_string = now.strftime('%H:%M:%S')
    name = ''
    studentID = ''
    name = input('Please enter your first and last name: ')
    studentID = input('Enter your student ID: ')
    if studentID.isdigit():
        print('Name: ' + name)
        print('Student ID: ' + studentID)
        print('Time: ', time_string)
        print('Press any key to begin the quiz...')
        Question()
    else: 
        print('Either the information you have entered is invalid, or your student ID does not meet the requirements.')
        print('Requirements: Numbers Only, 10 Character Limit')
def Question():
    #initialize and define all variables
    index = 0
    question1Array = ['Question 1: A video display is a(n)...\n','1. Output device\n','2. Input device\n','3. Control device\n','4. Cord that you plug into your television\n']
    question2Array = ['Question 2: A(n) ___ sets a variable to a specified value.\n','1. Variable declaration\n','2. Not a variable declaration\n','3. Not even close to a variable declaration\n','4. None of the above\n']
    question3Array = ['Question 3: You ___ the module to execute it\n.','1. Call\n','2. Infinitely loop\n','3. Create\n','4. Print\n']
    question4Array = ['Question 4: A(n) ___ expression.\n','1. Not boolean 1\n','2. Not boolean 2\n','3. Not boolean 3\n','4. Boolean\n']
    #while loop that steps through each index and prints them out
    while index < 5:
        print(question1Array[index])
        index = index + 1
    #request user input
    question1Response = input('Please enter the integer associated with your answer choice: ')
    #assure a response from 1-4
    if int(question1Response) < 1 or int(question1Response) > 4:
        print('Invalid input. Integer must be from 1-4.')
        question1Response = print('Please enter the integer associated with your answer choice: ')
    #reset index to 0 so the other while loops can step through the array
    index = 0
    while index < 5:
        print(question2Array[index])
        index = index + 1
    question2Response = input('Please enter the integer associated with your answer choice: ')
    if int(question2Response) < 1 or int(question2Response) > 4:
        print('Invalid input. Integer must be from 1-4.')
        question2Response = print('Please enter the integer associated with your answer choice: ')
    index = 0
    while index < 5:
        print(question3Array[index])
        index = index + 1
    question3Response = input('Please enter the integer associated with your answer choice: ')
    if int(question3Response) < 1 or int(question3Response) > 4:
        print('Invalid input. Integer must be from 1-4.')
        question3Response = print('Please enter the integer associated with your answer choice: ')
    index = 0
    while index < 5:
        print(question4Array[index])
        index = index + 1
    question4Response = input('Please enter the integer associated with your answer choice: ')
    if int(question4Response) < 1 or int(question4Response) > 4:
        print('Invalid input. Integer must be from 1-4.')
        question4Response = print('Please enter the integer associated with your answer choice: ')
    results = open('results.txt', 'w')
    results.write(str(question1Response) + str(question2Response) + str(question3Response) + str(question4Response))
    results.close
    ViewResults()
'''
def WriteResults():
with open('quiz_results.txt','w') as results:
    results.write(question1Response, question2Response, question3Response, question4Response)
    results.close()
ViewResults()
'''

def ViewResults():
    results = open('results.txt' 'r')
    print(results)
MainMenu()

