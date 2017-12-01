movies = {
    2005 : [{'title' : 'Munich', 'director' : 'Steven Spielberg'}],
    2006 : [
        {'title' : 'The Prestige', 'director' : 'Christopher Nolan'},
        {'title' : 'The Departed', 'director' : 'Martin Scorsese'},
    ],
    2007 : [{'title' : 'Into the Wild', 'director': 'Sean Penn'}],
    2008 : [{'title' : 'The Dark Knight', 'director': 'Christopher Nolan'}],
    2009 : [{'title' : 'Mary and Max', 'director': 'Adam Elliot'}],
    2010 : [{'title' : 'The King\'s Speech', 'director': 'Tom Hooper'}],
    2011 : [
        {'title' : 'The Artist', 'director' : 'Michel Hazanavicius'},
        {'title' : 'The Help', 'director' : 'Tate Taylor'},
    ],
    2012 : [{'title' : 'Argo', 'director': 'Ben Affleck'}],
    2013 : [{'title' : '12 Years a Slave', 'director': 'Steve McQueen'}],
    2014 : [{'title' : 'Birdman', 'director': 'Alejandro G. Inarritu'}],
    2015 : [{'title' : 'Spotlight', 'director': 'Tom McCarthy'}],
    2016 : [{'title' : 'The BFG', 'director': 'Steven Spielberg'}],
}

promptUser = int(input('Enter a year between 2005 and 2016:\n'))

if promptUser < 2005 or promptUser > 2016:
    print('N/A')
else:
    list_movies_year = movies[promptUser]
    for item in list_movies_year:
        print(item['title'] + ', ' + item['director'])
    print('')

display_option = True

while display_option:
    print('MENU')
    print('Sort by:')
    print('y - Year')
    print('d - Director')
    print('t - Movie title')
    print('q - Quit\n')
    menu_option = input('Choose an option:\n')
    if menu_option == 'q':
        display_option = False
        continue
    elif menu_option == 'y':
        for key in sorted(movies.keys()):
            print(str(key) + ':')
            items = movies[key]
            for i in items:
                print('\t' + i['title'] + ', ' + i['director'])
            print('')
    elif menu_option == 'd':
        all_directors = []
        for key in movies.keys():
            items = movies[key]
            for i in items:
                all_directors.append(i['director'])
        unique_director_container = []
        for director in all_directors:
            if director not in unique_director_container:
                unique_director_container.append(director)
        unique_director_container.sort()
        for director in unique_director_container:
            print(director + ':')
            for key in sorted(movies.keys()):
                items = movies[key]
                for item in items:
                    if director == item['director']:
                        print('\t' + item['title'] + ', ' + str(key))
            print('')
    elif menu_option == 't':
        all_titles = []
        for key in movies.keys():
            items = movies[key]
            for i in items:
                all_titles.append(i['title'])
        unique_title_container = []
        for title in all_titles:
            if title not in unique_title_container:
                unique_title_container.append(title)
        unique_title_container.sort()
        for title in unique_title_container:
            print(title + ':')
            for key in movies.keys():
                items = movies[key]
                for item in items:
                    if title == item['title']:
                        print('\t' + item['director'] + ', ' + str(key))
            print('')
    else:
        continue