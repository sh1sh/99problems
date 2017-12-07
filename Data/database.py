import wikipedia, os, linecache

class Database:

    def myConstants():
        months = ['January','February','March']#,'April','May','June','July','August','September','October','November','December']
        days = [1, 2, 3,4]#,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        return (months,days)

    def createDatabase():
        myData = Database.myConstants()
        try:
            os.mkdir('Months')
        except:
            pass

        for m in myData[0]:
            for d in myData[1]:
                nameFile = str(m) + '_' + str(d)
                try:
                    os.makedirs('Months/' + m)
                except:
                    pass     # open('Months/January/January_1', 'w')
                pathFile = ('Months/' + m + '/' + nameFile)
                file = open((pathFile), 'w')
                article = wikipedia.page(nameFile)
                file.write(article.content)
                file.close()
        return ('Database is created')

    def readDatabase():
        myData = Database.myConstants()
        for m in myData[0]:
            for d in myData[1]:
                nameFile = m + '_' + str(d)
                pathFile = ('Months/' + m + '/' + nameFile)
                database = open(pathFile, 'r')
        return database

    def searchTags():
        data = Database.readDatabase()
        tags = []
        for line in data:
            textSearch = line
            if textSearch.startswith('=='):
                textSearch = textSearch.split('\n')
                tags.append(textSearch[0])
        data.close()
        return tags

    def setContentForTag():
        data = Database.readDatabase()
        tags = Database.searchTags()
        months = Database.myConstants()
        month = months[0]
        try:
            os.mkdir('Category')
        except:
            pass
        for i, line in enumerate(data):
            for tag in tags:
                if tag in line:
                    text = tag.strip('==').strip(' ')
                    pathToDir = ('Category/' + text)
                    try:
                        os.mkdir(pathToDir)
                    except:
                        pass
                    return tag
                # Write to file content of current category. Need to find the solution how to extract content to file in category.
                if tag in line:

                    print(s)



        data.close()
        pass


#Database.readDatabase()
#Database.createDatabase()

#myData = Database.myConstants()
#print(myData[0])

#print(Database.searchTags())

Database.setContentForTag()