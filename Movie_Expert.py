def read_file():
    with open ('VS Code/Public/movieData.txt', 'r')as movieData:
        for data in movieData:
            newdata = data.rstrip('\n')
            movie, mainGuy = newdata.split('/')
            # print (movie)
            # print (mainGuy)

def write_file(movie, mainGuy):
    with open('VS Code/Public/movieData.txt', 'a') as data: 
        data.write('\n' + movie + '/' + mainGuy)

def character_search():
    pass
def user_interface():
    read_file()
    print ("Would you like to find out more about movies?")
    userInput = input()
    userInput = userInput.lower()
    if userInput == 'yes':
        character_search()
    elif userInput == 'no':
        print("Ok, your loss. have a great day!")
    else:
        print ("I'm sorry that wasn't a yes or a no.")
    
user_interface()
