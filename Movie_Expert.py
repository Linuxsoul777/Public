def read_file():
    with open ('VS Code/Public/movieData.txt', 'r')as movieData:
        for data in movieData:
            newdata = data.rstrip('\n')
            movie, mainGuy = newdata.split('/')
            print (movie)
            print (mainGuy)

read_file()
