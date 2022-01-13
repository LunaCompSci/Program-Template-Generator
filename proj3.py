#Christina Nguyen, 1/24/21, creates an attractive Python program banner and section headings
global STAR_LENGTH 
STAR_LENGTH = 70

def main(): #calls function
    collectInputs()
    displayBanner()
    displaySectHeaders()
        
def collectInputs():  #asks user for input
    global name, date, programName, description
    name = input("Enter your name: ")
    date = input("Enter the date: ")
    programName = input("Enter the program name: ")
    description = input("Enter short description: ")

def displayBanner(): #displays banner
    displayStarLine()
    print("#\tCoder\t:  ", name)
    print("#\tDate\t:  ", date)
    print("#\tProgram\t:  ", programName)
    print("#\tDescrip\t:  ", description)
    displayStarLine()
    
def displaySectHeaders(): #display Section Headers #Gives argument to parameter
    print("\n" * 2)
    displaySectHeader("Constants")
    print("\n" * 2)
    displaySectHeader("Variables")
    print("\n" * 2)
    displaySectHeader("Input")
    print("\n" * 2)
    displaySectHeader("Processing")
    print("\n" * 2)
    displaySectHeader("Output")
    
def displaySectHeader(sectionName): #display Section Header #Receives argument
    displayStarLine()
    print("#\t",sectionName, sep='')
    displayStarLine()
    
    
def displayStarLine(): #display star line
    print("#" + "*" * STAR_LENGTH)

main()

#For testing I had #None twice in my output.
#After going to Bill I found that I was giving an empty agrument to the varibles I had assigned to displaySectHeader calls.
#The variables needed to there in the first place because I was trying to return an argrument and needed a place to store them.
#I learned from this assignment that not every parameter needs the keyword "return".
#I'm suprised my program didn't  break. Now I know one reason why Python is considered a forgiving language. 
#On the next project I'll draw arrows on the call hierarchy showing where the agruments are moving within the parameters. I think that will keep me more organized.
#Something I would like to fix as I learn more is how to loop those print("\n" * 2) lines. They were a lot to type.
#For my test cases, when I gave really long inputs, the second line would start under the hashtag rather than the colon.
#However, when I expand by shell, no second line is necessary and it looks nice. 
#In the future I would like to change my code so the second line lines up with the colon. 
