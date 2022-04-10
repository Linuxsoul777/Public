## NOTE! Replace VS Code/Public/movieData.txt with the aboslute path of the location of this file on your computer.

def write_file(movie, mainGuy, length):
    '''creates variable to write to file movieData'''
    with open('VS Code/Public/movieData.txt', 'a') as data: 
        movie = movie.lower()
        mainGuy = mainGuy.lower()
        data.write('\n' + movie + '/' + mainGuy + '/' + length)    # writes to file


def character_search():
    '''Creates a function to search for movie info and interact with the user'''
    print ("What movie would you like to find out more about? (You can type e to quit)")
    movieInput = input()
    with open ('VS Code/Public/movieData.txt', 'r')as movieData:            # opens movieData
        for data in movieData:
            newdata = data.rstrip('\n')
            movie, mainGuy, length = newdata.split('/')                     # assigns variables for each of the nuggets of info
            if movieInput.lower() == movie:
                print ("The main actor is " + mainGuy.title())              # returns info for user
                print ("The length of the movie is: " + str(length))
                return
            elif movieInput.lower() == 'e':                                 # allows for an exit command
                print ("Ok then, Good Bye!")
                exit()
        if movieInput != movie:                                             # allows to file new information
            print ("ERROR! Movie not filed.")
            print ("Would you like to add this movie's details? (yes/no)")
            answer = input()
            if answer.lower() == 'yes':
                print ("OH GOODY GOODY!")
                print ("Who is the main actor in the movie?")
                mainActor = input()
                print ("Great, now what is the length of the movie? (Please put convert to minutes... e.g (120 minutes)")
                movieLength = input() 
                write_file (movieInput, mainActor, movieLength)             # writes to file
                return
            elif answer.lower == 'no':
                print ("I am sad. Have a great day!")
                exit()

                

def startUp_interface():
    '''Creates a funtion for the start-up interface'''
    print ("Would you like to find out more about movies?")
    userInput = input()
    while userInput.lower() != 'no':
        if userInput.lower() == 'yes':
            character_search()
        else:
            print ("I'm sorry that wasn't a yes or a no.")
            userInput = input()
    print ("Ok, your loss. Have a great day!")
startUp_interface()
