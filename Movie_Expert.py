#!/usr/bin/python3
from tkinter import simpledialog, messagebox, Tk

## NOTE! Replace VS Code/Public/movieData.txt with the aboslute path of the location of this file on your computer.

def write_file(movie, mainGuy, length):
    '''creates variable to write to file movieData'''
    with open('/mnt/HD 1/VS Code/Public/movieData.txt', 'a') as data: 
        movie = movie.lower()
        mainGuy = mainGuy.lower()
        data.write('\n' + movie + '/' + mainGuy + '/' + length)    # writes to file

def character_search():
    '''Creates a function to search for movie info and interact with the user'''
    movieInput = simpledialog.askstring ('Movie Expert',"What movie would you like to find out more about? (You can type e to quit)")
    with open ('/mnt/HD 1/VS Code/Public/movieData.txt', 'r')as movieData:            # opens movieData
        for data in movieData:
            newdata = data.rstrip('\n')
            movie, mainGuy, length = newdata.split('/')                     # assigns variables for each of the nuggets of info
            if movieInput.lower() == movie:
                messagebox.showinfo(movieInput.title(), "The main actor is: \n" + mainGuy.title() + "\nThe length of the movie is: \n" + str(length))              # returns info for user
                return
            elif movieInput.lower() == 'e':                                 # allows for an exit command
                messagebox.showinfo('Farewell!',"Ok then, Good Bye!")
                exit()
        if movieInput != movie:                                             # allows to file new information
            answer = messagebox.askyesnocancel('ERROR! Movie not filed.',"Would you like to add this movie's details?")
            if answer is True:
                mainActor = simpledialog.askstring('Main Actor', "OH GOODY GOODY! \nWho is the main actor in the movie?")
                movieLength = simpledialog.askstring('Length',"Great, now what is the length of the movie? \n(Please put convert to minutes... e.g (120 minutes)")
                write_file (movieInput, mainActor, movieLength)             # writes to file
                return
            elif answer is False:
                messagebox.showinfo(' ', "I am sad. Have a great day!")
                exit()
           
root = Tk()
root.withdraw()

def startUp_interface():
    '''Creates a funtion for the start-up interface'''
    userInput = messagebox.askyesnocancel('Movie Expert',"Would you like to find out more about movies?")
    while userInput is not False:
        if userInput is True:
            character_search()
    messagebox.showinfo('Answer', "Ok, your loss. Have a great day!")

startUp_interface()
