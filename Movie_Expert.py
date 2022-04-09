def read_file():
    with open ('VS Code/Public/movieData.txt', 'r')as movieData:
        for data in movieData:
            newdata = data.rstrip('\n')
            movie, mainGuy = newdata.split('/')
            print (movie)
            print (mainGuy)

def write_file(movie, mainGuy):
    with open('VS Code/Public/movieData.txt', 'a') as data: 
        data.write('\n' + movie + '/' + mainGuy)

read_file()
write_file()
