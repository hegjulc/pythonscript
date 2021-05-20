import os
os.system('cls')

print("1. Get the information and display to screen")
print("2. Call user created functions")
print("3. Write list of files to file")
print("4. Read specified file")
print("")
choice = input("Enter number of task to do: ")

def GetState():
    state = input("What is the name of your state?")
    return state;

def FormatState(state)
     stateCount = len(state)
     while stateCount < 8:
        FormattedState = state.ljust(1)
        stateCount = len(FormattedState)
        return state;

if choice == 1:
    companyName = "Dunwoody College"
    programName = "Computer Networking"
    uName = os.environ['username']
    classFirst = input("What is the name of your first class?")
    classSecond = input("What is the name of your second class?")
    print("I'm", uName "My first class is", classFirst ". My second class is ", classSecond ". I go to ", companyName " where I take", programName ".")
    
elif choice = 2:
        state = GetState()
        newState = FormatState()
        FormatState(state)
        print(state,"Was the name of the state, it is now ",newState)
        
elif choice = 3:
        fileName = input("What is the name of the file you would like to create?")
        os.system('touch ',fileName'.txt.')
        
elif choice = 4:
        fileChoice = input("What is the name of the text file you would like to read?")
        os.system('cat ',fileChoice)
    


