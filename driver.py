from header import *
import pickle

def main():
    movies = []
    pickle_in = open("data.pickle", "rb")
    movies = pickle.load(pickle_in)
    myDatabase = Database(movies)

    while True:
        choice = input('1. Add New Movie\n'
                        '2. Rate a Movie\n'
                        '3. List All Movies\n'
                       '4. Movie Suggestions\n'
                        '5. Save and Exit\n')

        if choice == '1':
            title = input('Title: ')
            director = input('Director: ')
            rating = str(input('Rating(enter 0 if not watched): '))
            myDatabase.addMovie(title, director, rating)

        elif choice == '2':
            myDatabase.rateMovie()
        elif choice == '3':
            myDatabase.listMovies()
        elif choice == '4':
            myDatabase.listWantedMovies()
        else:
            pickle_out = open('data.pickle', 'wb')
            pickle.dump(movies, pickle_out)
            print(choice)
            break

main()